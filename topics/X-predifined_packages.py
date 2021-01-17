# numpy
# pip install numpy

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr.ndim)
print(arr.dtype)
print(arr.shape)

print(arr[1, 1:4])
print(arr[:, 2:4])


arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
x[0] = 6

print(arr)
print(x)

y = arr.view()
y[0] = 7

print(arr)
print(y)

print(x.base)
print(y.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(2, 3, 2)

print(new_arr)


arr = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = arr.reshape(-1)

print(new_arr)


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


x=np.random.randint(100, size=(5))

print(x)
print(np.sort(x))

x = np.random.randint(100, size=(3, 5))

print(x)
print(np.sort(x))