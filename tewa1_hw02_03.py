import numpy as np


# homework 2 assignment 3

# Task 1


def My10Up(arr):
    """

    write a function (My10Up) that takes as an input 2d numpy array (matrix) of
    numbers, calculates the number of elements that are bigger than 10 for each
    row. this function should return an array (Num10Up) that is the length of 
    the number of rows in the input. first write a solution with a for cycle, 
    where you initialize Num10Up with an array of zeros (equaling the number of
    rows). in fact the task can be solved without for cycle with a single line
    of code, try to find this solution as well.

    """
    zerolen = np.zeros(len(arr))

    for i in range(np.shape(arr)[0]):
        for l in range(np.shape(arr)[1]):
            if arr[i, l] > 10:
                zerolen[i] = zerolen[i] + 1
    return zerolen


arr = np.array([[1, 20, 6], [40, 5, 70], [55, 23, 12], [78, 11, 22]])

res = My10Up(arr)

print("Task 1: In this array\n\n", arr)
print("\nthe number of values over 10 are\n")
for i in range(len(res)):
    print(int(res[i]), "in row", i + 1)


### Task 2a: nested list comprehension


def my_10_up_nlc(arr):
    res = [len([i for i in row if i > 10]) for row in arr]
    return res


print("\nTask 2: Use a one-liner for the same procedure:")
print("\nThe nested list comprehension gives us: ", my_10_up_nlc(arr))

### Task 2b: list comprehension with conditional sum


def my_10_up_lcsum(arr):
    res = [sum(row > 10) for row in arr]
    return res


print("\nThe list comprehension with conditional sum gives us: ", my_10_up_lcsum(arr))
