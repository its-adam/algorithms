#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sorting.py
#

from random import randrange

"""library of sorting algorithms"""


def partition(lst, left, right):
    """
    routine to partition a given array of len(right - left)
        msb is lst[right-1]
        returns the index where the pivot was finally placed
        partitioning is done in place
    """
    pivot_index = randrange(left, right-1)
    if pivot_index != left:
        (lst[left], lst[pivot_index]) = (lst[pivot_index], lst[left])
        pivot_index = left
    
    pivot = lst[pivot_index]
    # the index where pivot will end up being placed
    i = pivot_index
    for j in range(left + 1, right):
        if lst[j] < pivot:
            i += 1
            (lst[i], lst[j]) = (lst[j], lst[i])
    
    (lst[pivot_index], lst[i]) = (lst[i], lst[pivot_index])
    return i


def quick_sort(lst, left, right):
    """
    quick sort algorithm
        usage: quick_sort(array, 0, len(array))
    """
    
    if left < right - 1:
        boundary_index = partition(lst, left, right)
        
        # smaller  pivot  larger
        # [:b_i]   [b_i]  [b_+1:]
        
        quick_sort(lst, left, boundary_index)  # python slicing is exclusive on msb
        quick_sort(lst, boundary_index + 1, right)
    return lst
