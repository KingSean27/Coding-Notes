# numpy is one of the key packages for data science
import numpy as np

# we can multiply numpy arrays together unlike lists
height = np.array([1.73, 1.68, 1.71])
weight = np.array([60.5, 70.2, 90.5])

BMI = weight / height ** 2
print(BMI)

# this works as numpy arrays contain only one type
# if you put multiple things together they will converted to the same type

# numpy arrays can add things together and filter values easily
print(BMI > 24 )
print(BMI[BMI > 24])
BMI = BMI + 10
print(BMI)
print(BMI.dtype)

