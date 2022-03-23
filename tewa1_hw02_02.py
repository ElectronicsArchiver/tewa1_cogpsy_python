import numpy as np
import matplotlib.pyplot as plt

# homework 2 assignment 2

# 1. make a 1-dimensional array of 50 normally distributed random values, with mean=10 and
# SD=4

# 2. make a figures with two subplots, on subplot 1 should be a histogram of
# the result on subplot 2 should be a scatter plot containing the values in
# order on the X axis, and the actual values on the Y  (plt.subplot)

# 3. calculate the proporiton of these numbers that are smaller than 7

# 4. calculate the proportion of that is smaller 5 or bigger than 14

# 5. make a new scatter plot that has different color for these extreme values
# (red), that you found in 4. (you can use a for cycle to make a scatter for
# each dot individually)


# 2.1
arr_norm = np.random.normal(10, 4, 50)
print(
    "Task 1: 1-dimensional Array with 50 normally distributed random values (M=10, SD=4):\n",
    arr_norm,
)


# 2.2
plt.figure(figsize=(16, 6))
plt.subplot(121)
plt.hist(arr_norm, bins=10)
plt.title("Histogram")
plt.suptitle("Task 2: A figure with 2 subplots")
plt.subplot(122)
plt.scatter(range(len(arr_norm)), arr_norm)
plt.title("Scatter plot")
plt.show()
print("\nTask 2: See plot")

# 2.3
proportion_smaller_7 = len(arr_norm[arr_norm > 7]) / len(arr_norm)
print(
    "\nTask 3: In the same array the proportion of numbers that are smaller than 7 is",
    proportion_smaller_7,
)
# alternative solution
# le = np.shape(arr_norm)
# pr1 = np.sum(arr_norm > 7) / le
# print(pr1[0])


# 2.4
proportion_sm5_gr14 = np.sum((arr_norm < 5) | (arr_norm > 14)) / len(arr_norm)
print(
    "\nTask 4: While the proportion of numbers that are smaller than 5 or greater than 14 is",
    proportion_sm5_gr14,
)

# 2.5
arr_in = []
arr_out = []
for i in arr_norm:
    if i < 5 or i > 14:
        arr_out.append(i)
    else:
        arr_in.append(i)

plt.figure(figsize=(8, 6))
plt.title("Task 5: Scatter plot showing the extreme values in red")
plt.scatter(range(len(arr_out)), arr_out, c="r")
plt.scatter(range(len(arr_in)), arr_in, c="b")
plt.show()
print("\nTask 5: See plot")
