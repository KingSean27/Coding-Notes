import numpy as np

# numpy has lots of inbuilt mathematical functions such as mean and median
np_2d = np.array([[1.7, 1.6, 1.8, 2], [65, 59, 88, 93]])
print("Mean:", np.mean(np_2d[1]))
print("Median:", np.median(np_2d[0]))

# other common functions include correlation coefficient, np.corrcoef and standard deviation np.std
# as there is only one data type in the array these calculations are much quicker than they are in base python
