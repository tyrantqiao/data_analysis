import numpy as np
import timeit

timer = timeit.Timer()
arr = np.arange(1e7)
l = arr.tolist()


def multiply(arr, number):
    for i, item in enumerate(arr):
        arr[i] = item * number;
    return arr



print(timeit.timeit(l * 1.1))
