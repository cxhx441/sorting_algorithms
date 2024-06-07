import unittest
import timeit
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from quick_sort import quick_sort_in_place
from shell_sort import shell_sort
from merge_sort import merge_sort

class MyTests(unittest.TestCase):
    def setUp(self):
        # self.a = [5, 4, 3, 2, 1]
        # self.b = [0, 0, 0, 0, 0]
        # self.c = [1, 2, 3, 4, 5]
        # self.d = [-1, -2, -3, -4, -5]
        # self.e = [100, -2, 40, -800, 1]
        # self.f = [10, 100, 5, 200, 1]

        # self.a_ans = [1, 2, 3, 4, 5]
        # self.b_ans = [0, 0, 0, 0, 0]
        # self.c_ans = [1, 2, 3, 4, 5]
        # self.d_ans = [-5, -4, -3, -2, -1]
        # self.e_ans = [-800, -2, 1, 40, 100]
        # self.f_ans = [1, 5, 10, 100, 200]
        #
        x = 1000
        self.my_unsorted_lists = [
            [5, 4, 3, 2, 1]*x,
            [0, 0, 0, 0, 0]*x,
            [1, 2, 3, 4, 5]*x,
            [-1, -2, -3, -4, -5]*x,
            [100, -2, 40, -800, 1]*x,
            [10, 100, 5, 200, 1]*x
        ]

        self.python_sorted_lists = []
        for l in self.my_unsorted_lists:
            self.python_sorted_lists.append(l.copy())
        for l in self.python_sorted_lists:
            l.sort()


    # def test_python_sort(self):
    #     self.a.sort()
    #     self.b.sort()
    #     self.c.sort()
    #     self.d.sort()
    #     self.e.sort()
    #     self.f.sort()
    #     self.assertEqual(self.a_ans, self.a)
    #     self.assertEqual(self.b_ans, self.b)
    #     self.assertEqual(self.c_ans, self.c)
    #     self.assertEqual(self.d_ans, self.d)
    #     self.assertEqual(self.e_ans, self.e)
    #     self.assertEqual(self.f_ans, self.f)

    def test_insertion_sort(self):
        t0 = timeit.default_timer()
        for l in self.my_unsorted_lists:
            insertion_sort(l)
        print('insertion_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_bubble_sort(self):
        t0 = timeit.default_timer()
        for l in self.my_unsorted_lists:
            bubble_sort(l)
        print('bubble_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_selection_sort(self):
        t0 = timeit.default_timer()
        for l in self.my_unsorted_lists:
            selection_sort(l)
        print('selection_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_quick_sort(self):
        t0 = timeit.default_timer()
        self.my_unsorted_lists = [quick_sort(l) for l in self.my_unsorted_lists]
        print('quick_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_quick_sort_in_place(self):
        t0 = timeit.default_timer()
        self.my_unsorted_lists = [quick_sort_in_place(l) for l in self.my_unsorted_lists]
        print('quick_sort_inplace:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_shell_sort(self):
        t0 = timeit.default_timer()
        for l in self.my_unsorted_lists:
            shell_sort(l)
        print('shell_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

    def test_merge_sort(self):
        t0 = timeit.default_timer()
        for i, l in enumerate(self.my_unsorted_lists):
            self.my_unsorted_lists[i] = merge_sort(l)
        print('merge_sort:', (timeit.default_timer() - t0)*1000)

        for idx in range(len(self.my_unsorted_lists)):
            my_sorted = self.my_unsorted_lists[idx]
            python_sorted = self.python_sorted_lists[idx]
            self.assertEqual(my_sorted, python_sorted)

if __name__ == '__main__':
    unittest.main()
