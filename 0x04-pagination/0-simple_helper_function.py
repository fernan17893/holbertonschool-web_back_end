#!/usr/bin/env python3
"""task 0"""

def index_range(page, page_size):
    """Return a tuple of size two containing a start index and an end index
       corresponding to the range of indexes to return in a list for those
       particular pagination parameters.

       page: current page number
       page_size: number of items per page
       Return: a tuple of size two
    """
    return ((page - 1) * page_size, page * page_size)
