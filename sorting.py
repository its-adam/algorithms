# -*- coding: utf-8 -*-
#
#  sorting.py
#
"""library of sorting algorithms"""

from random import randrange


# quick_sort


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
    quick sort algorithm with O(n log n) average run time when using random pivot selection
        usage: quick_sort(array, 0, len(array))
        returns sorted list
        also mutates original list by sorting it in place
    """
    
    if left < right - 1:
        boundary_index = partition(lst, left, right)
        
        # smaller  pivot  larger
        # [:b_i]   [b_i]  [b_+1:]
        
        quick_sort(lst, left, boundary_index)  # python slicing is exclusive on msb
        quick_sort(lst, boundary_index + 1, right)
    return lst


# merge_sort


def split_list(lst):
    """split a list into two separate lists of equal length"""
    half = len(lst) // 2
    left = lst[:half]
    right = lst[half:]
    return left, right


def merge(left, right, output, inversions):
    """merge two sorted lists together while counting the number of split inversions between them"""
    i = 0
    j = 0
    k = 0
    # TODO: figure out how to remove the in place mutation of original list
    # output = list(range(len(left) + len(right)))
    while k < len(left) + len(right):
        # repeated values do not count as an inversion
        if left[i] <= right[j]:
            output[k] = left[i]
            i = i + 1
            k = k + 1
        elif left[i] > right[j]:
            output[k] = right[j]
            j = j + 1
            k = k + 1
            inversions = inversions + len(left) - i
        if i == len(left):
            output[k:] = right[j:]
            break
        if j == len(right):
            output[k:] = left[i:]
            break
    return output, inversions


def merge_sort(lst, inversions):
    """
    merge_sort algorithm with O(n log n) run time
        usage: merge_sort(lst, 0)
        returns the sorted list and the number of inversions in the original list
        current implementation also mutates the original list by sorting it in place
    """
    
    if len(lst) > 1:
        (left, right) = split_list(lst)
    
        (lst_l, inversions) = merge_sort(left, inversions)
        (lst_r, inversions) = merge_sort(right, inversions)
    
        (lst, inversions) = merge(left, right, lst, inversions)
    
    return lst, inversions


# insertion_sort
def insertion_sort(lst, order="normal"):
    """
    in place, non-recursive sorting method with O(n**2) run time
        usage: insertion_sort(lst, [order='reverse'])
        returns sorted list
        also mutates original list by sorting it in place
    """
    
    for i in range(1, len(lst)):
        current_value = lst[i]
        
        j = i - 1
        if order == "normal":
            while j >= 0 and lst[j] > current_value:
                lst[j + 1] = lst[j]
                lst[j] = current_value
                j -= 1
        elif order == "reverse":
            while j >= 0 and lst[j] < current_value:
                lst[j + 1] = lst[j]
                lst[j] = current_value
                j -= 1
    return lst


# bubble_sort
