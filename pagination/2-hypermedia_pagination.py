#!/usr/bin/env python3
""" simple pagination with python """
import csv
import math
from typing import List
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes two ints and returns a list of lists """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        (start, end) = index_range(page, page_size)
        readingList = []

        if end < len(self.dataset()):
            for newPage in range(start, end):
                readingList.append(self.dataset()[newPage])

        return readingList

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
            returns a dict with page_size, page, data,
            next_page, prev_page, and total_pages
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
