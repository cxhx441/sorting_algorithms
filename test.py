import unittest
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

class MyTests(unittest.TestCase):
    def setUp(self):
        self.a = [5, 4, 3, 2, 1]
        self.b = [0, 0, 0, 0, 0]
        self.c = [1, 2, 3, 4, 5]
        self.d = [-1, -2, -3, -4, -5]
        self.e = [100, -2, 40, -800, 1]

        self.a_ans = [1, 2, 3, 4, 5]
        self.b_ans = [0, 0, 0, 0, 0]
        self.c_ans = [1, 2, 3, 4, 5]
        self.d_ans = [-5, -4, -3, -2, -1]
        self.e_ans = [-800, -2, 1, 40, 100]

    def test_python_sort(self):
        self.a.sort()
        self.b.sort()
        self.c.sort()
        self.d.sort()
        self.e.sort()
        self.assertEqual(self.a_ans, self.a)
        self.assertEqual(self.b_ans, self.b)
        self.assertEqual(self.c_ans, self.c)
        self.assertEqual(self.d_ans, self.d)
        self.assertEqual(self.e_ans, self.e)

    def test_insertion_sort(self):
        insertion_sort(self.a)
        insertion_sort(self.b)
        insertion_sort(self.c)
        insertion_sort(self.d)
        insertion_sort(self.e)
        self.assertEqual(self.a_ans, self.a)
        self.assertEqual(self.b_ans, self.b)
        self.assertEqual(self.c_ans, self.c)
        self.assertEqual(self.d_ans, self.d)
        self.assertEqual(self.e_ans, self.e)

    def test_bubble_sort(self):
        bubble_sort(self.a)
        bubble_sort(self.b)
        bubble_sort(self.c)
        bubble_sort(self.d)
        bubble_sort(self.e)
        self.assertEqual(self.a_ans, self.a)
        self.assertEqual(self.b_ans, self.b)
        self.assertEqual(self.c_ans, self.c)
        self.assertEqual(self.d_ans, self.d)
        self.assertEqual(self.e_ans, self.e)

    def test_selection_sort(self):
        selection_sort(self.a)
        selection_sort(self.b)
        selection_sort(self.c)
        selection_sort(self.d)
        selection_sort(self.e)
        self.assertEqual(self.a_ans, self.a)
        self.assertEqual(self.b_ans, self.b)
        self.assertEqual(self.c_ans, self.c)
        self.assertEqual(self.d_ans, self.d)
        self.assertEqual(self.e_ans, self.e)

    def test_quick_sort(self):
        self.a = quick_sort(self.a)
        self.b = quick_sort(self.b)
        self.c = quick_sort(self.c)
        self.d = quick_sort(self.d)
        self.e = quick_sort(self.e)
        self.assertEqual(self.a_ans, self.a)
        self.assertEqual(self.b_ans, self.b)
        self.assertEqual(self.c_ans, self.c)
        self.assertEqual(self.d_ans, self.d)
        self.assertEqual(self.e_ans, self.e)
