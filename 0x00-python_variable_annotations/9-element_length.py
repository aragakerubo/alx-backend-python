#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list lst as argument
and returns the length of the list as an integer"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each with a sequence and its length."""
    return [(i, len(i)) for i in lst]
