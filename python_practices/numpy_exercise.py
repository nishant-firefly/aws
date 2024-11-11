# Minimum requirement for Data Sciences. # Numpy stack overflow second rank, professional devloper 
# Panda and tensor flow is based on numpy 
import numpy as np 
print("####  Data Types, Assignment and Casting.")
# Same as python e.g. a = [1,2,3,], a[1], a [1:4] a[-1]
# they work same written in c, optimized for linear algebra 
a = np.array([1,2,3,4,5])
np.array(a)
#print(a) # [1 2 3 4 5]
#print(type(a)) # <class 'numpy.ndarray'>
# print(a[1]) # 2 
# print(a[1:]) # [2 3 4 5]
# print(a[:-2]) # [1 2 3]
# a[2]=10
# print(a) # [ 1  2 10  4  5]
a_mul = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#print(a_mul) # [[ 1  2  3  4]\n [ 5  6  7  8]\n [ 9 10 11 12]]
"""Note: If try to have less or more elements after 1,2,3 
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.
"""
#print(a_mul[0]) # [1 2 4]
#print(a_mul.shape) # (3, 4)
a_mul_arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12],],[[13,14,15,16],[17,18,19,20],[21,22,23,24],]])
# print(a_mul_arr) #[[[ 1  2  3  4]\n [ 5  6  7  8]\n [ 9 10 11 12]]\n \n [[13 14 15 16]\n [17 18 19 20]\n [21 22 23 24]]]
# print(a_mul_arr.shape) # (2, 3, 4)
#print(a_mul_arr.ndim) # 3 # As it is 3 dimensional array
#print(a_mul_arr.size) # 24 # 2*3*4
#print(a_mul_arr.dtype) # int64 # As it is 3 dimensional array
# Note as it is written in c and why it is optimized it always have static type 
a_mul_arr[0][0][0]="22"
#print(a_mul_arr.dtype) # int64 # Still same as "22" can be casted
# a_mul_arr[0][0][0]="2.2" # ValueError: invalid literal for int() with base 10: '2.2'
a_mul_arr[0][0][0]=2.2
#print(a_mul_arr.dtype) # int64 # 2.2 is converted *One time casting only to set that is why 2.2. fine and not "2.3"* ,Once type assigned durining initialization can not be changed. 
#a_mul_arr[0][0][1]="Str Val"  # ValueError: invalid literal for int() with base 10: '2.2'
cast_arr_at_init=np.array([1,"2.2",3,4])
#print(cast_arr_at_init.dtype) # <U21 ## Not put any brain for catsing if giving string it is a string only 
cast_arr_at_init_obj=np.array([{"name":"Many"},"2.2",3,4])
#print(cast_arr_at_init_obj.dtype) # object ## Obvious
#print(cast_arr_at_init_obj[0], type(cast_arr_at_init_obj[0])) # {'name': 'Many'} <class 'dict'>
# print("## EXplicitly mention Dtype")
a = np.array([1.1,"2",3] , dtype=np.int32) # int16 int32 etc. all exists.
# print(a.dtype) #int32 "1.1" as string will be value error
a = np.array([1.1,"2","3.2"] , dtype=np.float16) # int16 int32 etc. all exists.
#print(a.dtype) # float16
a = np.array([1,2,3,],dtype="<U4") 
# print(a.dtype) # <U4
dtypes_doc=""" Basic Data Types in Numpy
1. Integer Types
np.int8: 8-bit signed integer (-128 to 127)
np.int16: 16-bit signed integer (-32,768 to 32,767)
np.int32: 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
np.int64: 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
Corresponding unsigned integer types are also available (e.g., np.uint8, np.uint16, etc.).

2. Floating-Point Types
np.float16: Half precision floating point
np.float32: Single precision floating point
np.float64: Double precision floating point (default for floats in NumPy)
3. Complex Types
np.complex64: Complex number represented by two 32-bit floats (real and imaginary parts)
np.complex128: Complex number represented by two 64-bit floats (real and imaginary parts)
4. Boolean Type
np.bool_: Boolean values (True or False)
5. String and Unicode Types
np.bytes_: strings
np.unicode_: Fixed-length Unicode strings
6. Object Type
np.object_: Generic object type that can hold any Python object
7. Datetime and Timedelta Types
np.datetime64: Dates and times (e.g., np.datetime64('2023-01-01'))
np.timedelta64: Differences between dates and times
"""
#print(dtypes_doc)
bool_array = np.array([True, False, True, True], dtype=np.bool_)
# print(bool_array) # [ True False  True  True]
string_array = np.array(['hello', 'world'], dtype=np.bytes_)
#print(string_array)
#print(string_array.dtype)  # dtype will show '|S5' (5-character ASCII string)
unicode_array = np.array(['hello', 'world', '😊'], dtype='U5')
#print(unicode_array)
#print(unicode_array.dtype)  # dtype will show '<U5' (5-character Unicode string)

print("For every elelement either object, inefficient or one data type only, depends on type of assignment or explicit mention dtype")
print("Learnt about np.array, shape=>(2,3,4) | dtype, ndim=>3 |  size=>24  np.float16-32 np.int 16-32, np.datetime64, np.timedelta64, np.bool_, Object, np.string_ is deprecated in 2.0 and bytes_, U1, U4 ,")

#print("### Arrays with default Value")
a = np.full((2,3,4),10)
# print(a)
# [[[10 10 10 10]\n [10 10 10 10]\n [10 10 10 10]]\n [[10 10 10 10]\n [10 10 10 10]\n [10 10 10 10]]]
#a = np.full((2,3,4,5,6,7),10)
#print(a) # a = np.full((2,3,4),10)\n [10 10 10 ... 10 10 10]\n ......
a=np.zeros((2,3))
# print(a)# [0 0] [0 0]
a=np.ones((2,3))
# print(a) # [[1 1 1]\n [1 1 1]...]
a=np.empty((2,4))
# print(a)#[[0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000]\n [0.00000000e+000 5.25685847e-321 0.00000000e+000 1.11253693e-308]]
#arange::  start: Starting *value*(not index) of the sequence (inclusive). | stop: End value of the sequence (exclusive) | step: The interval between values.
#print(np.arange(1,10,1)) # [1 2 3 4 5 6 7 8 9]
#linspace::start: Starting *value*(not index) of the sequence (inclusive). | stop: End value of the sequence (---------) | num: The number of values to geenrate.
#print(np.linspace(2, 10, 5)) # [ 2.  4.  6.  8. 10.]

#print(np.isnan(np.nan)) # True -- nan 
#print(np.isnan(np.sqrt(-1))) # True -- nan 

#print(np.isinf(np.inf)) # True -- inf, /0 dont through excepion 
# print(np.isinf(1/0)) # Zero Division Array

print("Learnt about full => (shape,vale)  | zeros (shape) | ones(shape) | empty(shape) | arange, linspace, inf, nan, isinf, isnan")
print("## Mathematical Operations")

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
a1=np.array(l1)
a2=np.array(l2)
#print(l1*5) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#print(a1*5) # [ 5 10 15 20 25]
#print(a1+5) # [ 6  7  8  9 10]
#print(l1+l2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#print(a1+a2) # [ 7  9 11 13  5]
#print(a1/a2) # [ 7  9 11 13  5] # [0.16666667 0.28571429 0.375      0.44444444        inf] Note infinity value here.
# print(a1-a2) ## [-5 -5 -5 -5  5]
# print(a1*a2) ## [ 6 14 24 36  0]  l1*l2 l1/2 li-l2 all are Type Error
a1= np.array([1,2,3]) # 1x3 must b 3xsomething 
a2=np.array([[1,3,5],[4,5,5]])
# print(a1*a2) # [[ 1  6 15] [ 4 10 15]]

print("+ , -, * / works on both array of same dimensions, and in list only + works and that is concatenation")
print("For different dimensions it should be compatible e.g 1*3 3*1 will work but 1*3 with 2*2 will not work")


# print(np.sqrt(a2)) # [[1.         1.73205081 2.23606798] [2.         2.23606798 2.23606798]]
# print(np.sin(a1))  # [0.84147098 0.90929743 0.14112001]
# print(np.cos(a1))  # [ 0.54030231 -0.41614684 -0.9899925 ]
# print(np.tan(a1))  # [ 1.55740772 -2.18503986 -0.14254654] 
# print(np.exp(a1))  # [ 2.71828183  7.3890561  20.08553692]
# print(np.log(a1))  # [0.         0.69314718 1.09861229]
#print(np.log2(a1))  # [0.        1.        1.5849625]
#print(np.log10(a1))  # [0.         0.30103    0.47712125]
print("np.math-funciton apply to all element e.g sqrt, sin, cos, tan, exp , log visit doc for the rest :  https://numpy.org/doc/2.1/reference/routines.math.html")
print("Note: We should always assign the value to vars, whenever do any change.")
a = np.array([1,2,3])
a = np.append(a,[7,8,9]) # Here list as well np.array([7,8,9]) both will work.
a = np.insert(a,3,[4,5,6])


# 1. Append along columns (axis=1)
# Input: ( 𝑚 , 𝑛 1 ) (m,n 1 ​ ) and ( 𝑚 , 𝑛 2 ) (m,n 2 ​ )
# Output: ( 𝑚 , 𝑛 1 + 𝑛 2 ) (m,n 1 ​ +n 2 ​ ) python Copy code

arr1 = np.array([[1, 2], [3, 4]])  # (2, 2)
arr2 = np.array([[5, 6], [7, 8]])  # (2, 2)
arr = np.append(arr1, arr2, axis=1)  # Result: (2, 4)
# 2. Append along rows (axis=0)
# Input: ( 𝑚 1 , 𝑛 ) (m 1 ​ ,n) and ( 𝑚 2 , 𝑛 ) (m 2 ​ ,n)
# Output: ( 𝑚 1 + 𝑚 2 , 𝑛 ) (m 1 ​ +m 2 ​ ,n) python Copy code
arr1 = np.array([[1, 2], [3, 4]])  # (2, 2)
arr2 = np.array([[5, 6], [7, 8]])  # (2, 2)
arr = np.append(arr1, arr2, axis=0)  # Result: (4, 2)
# 3. Append along rows (axis=0) or columns (axis=1)
# Input: ( 𝑚 , 𝑛 ) (m,n) and ( 𝑚 , 𝑛 ) (m,n)
# Output: ( 2 𝑚 , 𝑛 ) (2m,n) for axis=0 or ( 𝑚 , 2 𝑛 ) (m,2n) for axis=1
arr1 = np.array([[1, 2], [3, 4]])  # (2, 2)
arr2 = np.array([[5, 6], [7, 8]])  # (2, 2)
arr = np.append(arr1, arr2, axis=0)  # Result: (4, 2)
arr2 = np.append(arr1, arr2, axis=1)  # Result: (2, 4)
# 4. Flatten before appending
# Input: ( 𝑚 , 𝑛 ) (m,n) and ( 𝑚 × 𝑛 ) (m×n)
# Output: Flattened ( 𝑚 × 𝑛 ) (m×n) array
arr1 = np.array([[1, 2], [3, 4]])  # (2, 2)
arr2 = np.array([5, 6, 7, 8])      # (4,)
arr1_flat = arr1.flatten()          # (4,)
arr = np.append(arr1_flat, arr2)    # Result: (8,)

print("When appending two NumPy arrays, the condition for compatibility is that either the number of rows or the number of columns must be the same, ")
print("mxn1 mxn2 => mx n1+n2  | m1xn  m2xn => m1+m2xn | mxn mxn  2mxn or mx2n if axis=0 or axis=1, in this case need to flattern first ")
# 1. Delete along a specified axis
# Input: Array with shape ( 𝑚 , 𝑛 ) (m,n), axis specified.
# Output: Array with specified rows/columns removed.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # (3, 3)
arr_new = np.delete(arr, 1, axis=0)  # Delete row at index 1, Result: (2, 3)
# 2. Delete elements by index (flattened array)
# Input: 1D array, index of elements to delete.
# Output: 1D array with elements removed. python Copy code
arr = np.array([1, 2, 3, 4, 5])  # (5,)
arr_new = np.delete(arr, [1, 3])  # Delete elements at indices 1 and 3, Result: [1, 3, 5]
# 3. Delete along columns (axis=1)
# Input: Array with shape ( 𝑚 , 𝑛 ) (m,n), axis=1 (columns specified).
# Output: Array with specified columns removed. python Copy code
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # (3, 3)
arr_new = np.delete(arr, 1, axis=1)  # Delete column at index 1, Result: (3, 2)
# 4. Delete elements by value
# Input: 1D array, value to delete.
# # Output: 1D array with specified value(s) removed. python Copy code
arr = np.array([1, 2, 3, 4, 5])  # (5,)
arr_new = np.delete(arr, np.where(arr == 3))  # Delete element with value 3, Result: [1, 2, 4, 5]
print("np.delete removes elements or entire rows/columns from an array along a specified axis or by index, returning a new array with the specified elements deleted.")

# Original 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. reshape(): Returns a new reshaped array without altering the original array
reshaped_arr = arr.reshape(3, 2)  # Changes shape to (3, 2)
print("reshape() to 3x2:\n", reshaped_arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# 2. resize(): Modifies the array in-place, altering its shape and potentially changing data
arr.resize(3, 2)  # In-place resize to (3, 2)
print("resize() in-place to 3x2:\n", arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Reset array for further examples
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 3. flatten(): Returns a new 1D copy of the array
flat_arr = arr.flatten()
print("flatten() 1D copy:", flat_arr)
# Output:
# [1 2 3 4 5 6]

# 4. ravel(): Returns a flattened view (if possible) that reflects changes in the original array
ravel_arr = arr.ravel()
ravel_arr[0] = 99  # Modifying ravel array affects the original array
print("ravel() flattened view:", ravel_arr)
print("Original array after ravel modification:\n", arr)
# Output:
# ravel() flattened view: [99 2 3 4 5 6]
# Original array after ravel modification:
# [[99  2  3]
#  [ 4  5  6]]

# 5. flat: An iterator for traversing elements in 1D
print("Using flat iterator:")
for item in arr.flat:
    print(item, end=" ")
# Output:
# 99 2 3 4 5 6

print("""
reshape(): Returns a new reshaped array without modifying the original.
resize(): Reshapes the array in place, changing the original.
flatten(): Creates a 1D copy, so changes don’t affect the original.
ravel(): Provides a flattened view; changes may affect the original.
flat: An iterator for 1D traversal of array elements.
""")
print("Always pass tuple as shape as general guideline, any multiple will cause it reshape need to reassign, resize no need to assign More one is extra list only")
import numpy as np

# Original 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. Simple row-column swap (manually swapping rows/columns)
swapped = arr[:, [1, 0, 2]]  # Swaps columns 0 and 1
print("Manual column swap (columns 0 and 1):\n", swapped)
# Output:
# [[2 1 3]
#  [5 4 6]]

# 2. transpose() or .T: Transposes the array, swapping rows and columns
transposed = arr.transpose()  # Equivalent to arr.T
print("transpose() or .T:\n", transposed)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# 3. swapaxes(): Swaps specified axes
# For a 2D array, swapaxes(0, 1) is equivalent to transpose()
swapped_axes = arr.swapaxes(0, 1)  # Swaps rows and columns
print("swapaxes(0, 1):\n", swapped_axes)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# For 3D arrays, swapaxes can swap any two axes
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Shape (2, 2, 2)
swapped_3d = arr_3d.swapaxes(0, 2)  # Swaps axis 0 with axis 2
print("swapaxes(0, 2) on 3D array:\n", swapped_3d)
# Output:
# [[[1 5]
#   [3 7]]
#  [[2 6]
#   [4 8]]]

# 4. transpose() with specified axes: Allows custom axis reordering
custom_transpose = arr_3d.transpose(2, 0, 1)  # Rearranges axes (2, 0, 1)
print("transpose() with custom axes (2, 0, 1):\n", custom_transpose)
# Output:
# [[[1 3]
#   [5 7]]
#  [[2 4]
#   [6 8]]]
print("""
Manual Row/Column Swap: Use slicing to swap specific rows or columns.
transpose() or .T: Swaps all rows and columns in 2D arrays; can specify axis order in higher dimensions.
swapaxes(): Swaps only the specified axes, allowing selective axis swapping, especially useful in multi-dimensional arrays.
""")

import numpy as np

# Example arrays for joining and splitting
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 1. concatenate(): Joins arrays along an existing axis (0 = rows, 1 = columns)
concat_axis0 = np.concatenate((arr1, arr2), axis=0)  # Joins along rows (axis 0)
#print("concatenate along axis 0:\n", concat_axis0)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

concat_axis1 = np.concatenate((arr1, arr2), axis=1)  # Joins along columns (axis 1)
# print("concatenate along axis 1:\n", concat_axis1)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# 2. stack(): Stacks along a new dimension (default axis=0 adds a new outermost dimension)
stack_axis0 = np.stack((arr1, arr2), axis=0)  # Stacks along a new dimension at axis 0
#print("stack along new axis 0:\n", stack_axis0)
# Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]

# vstack(): Vertically stacks arrays along a new row dimension (similar to concatenate along axis=0)
v_stacked = np.vstack((arr1, arr2))
#print("vstack:\n", v_stacked)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# hstack(): Horizontally stacks arrays along a new column dimension (similar to concatenate along axis=1)
h_stacked = np.hstack((arr1, arr2))
#print("hstack:\n", h_stacked)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# 3. split(): Splits an array into multiple sub-arrays
split_result = np.split(concat_axis0, 2)  # Splits concat_axis0 into 2 equal parts along axis 0
#print("split into 2 parts along axis 0:\n", split_result)
# Output:
# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#                         [7, 8]])]

# Additional Example: Split array along columns
split_cols = np.split(concat_axis1, 2, axis=1)  # Splits concat_axis1 into 2 parts along axis 1 (columns)
# print("split into 2 parts along axis 1:\n", split_cols)
# Output:
# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#                         [7, 8]])]



print("""
np.concatenate(): Joins arrays along an existing axis. axis=0 joins rows, axis=1 joins columns.
np.stack(): Adds a new dimension and stacks arrays along this new axis, useful for multi-dimensional stacking.
np.vstack(): Vertically stacks arrays along a new row dimension, like concatenation along axis=0.
np.hstack(): Horizontally stacks arrays along a new column dimension, similar to concatenation along axis=1.
np.split(): Divides an array into multiple sub-arrays along a specified axis, useful for breaking arrays into equal parts.
""")



# Example array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. min(): Finds the minimum value in the array
min_value = np.min(arr)  # Minimum of entire array
# print("Minimum value:", min_value)
# Output:
# Minimum value: 1

min_axis0 = np.min(arr, axis=0)  # Minimum along rows (axis=0)
# print("Minimum along rows (axis=0):", min_axis0)
# Output:
# Minimum along rows (axis=0): [1 2 3]

min_axis1 = np.min(arr, axis=1)  # Minimum along columns (axis=1)
# print("Minimum along columns (axis=1):", min_axis1)
# Output:
# Minimum along columns (axis=1): [1 4]

# 2. max(): Finds the maximum value in the array
max_value = np.max(arr)  # Maximum of entire array
# print("Maximum value:", max_value)
# Output:
# Maximum value: 6

# 3. sum(): Calculates the sum of elements in the array
sum_total = np.sum(arr)  # Sum of entire array
# print("Total sum:", sum_total)
# Output:
# Total sum: 21

sum_axis0 = np.sum(arr, axis=0)  # Sum along rows (axis=0)
# print("Sum along rows (axis=0):", sum_axis0)
# Output:
# Sum along rows (axis=0): [5 7 9]

sum_axis1 = np.sum(arr, axis=1)  # Sum along columns (axis=1)
# print("Sum along columns (axis=1):", sum_axis1)
# Output:
# Sum along columns (axis=1): [ 6 15]

# 4. mean(): Calculates the mean (average) of elements
mean_value = np.mean(arr)  # Mean of entire array
# print("Mean value:", mean_value)
# Output:
# Mean value: 3.5

# 5. median(): Calculates the median value of elements
median_value = np.median(arr)  # Median of entire array
# print("Median value:", median_value)
# Output:
# Median value: 3.5

# 6. std(): Calculates the standard deviation
std_value = np.std(arr)  # Standard deviation of entire array
# print("Standard deviation:", std_value)
# Output:
# Standard deviation: 1.707825127659933

# 7. var(): Calculates the variance
var_value = np.var(arr)  # Variance of entire array
# print("Variance:", var_value)
# Output:
# Variance: 2.9166666666666665

# 8. prod(): Calculates the product of all elements
prod_value = np.prod(arr)  # Product of entire array
# print("Product of all elements:", prod_value)
# Output:
# Product of all elements: 720

# 9. cumsum(): Returns the cumulative sum of elements
cumsum_value = np.cumsum(arr)  # Cumulative sum of entire array
# print("Cumulative sum:", cumsum_value)
# Output:
# Cumulative sum: [ 1  3  6 10 15 21]

# 10. cumprod(): Returns the cumulative product of elements
cumprod_value = np.cumprod(arr)  # Cumulative product of entire array
# print("Cumulative product:", cumprod_value)
# Output:
# Cumulative product: [  1   2   6  24 120 720]


print("""Summary of NumPy Aggregate Functions
min(): Finds the minimum value, optionally along an axis.
max(): Finds the maximum value, optionally along an axis.
sum(): Calculates the sum of elements, optionally along an axis.
mean(): Calculates the mean (average) value.
median(): Finds the median value.
std(): Calculates the standard deviation.
var(): Finds the variance.
prod(): Calculates the product of all elements.
cumsum(): Provides the cumulative sum.
cumprod(): Provides the cumulative product.
Each of these functions can operate on the entire array or along a specified axis, providing flexibility for various calculations.
""")




import numpy as np

# 1. randint(): Generates random integers within a specified range
rand_int = np.random.randint(1, 10)  # A single random integer between 1 and 9
# print("Single random integer:", rand_int)
# Output example:
# Single random integer: 7

rand_int_array = np.random.randint(1, 10, size=(3, 3))  # 3x3 array of random integers from 1 to 9
# print("3x3 array of random integers between 1 and 9:\n", rand_int_array)
# Output example:
# [[3 8 5]
#  [1 4 7]
#  [6 9 2]]

# 2. rand(): Generates random floats between 0 and 1
rand_float = np.random.rand()  # Single random float between 0 and 1
# print("Single random float:", rand_float)
# Output example:
# Single random float: 0.764328

rand_float_array = np.random.rand(2, 3)  # 2x3 array of random floats between 0 and 1
# print("2x3 array of random floats between 0 and 1:\n", rand_float_array)
# Output example:
# [[0.536842 0.283291 0.756291]
#  [0.192384 0.764328 0.241594]]

# 3. random(): Similar to rand(), generates random floats between 0 and 1 with shape specified by `size`
rand_array_size = np.random.random(size=(4,))  # 1D array of 4 random floats
# print("1D array of 4 random floats:", rand_array_size)
# Output example:
# [0.545123 0.853924 0.294531 0.124531]

# 4. randn(): Generates random numbers from a standard normal distribution (mean=0, std=1)
randn_array = np.random.randn(2, 2)  # 2x2 array of random values from a normal distribution
# print("2x2 array from a normal distribution:\n", randn_array)
# Output example:
# [[-0.7852  1.5647]
#  [ 0.3419 -1.2564]]

# 5. choice(): Selects random elements from a given array
arr = np.array([10, 20, 30, 40, 50])
rand_choice = np.random.choice(arr, size=3)  # 3 random elements from arr
# print("3 random choices from array:", rand_choice)
# Output example:
# [20 10 50]

# 6. uniform(): Generates random floats within a specified range
rand_uniform = np.random.uniform(5, 15, size=(2, 2))  # 2x2 array with random floats between 5 and 15
# print("2x2 array with random floats between 5 and 15:\n", rand_uniform)
# Output example:
# [[ 7.2  9.3]
#  [11.8 14.6]]

# 7. binomial(): Generates samples from a binomial distribution
# Binomial distribution with n=10 trials and p=0.5 probability of success
binomial_samples = np.random.binomial(n=10, p=0.5, size=5)  # 5 samples of binomial distribution
# print("5 samples from a binomial distribution with n=10 and p=0.5:", binomial_samples)
# Output example:
# [4 5 7 3 6]
print("""Summary of NumPy Random Functions
randint(low, high, size): Generates random integers between low (inclusive) and high (exclusive), with an optional size for array dimensions.
rand(d0, d1, …): Generates random floats between 0 and 1 with shape specified by dimensions.
random(size): Generates random floats between 0 and 1, similar to rand(), with a specified shape.
randn(d0, d1, …): Generates random numbers from a standard normal distribution.
choice(a, size): Selects random samples from a given array a, with specified size.
uniform(low, high, size): Generates random floats within the specified range [low, high), with an optional shape.
binomial(n, p, size): Generates samples from a binomial distribution with n trials and probability p of success, useful for modeling binary outcomes.
""")



import numpy as np

# Example array to save and load
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. np.save(): Saves an array to a binary .npy file (optimized for large arrays)
np.save('example.npy', arr)
# print("Array saved to example.npy")

# 2. np.load(): Loads an array from a .npy file
loaded_arr = np.load('example.npy')
# print("Loaded array from .npy file:\n", loaded_arr)
# Output example:
# Loaded array from .npy file:
# [[1 2 3]
#  [4 5 6]]

# Saving and loading in .npy format is memory-efficient and preserves data types and structures.

# 3. np.savetxt(): Saves an array to a .csv file (text format, less optimized than .npy)
np.savetxt('example.csv', arr, delimiter=',', fmt='%d')
#print("Array saved to example.csv")

# 4. np.loadtxt(): Loads data from a .csv file or text file
loaded_csv = np.loadtxt('example.csv', delimiter=',')
#print("Loaded array from .csv file:\n", loaded_csv)
# Output example:
# Loaded array from .csv file:
# [[1. 2. 3.]
#  [4. 5. 6.]]

# Note: Data from .csv is loaded as floats by default. Use `dtype=int` in loadtxt if needed.
loaded_csv_int = np.loadtxt('example.csv', delimiter=',', dtype=int)
#print("Loaded array from .csv file as integers:\n", loaded_csv_int)
# Output example:
# Loaded array from .csv file as integers:
# [[1

print("""Summary of Formats
Format	Use Case	                        Speed	    MemoryEfficiency        Compression	        Recommended For
.npy	Single array storage	            Very fast	High        	            No	            Large datasets, single arrays
.npz	Multiple arrays	                    Fast	    High,with compression	    Yes	            Multiple arrays, large datasets
Parquet Columnar storage for tabular data	Very fast   Very high with compression	Snappy, GZIP,   Big data analytics, data engineering 	
                                        (selective columns)	                            Brotli
.csv	Interoperability (text-based)	    Slower	    Low	                    No	        Sharing with other applications
.txt	Simple text storage	                Slower	    Low	                    No	        Text-based or lightweight data
HDF5	Large, hierarchical data storage	Very fast	High, with compression	Yes	        Scientific, complex data storage
Pickle	Complex Python objects	            Fast	    Medium  	            No	        Python-specific complex objects
                                                (Python-specific)""")









