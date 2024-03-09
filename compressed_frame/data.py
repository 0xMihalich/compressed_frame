from typing import Any, Union
from zlib import crc32

from pandas import DataFrame as PdDF
from polars import DataFrame as PlDF

from .error import CompactFrameError, Crc32Error, DataFrameTypeError, DataError, ZlibError
from .pickle import to_pickle, from_pickle
from .struct import CompactFrame
from .type_checker import frame_type
from .zlib import to_zlib, from_zlib


def to_hex(zlib_data: bytes) -> str:
    """Преобразовать zlib data в hex string."""

    if not isinstance(zlib_data, bytes):
        raise ZlibError()
    
    return zlib_data.hex()


def from_hex(data: str) -> bytes:
    """Преобразовать hex string в zlib data."""

    if not isinstance(data, str):
        raise DataError()
    
    return bytes.fromhex(data)


def to_compact_frame(data_frame: Union[Any, PlDF, PdDF,],
                     level: int = 9,) -> CompactFrame:
    """Упаковать DataFrame в объект CompactFrame."""

    pickle_dump: bytes = to_pickle(data_frame)
    zlib_data:   bytes = to_zlib(pickle_dump=pickle_dump,
                                 level=level,)

    _type:           str   = frame_type(data_frame)
    _columns:        str   = str(list(data_frame.columns))
    _dtypes:         str   = str(list(data_frame.dtypes))
    _num_columns:    int   = len(data_frame.columns)
    _frame_count:    int   = len(data_frame)
    _pickle_size:    int   = len(pickle_dump)
    _size:           int   = len(zlib_data)
    _compress_ratio: float = round((1 - _size / _pickle_size) * 100, 2)
    _crc32:          str   = hex(crc32(zlib_data))[2:]
    _data:           str   = to_hex(zlib_data)

    return CompactFrame(_type,
                        _columns,
                        _dtypes,
                        _num_columns,
                        _frame_count,
                        _pickle_size,
                        _size,
                        _compress_ratio,
                        _crc32,
                        _data,)


def from_compact_frame(compact_frame: CompactFrame) -> Union[PlDF, PdDF]:
    """Распаковать CompactFrame в DataFrame."""

    if not isinstance(compact_frame, CompactFrame):
        raise CompactFrameError(f"Type {type(compact_frame)} don't support.")
    
    zlib_data:   bytes                   = from_hex(data=compact_frame.data)

    if compact_frame.crc32 != hex(crc32(zlib_data))[2:]:
        raise Crc32Error()

    pickle_dump: bytes                   = from_zlib(zlib_data)
    data_frame:  Union[Any, PlDF, PdDF,] = from_pickle(pickle_dump)

    if not isinstance(data_frame, Union[PlDF, PdDF,]):
        raise DataFrameTypeError(type(data_frame))
    
    return data_frame
