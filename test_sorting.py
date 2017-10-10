import unittest
import sorting


class MergeSortTests(unittest.TestCase):
    def test_best_case_sorted_list_no_inversions(self):
        test_list = [1, 2, 3, 4, 5, 6]
        list_answer = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting.merge_sort(lst=[1, 2, 3, 4, 5, 6], inversions=0), (list_answer, 0))

    def test_worst_case_reverse_list_nlogn_inversions(self):
        test_list = [6, 5, 4, 3, 2, 1]
        list_answer = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting.merge_sort(lst=test_list, inversions=0), (list_answer, 15))

    def test_worst_case_reverse_list_nlogn_inversions2(self):
        test_list = [6, 5, 4, 3, 2, 1]
        list_answer = [1, 2, 3, 4, 5, 6]
        n = len(test_list)
        self.assertEqual(sorting.merge_sort(lst=test_list, inversions=0), (list_answer, int(n*(n-1)/2)))

    def test_all_split_case(self):
        test_list = [1, 3, 5, 2, 4, 6]
        list_answer = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting.merge_sort(lst=test_list, inversions=0), (list_answer, 3))

    def test_random_junk(self):
        test_list = [89, 76, 2, 4, 1, 5435, 0, 1, 129, 43, 34, 56, 82]
        list_answer = [0, 1, 1, 2, 4, 34, 43, 56, 76, 82, 89, 129, 5435]
        inv = sorting.merge_sort(lst=test_list, inversions=0)
        self.assertEqual(inv, (list_answer, 37))

    def test_random_junk2_worst_case(self):
        test_list = [5435, 129, 89, 82, 76, 56, 43, 34, 4, 3, 2, 1, 0]
        list_answer = [0, 1, 2, 3, 4, 34, 43, 56, 76, 82, 89, 129, 5435]
        n = len(test_list)
        inv = sorting.merge_sort(lst=test_list, inversions=0)
        self.assertEqual(inv, (list_answer, n*(n-1)//2))

    def test_random_junk2_with_repeated_value_off_by_one(self):
        test_list = [5435, 129, 89, 82, 76, 56, 43, 34, 4, 3, 1, 1, 0]
        list_answer = [0, 1, 1, 3, 4, 34, 43, 56, 76, 82, 89, 129, 5435]
        n = len(test_list)
        inv = sorting.merge_sort(lst=test_list, inversions=0)
        self.assertEqual(inv, (list_answer, n*(n-1)//2 - 1))


class QuickSortTest(unittest.TestCase):
    pass


class InsertionSortTests(unittest.TestCase):
    def test_sorted_list(self):
        test_list = [1, 2, 3, 4, 5, 6]
        list_answer = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting.insertion_sort(lst=test_list), list_answer)

    def test_reverse_list(self):
        test_list = [6, 5, 4, 3, 2, 1]
        list_answer = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorting.insertion_sort(lst=test_list), list_answer)

    def test_random_junk(self):
        test_list = [89, 76, 2, 4, 1, 5435, 0, 1, 129, 43, 34, 56, 82]
        list_answer = [0, 1, 1, 2, 4, 34, 43, 56, 76, 82, 89, 129, 5435]
        self.assertEqual(sorting.insertion_sort(lst=test_list), list_answer)




class BubbleSortTests(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
