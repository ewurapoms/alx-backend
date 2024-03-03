#!/usr/bin/env python3
""" Module function takes two integer args and return a tuple """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function returns a tuple """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
