import numpy as np


def n_greater_zero_less_ten(arr):
    """
    homework 2 assignment 1:
    write a function that takes as input a 1-dimensional numpy array and
    calculates the number of elements that are bigger than 0 but smaller than
    10.
    """

    arr_tmp = []
    for i in arr:
        if i > 0 and i < 10:
            arr_tmp.append(i)
    return len(arr_tmp)


arr = np.array([1, 2, 3, -5, 222, 12, 8, 5, 7, 6, 5, 4, -9, 8])

print(
    n_greater_zero_less_ten(arr),
    "numbers in the following array are greater than 0 and smaller than 10:\n",
    arr,
)
