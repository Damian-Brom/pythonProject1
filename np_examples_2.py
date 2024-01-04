import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
column_0_values = arr[:,0]
transposed_arr = arr.T
reshaped_arr = arr.reshape((3,2))

print(f"arr's shape is", arr.shape)
print(f"arr =\n", arr)

print(f"\narr's first column is\n", column_0_values)
print(f"\narr transposed =\n", transposed_arr)
print(f"\narr reshaped to a 3x2 matrix =\n", reshaped_arr)

arr1 = np.zeros((3,4))
arr2 = np.ones((4,1))
# @ is a matrix multiplication operator. It'll be useful later.
arr3 = arr1 @ arr2

print(f"\narr1's shape is", arr1.shape)
print(f"arr2's shape is", arr2.shape)
print(f"arr3's shape is", arr3.shape)

print(f"\narr1 =\n", arr1)
print(f"\narr2 =\n", arr2)
print(f"\narr1 @ arr2 =\n", arr3)
