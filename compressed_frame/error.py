class CompactFrameError(Exception):
    """Базовый класс ошибки."""


class DataFrameTypeError(CompactFrameError):
    """Неизвестный тип данных."""

    def __init__(self: "DataFrameTypeError",
                 dtype: type,) -> None:
        
        super().__init__(f"Don't support type {dtype}")


class PickleDumpError(CompactFrameError):
    """Переданы не байты."""

    def __init__(self: "PickleDumpError") -> None:
        
        super().__init__("pickle dump not a bytes.")


class ZlibError(CompactFrameError):
    """Переданы не байты."""

    def __init__(self: "ZlibError") -> None:
        
        super().__init__("zlib data compress not a bytes.")


class DataError(CompactFrameError):
    """Передана не строка."""

    def __init__(self: "DataError") -> None:
        
        super().__init__("data tuple not a hex string.")


class CompressedFrameError(CompactFrameError):
    """Неизвестный тип данных."""

    def __init__(self: "CompressedFrameError") -> None:
        
        super().__init__("DataFrame must be pandas.DataFrame, polars.DataFrame, "
                         "compact_frame.CompactFrame, List or Tuple with CompactFrame struct type.")


class Crc32Error(CompactFrameError):
    """Не совпадает контрольная сумма."""

    def __init__(self: "CompressedFrameError") -> None:
        
        super().__init__("Data crc32 not valid.")
