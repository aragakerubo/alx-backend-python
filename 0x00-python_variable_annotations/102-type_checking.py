#!/usr/bin/env python3
"""Type-annotated function type_checking with mypy which takes
a variable x of type Tuple and returns the sum as a float."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list of tuples, each with a sequence and its length."""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
