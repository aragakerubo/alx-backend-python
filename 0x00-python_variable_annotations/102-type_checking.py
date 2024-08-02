#!/usr/bin/env python3
"""Type-annotated function type_checking with mypy which takes
a variable x of type Tuple and returns the sum as a float."""
from typing import Tuple, Union


def type_checking(n: Union[int, float]) -> Union[int, float]:
    """Return the sum of a tuple of floats."""
    return n
