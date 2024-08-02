#!/usr/bin/env python3
"""Type-annotated function safely_get_value that takes a dict input_dict of
type Mapping, a key key of type Any, a default value default of type Union[T, None],
and returns the value with key key in input_dict if key is present, or default."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Return the value with key key in input_dict if key is present, or default."""
    if key in dct:
        return dct[key]
    else:
        return default
