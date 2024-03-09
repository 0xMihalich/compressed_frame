from typing import NamedTuple


class CompactFrame(NamedTuple):
    """Структура объекта сжатого объекта."""

    type:           str   # Тип DataFrame (pandas/polars)
    columns:        str   # Строковое представление списка колонок List[str]
    dtypes:         str   # Строковое представление списка типов данных List[str]
    num_columns:    int   # Количество колонок в DataFrame
    frame_count:    int   # Количество строк в DataFrame
    pickle_size:    int   # Размер pickle dump DataFrame
    size:           int   # Размер сжатого файла в байтах
    compress_ratio: float # Процент сжатия
    crc32:          str   # Контрольная сумма zlib
    data:           str   # Hex строка

    def __str__(self: "CompactFrame") -> str:
        """Строковое отображение класса."""

        string_output: str = "\n".join((f"CompactFrame for {self.type.replace('_frame', ' DataFrame')}",
                                        "---------------------------------",
                                        f"Columns:             {self.columns}",
                                        f"Data types:          {self.dtypes}",
                                        f"Columns numbers:     {self.num_columns}",
                                        f"DataFrame count:     {self.frame_count}",
                                        f"Size as pickle dump: {self.pickle_size} bytes",
                                        f"Compressed size:     {self.size} bytes",
                                        f"Copmressed ratio:    {self.compress_ratio}%",
                                        f"CRC32:               {self.crc32}",),)

        return string_output

    def __repr__(self: "CompactFrame") -> str:
        """Строковое отображение класса в интерпретаторе."""

        return self.__str__()
