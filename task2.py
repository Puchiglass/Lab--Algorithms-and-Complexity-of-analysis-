import time
import random as rd
import matplotlib.pyplot as plt

from sort import k_merge_sort, d_heap_sort


q, w = 0, 1_000_000
low_n, high_n, step = 1, 500_000 + 1, 1_000

x_ax = []

arr1 = []
index = 0
print("work start")
k = 0
for n in range(low_n, high_n, step):
    arr1.append([])
    for i in range(n):
        arr1[index].append(rd.randint(q,w))
    index += 1
    if k % 50 == 0:
        print(f"Work = {k}")
    k += 1
    x_ax.append(n)
print("Created arrays for sorting\nStart sort arrays")

heap_rand_times = []
k = 0
for a in arr1:
    start = time.time()
    d_heap_sort(a, 3)
    end = time.time()
    heap_rand_times.append(end-start)
    if k % 50 == 0:
        print(f"Work = {k}")
    k += 1

plt.plot(x_ax, heap_rand_times, 'o', markersize = 0.2)
plt.show()