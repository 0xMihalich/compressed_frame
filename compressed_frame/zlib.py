from zlib import compress, decompress

from .error import PickleDumpError, ZlibError


def to_zlib(pickle_dump: bytes,
            level: int = 9,) -> bytes:
    """Сжатие pickle dump."""

    if not isinstance(pickle_dump, bytes):
        raise PickleDumpError()
    
    return compress(pickle_dump, level=level)


def from_zlib(zlib_data: bytes) -> bytes:
    """Распаковка zlib data."""

    if not isinstance(zlib_data, bytes):
        raise ZlibError()
    
    return decompress(zlib_data)
