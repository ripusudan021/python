import numpy as np

#creating Numpy Arrays

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

#one dimensional Array
print(list1)
arr_list1 = np.array(list1)
print(arr_list1)
print(type(arr_list1))
print(arr_list1.ndim)

#two dimensional Array

arr_list1_2 = np.array([list1,list2])
print(arr_list1_2)
print(arr_list1_2.ndim)

#three dimensional Array

arr_list1_2_3 = np.array([[list1,list2,list3]])
print(arr_list1_2_3)
print(arr_list1_2_3.ndim)

#Array attributes

#1d array 
print("1D Array Attribute")
print(arr_list1.ndim)
print(arr_list1.shape)
print(arr_list1.size)
print(arr_list1.dtype)
print(arr_list1.itemsize)

#2d array 
print("2D Array Attribute")
print(arr_list1_2.ndim)
print(arr_list1_2.shape)
print(arr_list1_2.size)
print(arr_list1_2.dtype)
print(arr_list1_2.itemsize)

#3d array 
print("3D Array Attribute")
print(arr_list1_2_3.ndim)
print(arr_list1_2_3.shape)
print(arr_list1_2_3.size)
print(arr_list1_2_3.dtype)
print(arr_list1_2_3.itemsize)

# Array initialization methods

#zero array 
zero_arr = np.zeros((2,3,))
print(zero_arr)

#one array 
one_arr = np.ones((2,3,))
print(one_arr)

#full array 
full_arr = np.full((2,3,),7)
print(full_arr)

# identity Matrix

id_arr = np.eye(3)
print(id_arr)


# 2d Array Slicing

arr = np.array([[3, 7, 7],
                [2, 9, 2]])

print(arr)

print(arr[0:2:1, 0:2:1])

#mathematical operation
arr1 = np.array(list1)
arr2 = np.array(list2)
print(arr1)
print(arr2)
print(arr1+10)
print(np.add(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.dot(arr1,arr2))
print(np.array_equal(arr1,arr2))
