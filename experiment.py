import re
import time
import random as rd

from sort import sort_dheap, sort_merge


def main():
    with open("experiment.txt", "r", encoding="UTF-8") as file_in:
        lines = file_in.read()
    match = re.findall(r"\d+", lines)
    length = int(match[0])
    upper_limit = int(match[1])
    lower_limit = int(match[2])
    filling = int(match[3])
    print(f"Сортировка {length} элементов")
    print(f"Нижняя граница чисел {lower_limit}, Верхняя граница чисел {upper_limit}")
    
    arr1 = [None] * length
    arr2 = [None] * length
    if filling == 1:
        for i in range(length):
            arr1[i] = rd.randint(lower_limit, upper_limit)
        arr2 = arr1[:]
        print("Сортировка псевдослучайных чисел")
    elif filling == 2:
        for i in range(length):
            arr1[i] = rd.randint(lower_limit, upper_limit)
        arr1.sort()
        arr2 = arr1[:]
        print("Сортировка чисел стоящий по неубыванию")
    elif filling == 3:
        for i in range(length):
            arr1[i] = rd.randint(lower_limit, upper_limit)
        arr1.sort()
        arr1 = arr1[::-1]
        arr2 = arr1[:]
        print("Сортировка чисел стоящий по невозрастанию")
    
    start_time = time.time()
    arr1 = sort_dheap(arr1, 3)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"\nВремя сортировки 3-кучей = {runtime:.4f} с")
    
    start_time = time.time()
    arr2 = sort_merge(arr2, 0, length - 1, 4)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Время сортировки 4-слиянием = {runtime:.4f} с")

    start_time = time.time()
    arr1.sort()
    end_time = time.time()
    runtime = end_time - start_time
    print(f"\nВремя сортировки sort() = {runtime:.4f} с")


if __name__ == "__main__":
    main()