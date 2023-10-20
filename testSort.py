import unittest
import random as rd

from sort import sort_dheap, sort_merge

def is_sorted(arr) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

class TestSortDheap(unittest.TestCase):
    def test_dheap_simple_exam(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        arr = sort_dheap(arr, 4)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9,10])
    
    def test_dheap_random_list(self):
        arr = []
        for i in range(10):
            arr.append(rd.randint(-1000, 1000))
        arr = sort_dheap(arr, 4)
        self.assertTrue(is_sorted(arr))

    def test_dheap_random_d(self):
        arr = [i for i in range(100)]
        d = rd.randint(2,10)
        arr = sort_dheap(arr, d)
        self.assertTrue(is_sorted(arr))

class TestSortMerge(unittest.TestCase):
    def test_merge_simple_exam(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        arr = sort_merge(arr, 0, len(arr) - 1, 3)
        self.assertEqual(arr, [1,2,3,4,5,6,7,8,9,10])

    def test_merge_random_list(self):
        arr = []
        for i in range(10):
            arr.append(rd.randint(-1000, 1000))
        arr = sort_merge(arr, 0, len(arr) - 1, 3)
        self.assertTrue(is_sorted(arr))

    def test_merge_random_k(self):
        arr = [i for i in range(100)]
        k = rd.randint(2,10)
        arr = sort_merge(arr, 0, len(arr) - 1, k)
        self.assertTrue(is_sorted(arr))



if __name__ == '__main__':
    unittest.main()