import numpy as np

# creating array using numpy
arr = np.array([1,2,3,4,5,69,77,99,72,84,56])
print(arr)
print(type(arr))

print(arr.max())
print(arr.min())
print(arr.mean())
print("before sorting:", arr)
arr.sort()
print("after sorting :", arr)
print("after reverse sorting :", np.flip(arr))


 

