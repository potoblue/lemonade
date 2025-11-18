import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)

# from numpy.random import default_rng

# rng = default_rng(seed = 42)

# print(rng.integers(1,10,size=5))
# print(rng.random(3))
# print(rng.normal(0,1,size = (2,2)))
# print(rng.uniform(5,10,size=3))

# arr  = np.array([10,20,30,40,50])
# print(arr[1:4])
# print(arr[:3])
# print(arr[2:])
# print(arr[::2])

# arr2 = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])

# print(arr2[:2,1:])

# arr = np.arange(1,13).reshape(3,4)
# print(arr)
# view_arr = arr.view()
# view_arr[-1:,:] = -1
# print(view_arr)

# arr = np.random.randint(1,99,(10,10))
# print(arr)
# # if i in range(0,size(arr)) : 
# #     pass

# print(arr[::2,2])

# arr2d = np.array([[1,2,3],
#                   [4,5,6]])

# arr1d = np.array([10,20,30])

# print(arr2d + arr1d)

# arr1 = np.array([1,2,3,4])
# arr11 = np.array([3])
# print(arr1+arr11)

# arr2 = np.array([[5,10],
#                  [15,20]])
# arr22 = np.array([-1])
# print(arr2*arr22)

# arr3 = np.array([2,4,6])
# arr33 = np.array([1,2,3])
# print(arr3*arr33)
# print(arr3/arr33)

# arr = np.array([[10,20],
#                 [30,40],
#                 [50,60]])

# print(np.mean(arr, axis = 0))
# print(np.mean(arr, axis = 1))

#------------------
# arr1 = np.arange(1,10).reshape(3,3)
# print(arr1)
# arr11 = np.full((3,2),2)
# print(arr11)
# print(arr1 @ arr11)

# arrI = np.eye(4)
# print(arrI)
# arrM = np.random.randint(1,9,(4,4))
# print(arrM)
# arrSum = np.matmul(arrI, arrM)
# print(arrSum)
# print(np.where(arrSum == arrM,"True","False"))

arr = np.array([[10,20],[30,40],[50,60]])

arrRav = arr.ravel()
arrFlat = arr.flatten()
print(arrRav)
print(arrFlat)

arr[0,0] = 999
print(arrRav)
print(arrFlat)

img = np.random.rand(32,32)
img1 = np.expand_dims(img, axis=1)
print(img)
print(img1)

