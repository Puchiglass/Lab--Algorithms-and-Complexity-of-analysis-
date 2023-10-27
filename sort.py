import time
import random as rd


def k_merge_sort(arr, k):
    length = len(arr)
    if length <= 1: return arr

    step = length // k if length // k > 0 else 1

    divide_arr = [arr[i : i+step] for i in range(0, length, step)]
    sorted_arr = [k_merge_sort(a, k) for a in divide_arr]
    return merge(sorted_arr)

def merge(sorted_arr):
    if len(sorted_arr) == 1:
        return sorted_arr[0]
    mid = len(sorted_arr) // 2
    left = merge(sorted_arr[:mid])
    right = merge(sorted_arr[mid:])
    return merge_2_arr(left, right)

def merge_2_arr(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res
    

def heapify(arr, d, length, index):
    largest = index
    for child in range(d * index + 1, min(length, d * index + d + 1)):
        if arr[largest] < arr[child]:
            largest = child

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, d, length, largest)

def d_heap_sort(arr, d=3):
    length = len(arr)
    
    # Создаем кучу
    for i in range((length + 1) // d - 1, -1, -1):
        heapify(arr, d, length, i)

    # Сортируем кучу
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, d, i, 0)


def main():
    arr1 = list()
    for i in range(1_000_000):
        arr1.append(rd.randint(1,100_000))
    arr2 = arr1[:]
    arr3 = arr1[:]

    start = time.time()
    arr1.sort()
    end = time.time()
    print(f'.sort() = {end - start}')
    
    start = time.time()
    d_heap_sort(arr2, 3)
    end = time.time()
    print(f'd_heap_sort() = {end - start}')

    start = time.time()
    k_merge_sort(arr3, 4)
    end = time.time()
    print(f'k_merge_sort() = {end - start}')
    

if __name__ == "__main__":
    main()