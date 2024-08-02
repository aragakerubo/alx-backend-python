#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list lst as argument
and returns the length of the list as a float."""
from typing import List, Union


def element_length(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """Return the length of a list of floats and integers."""
    return [len(lst)]
