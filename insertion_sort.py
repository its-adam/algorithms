#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertion_sort.py
#


def insertion_sort(lst, method="increasing"):
    """in place, non-recursive sorting method with O(n**2) run time"""
    
    for i in range(1, len(lst)):
        current_value = lst[i]
        
        j = i - 1
        if method == "increasing":
            while j >= 0 and lst[j] > current_value:
                lst[j+1] = lst[j]
                lst[j] = current_value
                j -= 1
        elif method == "reverse":
            while j >= 0 and lst[j] < current_value:
                lst[j+1] = lst[j]
                lst[j] = current_value
                j -= 1

    return lst


def main(args):
    """run insertion_sort on a list"""
    
    input_list = [6, 5, 4, 3, 2, 1]
    # input_list = [1, 1, 2, 3, 4, 5, 6]
    input_list_bk = input_list[:]
    
    print("main::")
    sorted_list = insertion_sort(input_list)
    print("  original list: {}".format(input_list_bk))
    print("    sorted list: {}".format(sorted_list))
    sorted_list = insertion_sort(input_list_bk, method="reverse")
    print("  original list: {}".format(input_list_bk))
    print("    sorted list: {}".format(sorted_list))

    return 0


if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))