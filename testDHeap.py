import unittest

from DHeap import Dheap


class TestDHeap(unittest.TestCase):
    def test_simple_heap(self):
        heap2 = Dheap(2, [4, 6, 9, 2, 3, 10, 11]).get_heap()
        heap3 = Dheap(3, [10, 2, 4, 5, 7, 9]).get_heap()
        heap4 = Dheap(4, [56, 19, 2, 90, 5, 23, 1, 37, 89, 54, 12]).get_heap()
        self.assertEqual(heap3, [10, 9, 5, 4, 2, 7])
        self.assertEqual(heap2, [11, 10, 6, 2, 9, 3, 4])
        self.assertEqual(heap4, [90, 89, 56, 37, 1, 12, 5, 23, 2, 19, 54])

    def test_len(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap_empty = Dheap(3, [])
        self.assertEqual(len(heap3), 6)
        self.assertEqual(len(heap_empty), 0)

    def test_get_heap(self):
        heap3 = Dheap(3, [10, 2, 4, 5, 7, 9]).get_heap()
        self.assertEqual(heap3, [10, 9, 5, 4, 2, 7])

    def test_add(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap3.add(11)
        self.assertEqual(heap3.get_heap(), [11, 10, 4, 5, 2, 7, 9])
        heap3.add(-1)
        self.assertEqual(heap3.get_heap(), [11, 10, 4, 5, 2, 7, 9, -1])
        heap3.add(10)
        self.assertEqual(heap3.get_heap(), [11, 10, 10, 5, 2, 7, 9, -1, 4])

    def test_delete(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap3.delete(0)
        self.assertEqual(heap3.get_heap(), [9, 7, 4, 5, 2])
        heap3.delete(100)
        self.assertEqual(heap3.get_heap(), [9, 7, 4, 5, 2])
        heap3.delete(-1)
        self.assertEqual(heap3.get_heap(), [9, 7, 4, 5, 2])

    def test_pop(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        x = heap3.pop()
        self.assertEqual(x, 7)
        heap_empty = Dheap(3, [])
        x = heap_empty.pop()
        self.assertEqual(x, None)

    def test_is_empty(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap_empty = Dheap(3, [])
        self.assertEqual(heap3.is_empty(), False)
        self.assertEqual(heap_empty.is_empty(), True)

    def test_get_max_element(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap_empty = Dheap(3, [])
        self.assertEqual(heap3.get_max_element(), 10)
        self.assertEqual(heap_empty.get_max_element(), None)

    def test_get_max_child_index(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        self.assertEqual(heap3._get_max_child_index(0), 1)
        self.assertEqual(heap3._get_max_child_index(1), 5)

    def test_get_parent_index(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        self.assertEqual(heap3._get_parent_index(5), 1)
        self.assertEqual(heap3._get_parent_index(0), -1)

    def test_swap(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap3.swap(0,1)
        self.assertEqual(heap3.get_heap(), [9, 10, 4, 5, 2, 7])

    def test_sift_down(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap3.swap(0, len(heap3) - 1)
        heap3.sift_down(0, len(heap3) - 2)
        self.assertEqual(heap3.get_heap(), [9, 7, 4, 5, 2, 10])

    def test_custom_max_child_index(self):
        heap3 = Dheap(3, [10, 9, 5, 4, 2, 7])
        heap3.swap(0, len(heap3) - 1)
        x = heap3._custom_max_child_index(1, len(heap3) - 1)
        self.assertEqual(x, 4)

        
