class Dheap():
    def __init__(self, d, arr):
        self.d = d
        self.heap = list()
        while (arr != None) and (len(arr) != 0):
            self.add(arr.pop())

    def __len__(self) -> int: 
        """ len() """
        return len(self.heap)
    
    def get_heap(self) -> list:
        """ Список d-кучи """
        return self.heap

    def add(self, element) -> None:
        """ Добавление элемента """
        self.heap.append(element)
        self._swim_up(len(self) - 1)

    def delete(self, index) -> None:
        """ Удаление элемента """
        if (index > len(self) or index < 0): return

        self.swap(index, len(self) - 1)
        self.heap.pop()
        if (index != 0 and self.heap[index] > self.heap[self._get_parent_index]):
            self._swim_up(index)
        else:
            self._swim_down(index)

    def pop(self):
        """ Удалить и вернуть последний элемент """
        if self.is_empty():
            return None
        return self.heap.pop()

    def _swim_up(self, index) -> None:
        """ Всплытие элемента наверх """
        parent_index = self._get_parent_index(index)
        if (parent_index >= 0) and (self.heap[index] > self.heap[parent_index]):
            self.swap(index, parent_index)
            self._swim_up(parent_index) 

    def _swim_down(self, index) -> None:
        """ Погружение элемента """
        max_child_index = self._get_max_child_index(index)
        if (max_child_index > 0) and (self.heap[index] < self.heap[max_child_index]):
            self.swap(index, max_child_index)
            self._swim_down(max_child_index)

    def is_empty(self) -> bool:
        """ Проверка на пустоту кучи """
        return len(self) == 0

    def get_max_element(self):
        """ Получить самый большой элемент """
        if self.is_empty():
            return None
        return self.heap[0]
    
    def _get_max_child_index(self, parent_index):
        """ Самый большой ребенок """
        first_child_index = parent_index * self.d + 1
        if first_child_index >= len(self):
            return -1
        
        count_of_child = len(self) - first_child_index
        if count_of_child > self.d:
            count_of_child = self.d

        max_child_index = first_child_index
        for i in range(first_child_index, first_child_index + count_of_child):
            if self.heap[i] > self.heap[max_child_index]:
                max_child_index = i
        return max_child_index

    def _get_parent_index(self, child_index) -> int:
        """ Индекс родителя """
        if child_index - 1 >= 0:
            return (child_index - 1) // self.d
        else:
            return -1

    def swap(self, index1, index2) -> None:
        """ Поменять местами элементы """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 

    def sift_down(self, index, length):
        """ Просеивание для алгоритмы сортировки """
        max_child_index = self._custom_max_child_index(index, length)
        if (max_child_index > 0) and (self.heap[index] < self.heap[max_child_index]):
            self.swap(index, max_child_index)
            self.sift_down(max_child_index, length)

    def _custom_max_child_index(self, parent_index, length):
        """ Самый большой ребенок в пределах неотсортированной кучи"""
        first_child_index = parent_index * self.d + 1
        if first_child_index >= length:
            return -1
        
        count_of_child = length - first_child_index
        if count_of_child > self.d:
            count_of_child = self.d

        max_child_index = first_child_index
        for i in range(first_child_index, first_child_index + count_of_child):
            if self.heap[i] > self.heap[max_child_index]:
                max_child_index = i
        return max_child_index