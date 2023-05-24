#!/usr/bin/env python3
"""
Annotate the below functions parameters
and return values with the appropriate types
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return list of tuple with items and lenght of each items
    """
    return [(i, len(i)) for i in lst]
