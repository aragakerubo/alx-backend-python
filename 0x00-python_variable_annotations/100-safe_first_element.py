#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a sequence input_seq
of any type and returns its first element if available."""
from typing import Union, Sequence, Any, TypeVar


T = TypeVar("T")


def safe_first_element(input_seq: Sequence[T]) -> Union[T, None]:
    """Return the first element of a sequence if available."""
    if input_seq:
        return input_seq[0]
    else:
        return None
