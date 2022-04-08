import numpy as np

# numpy can have more than 1 dimensional arrays
height = np.array([1.73, 1.68, 1.71])
print("The array height, has the shape:", height.shape)

# can create a 2D array from a list of lists
np_2d = np.array([[1.7, 1.6, 1.8, 2], [65, 59, 88, 93]])
print("The array np_2d has the following values:", np_2d)
print("And the attributes, type:", type(np_2d))
print("Dtype:", np_2d.dtype)
print("Shape:", np_2d.shape)

# we can index using the row then subset notation
# first number is rows, then columns
print("The 0, 2 element is:", np_2d[0][2])
print("The 1, 3 element is:", np_2d[1,3])