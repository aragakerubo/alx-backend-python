#!/usr/bin/env python3
"""Type-annotated function safe_first_element that takes a sequence input_seq
of any type and returns its first element if available."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence if available."""
    if lst:
        return lst[0]
    else:
        return None
