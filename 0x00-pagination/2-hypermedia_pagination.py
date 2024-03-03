#!/usr/bin/env python3
""" Module that paginates popular baby names database"""

from typing import Tuple
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """paginates popular baby names database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """displays the dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ function performs simple pagination"""
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer > 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page_size must be an integer > 0"
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset) or end > len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns list/page of the dataset """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        result = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return result
