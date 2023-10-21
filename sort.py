import random as rd  # для примера

from DHeap import Dheap


def sort_dheap(arr, d) -> list:
    heap = Dheap(d, arr)
    n = len(heap) - 1
    while n > 0:
        heap.swap(0, n)
        heap.sift_down(0, n)
        n -= 1
    # arr = [None] * len(heap)
    # for i in range(len(heap)):
    #     arr[i] = heap.get_heap()[i]
    arr = heap.get_heap()
    return arr


def sort_merge(arr, left, right, k) -> list:
    """
    arr - список
    left - крайний левый индекс. В начале 0
    right - крайний правый индекс. В начале len(arr) - 1
    k - кратность сортировки. Сортировка k-слиянием
    """

    def merge(arr, left, middle, right):
        """
        arr - список
        left - первый индекс первого подмассива
        middle - последний индекс первого подмассива
        right - последний индекс второго подмассива
        """
        tmp_arr = [None] * (right - left + 1)
        i = left
        j = middle + 1
        index = 0
        while i <= middle and j <= right:
            if arr[i] <= arr[j]:
                tmp_arr[index] = arr[i]
                i += 1
            else:
                tmp_arr[index] = arr[j]
                j += 1
            index += 1

        if i <= middle:
            while i <= middle:
                tmp_arr[index] = arr[i]
                i += 1
                index += 1
        elif j <= right:
            while j <= right:
                tmp_arr[index] = arr[j]
                j += 1
                index += 1

        index = left
        for num in tmp_arr:
            arr[index] = num
            index += 1

    if right - left < k:  # Когда сортируемый список меньше k
        tmp_arr = arr[left: right+1]
        tmp_arr.sort()
        index = left
        for num in tmp_arr:
            arr[index] = num
            index += 1
        return arr

    step = (right - left + 1) // k  # кол-во шагов для деления списка
    for i in range(step):  # сортировка подмассивов
        sort_merge(arr, left + k*i, left + k*(i+1) - 1, k)
    else:
        if (right - left + 1) % k != 0:
            sort_merge(arr, left + k*step, right, k)

    for i in range(step - 1):  # слияние подмассивов
        merge(arr, left, left + k*(i+1) - 1, left + k*(i+2) - 1)
    else:
        if (right - left + 1) % k != 0:
            merge(arr, left, left + k*step-1, right)

    return arr

def main():
    # def random_arr_dheap():
    #     arr = []
    #     for i in range(10):
    #         arr.append(rd.randint(1, 10))
    #     return sort_dheap(arr, 3)
    # for i in range(5):
    #     print(random_arr_dheap())
    
    # print("=" * 40)

    # def random_arr_merge():
    #     arr = []
    #     for i in range(10):
    #         arr.append(rd.randint(1, 10))
    #     sort_merge(arr, 0, len(arr)-1, 4)
    #     return arr
    # for i in range(5):
    #     print(random_arr_merge())
    arr = [i for i in range(1, 10)]
    arr[::-1]
    arr = sort_dheap(arr, 3)
    print(arr)


if __name__ == "__main__":
    main()