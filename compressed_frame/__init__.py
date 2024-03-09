from typing import List, Tuple, Union

from pandas import DataFrame as PdDF
from polars import DataFrame as PlDF

from .data import to_compact_frame, from_compact_frame
from .error import CompressedFrameError
from .struct import CompactFrame


class SimpleType:
    """Базовый тип возвращаемого из json объекта.
       TODO Не доделано. Я потом сделаю рефакторинг этого места."""

    def __init__(self: "SimpleType",
                 tuple_frame: Union[List, Tuple,]) -> None:
        
        if not isinstance(tuple_frame, Union[List, Tuple,]):
            raise CompressedFrameError()


class CompressedFrame:
    """Класс для Apache Airflow."""

    def __init__(self: "CompressedFrame",
                 data_frame: Union[SimpleType, CompactFrame, PlDF, PdDF,],
                 level: int = 9,) -> None:
        """Инициализация класса."""

        self.data_frame: CompactFrame
        self.level: int = level

        if isinstance(data_frame, Union[PlDF, PdDF,]):
            self.data_frame = to_compact_frame(data_frame=data_frame,
                                               level=level,)
        elif isinstance(data_frame, CompactFrame):
            self.data_frame = data_frame
        elif isinstance(data_frame, Union[List, Tuple]):
            if len(data_frame) == 10:
                if (all(isinstance(item, str) for item in data_frame[:3])
                    and all(isinstance(item, int) for item in data_frame[3:7])
                    and isinstance(data_frame[7], float)
                    and isinstance(data_frame[8], str)):
                    self.data_frame = CompactFrame(*data_frame)
                else:
                    raise CompressedFrameError()
            else:
                raise CompressedFrameError()
        else:
            raise CompressedFrameError()

    def __str__(self: "CompressedFrame") -> str:
        """Строковое отображение класса."""

        return self.data_frame.__str__()

    def __repr__(self: "CompressedFrame") -> str:
        """Строковое отображение класса в интерпретаторе."""

        return self.__str__()
    
    @property
    def push(self: "CompressedFrame") -> Tuple[str, str, str, int, int, int, int, float, str, str,]:
        """Отправить в xom кортеж объекта CompactFrame."""

        return tuple(self.data_frame)
    
    @property
    def pull(self: "CompressedFrame") -> Union[PlDF, PdDF,]:
        """Получить из xcom распакованный DataFrame."""

        return from_compact_frame(self.data_frame)
