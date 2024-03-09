from pickle import loads, dumps
from typing import Any, Union

from pandas import DataFrame as PdDF
from polars import DataFrame as PlDF

from .error import DataFrameTypeError, PickleDumpError


def to_pickle(data_frame: Union[PlDF, PdDF,]) -> bytes:
    """Конвертация DataFrame в pickle dump."""

    if not isinstance(data_frame, Union[PlDF, PdDF,]):
        raise DataFrameTypeError(type(data_frame))
    
    return dumps(obj=data_frame,
                 protocol=4,)
    

def from_pickle(pickle_dump: bytes) -> Union[PlDF, PdDF,]:
    """Конвертация pickle dump в DataFrame."""

    if not isinstance(pickle_dump, bytes):
        raise PickleDumpError()

    data_frame: Union[PlDF, PdDF, Any,] = loads(pickle_dump)

    if not isinstance(data_frame, Union[PlDF, PdDF]):
        raise DataFrameTypeError(type(data_frame))
    
    return data_frame
