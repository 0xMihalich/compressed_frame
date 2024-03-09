from typing import Union

from pandas import DataFrame as PdDF
from polars import DataFrame as PlDF

from .error import DataFrameTypeError


def frame_type(data_frame: Union[PlDF, PdDF,]) -> str:
    """Определение типа DataFrame."""

    if not isinstance(data_frame, Union[PlDF, PdDF,]):
        raise DataFrameTypeError(type(data_frame))
    
    return {PlDF: "polars_frame", PdDF: "pandas_frame"}[type(data_frame)]
