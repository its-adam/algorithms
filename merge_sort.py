#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  merge_sort.py
#

"""use merge_sort to sort a list of values in O(n log n) time
   additionally, count the number of inversions in the original list w/o altering O(n log n) run time
"""


def get_input(file):
    """read an input file and return the values as a list of integers"""
    
    lst = []
    with open(file, mode="rt", encoding="utf-8") as f:
        for line in f:
            lst.append(int(line.strip()))
    return lst


def split_list(lst):
    """split a list into two separate lists"""
    half = len(lst)//2
    left = lst[:half]
    right = lst[half:]
    return left, right


def merge(left, right, output, inversions):
    """merge two sorted lists together while counting the number of split inversions between them
    take in 'output' as an argument so that it does in-place edits to the original list."""
    # TODO: remove output from argument list
    i = 0
    j = 0
    k = 0
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
    return inversions


def merge_sort(lst, inversions):
    """merge_sort algorithm"""
    if len(lst) <= 1:
        return inversions
    
    (left, right) = split_list(lst)

    (inversions) = merge_sort(left, inversions)
    (inversions) = merge_sort(right, inversions)

    inversions = merge(left, right, lst, inversions)
    
    return inversions


def main(args):
    # input_file = ''
    # input_list = get_input(input_file)

    input_list = [1, 3, 5, 2, 4, 6]   # 3 inversions (all are split) -- other cases are covered in test_merge_sort.py
    input_list = [89, 76, 2, 4, 1, 5435, 0, 1, 129, 43, 34, 56, 82]
    input_list_bk = input_list[:]  # merge_sort() will update input_list directly
    
    inversions = 0
    inversions = merge_sort(input_list, inversions)
    
    print('original list: {}\n  sorted list: {}\ninversions: {}'.format(input_list_bk, input_list, inversions))
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
