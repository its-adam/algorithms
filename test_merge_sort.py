import unittest
import merge_sort
import insertion_sort


class SortTests(unittest.TestCase):
    def test_best_case_sorted_list_no_inversions(self):
        self.assertEqual(merge_sort.merge_sort(lst=[1, 2, 3, 4, 5, 6], inversions=0), 0)
        self.assertEqual(insertion_sort.insertion_sort(lst=[1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_worst_case_reverse_list_nlogn_inversions(self):
        self.assertEqual(merge_sort.merge_sort(lst=[6, 5, 4, 3, 2, 1], inversions=0), 15)
        self.assertEqual(insertion_sort.insertion_sort(lst=[6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])

    def test_worst_case_reverse_list_nlogn_inversions2(self):
        self.assertEqual(merge_sort.merge_sort(lst=[6, 5, 4, 3, 2, 1], inversions=0), int(6*(6-1)/2))

    def test_all_split_case(self):
        self.assertEqual(merge_sort.merge_sort(lst=[1, 3, 5, 2, 4, 6], inversions=0), 3)

    def test_random_junk(self):
        inv = merge_sort.merge_sort(lst=[89, 76, 2, 4, 1, 5435, 0, 1, 129, 43, 34, 56, 82], inversions=0)
        self.assertEqual(inv, 37)
        self.assertEqual(insertion_sort.insertion_sort(lst=[89, 76, 2, 4, 1, 5435, 0, 1, 129, 43, 34, 56, 82],), [0, 1, 1, 2, 4, 34, 43, 56, 76, 82, 89, 129, 5435])

    def test_random_junk2_worst_case(self):
        lst = [5435, 129, 89, 82, 76, 56, 43, 34, 4, 3, 2, 1, 0]
        n = len(lst)
        inv = merge_sort.merge_sort(lst=lst, inversions=0)
        self.assertEqual(inv, n*(n-1)//2)

    def test_random_junk2_with_repeated_value_off_by_one(self):
        lst = [5435, 129, 89, 82, 76, 56, 43, 34, 4, 3, 1, 1, 0]
        n = len(lst)
        inv = merge_sort.merge_sort(lst=lst, inversions=0)
        self.assertEqual(inv, n*(n-1)//2 - 1)

if __name__ == '__main__':
    unittest.main()
