import pandas as pd 
import numpy as np
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
# print(df.head())
""" First 5 rows how it looks like index from 0 in row and column both
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9
"""
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"])
# print(df.head())
""" Genrally columns comes with data file
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
"""
# print(df.head(1)) # First Row 
"""
   A  B  C
0  1  2  3
"""
# print(df.head(2)) # First 2 Row 
"""
   A  B  C
0  1  2  3
1  4  5  6
"""
#print(df.tail(2)) # First 2 Row 
"""
   A  B  C
1  4  5  6
2  7  8  9
"""
# print(df.columns)
# Index(['A', 'B', 'C'], dtype='object')

# The values in left colum called index 0,1,2
# 
# print(df.index) # RangeIndex(start=0, stop=3, step=1)
# print(df.index.tol_list) # [0,1,2] # index are useful 
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"])
# print(df.index) # Index(['x', 'y', 'z'], dtype='object')
# print(df)
""" No need f head can print directly as well as it is not big enough and we are can  fetch all 
   A  B  C
x  1  2  3
y  4  5  6
z  7  8  9
"""
# print(df.info())
""" Can see taking a lot of space. 
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, x to z
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   A       3 non-null      int64
 1   B       3 non-null      int64
 2   C       3 non-null      int64
dtypes: int64(3)
memory usage: 96.0+ bytes
None
"""
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"], index=["x","y","z"], dtype=np.int8)
#print(df.info())
""" AMount of memory used by df is optimized here and this will be takien an load all at once in general. Can not take more space than RAM size allocated. Pyspark will be used in that case where data will be distributed.
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, x to z
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   A       3 non-null      int8
 1   B       3 non-null      int8
 2   C       3 non-null      int8
dtypes: int8(3)
memory usage: 33.0+ bytes
None
"""
#print(df.describe())
"""
         A    B    C
count  3.0  3.0  3.0
mean   4.0  5.0  6.0
std    3.0  3.0  3.0
min    1.0  2.0  3.0
25%    2.5  3.5  4.5
50%    4.0  5.0  6.0
75%    5.5  6.5  7.5
max    7.0  8.0  9.0
"""
df = pd.DataFrame([ [1,"nishu",3],[1,4,4],[1,8,9]], columns=["A","B","C"])
# print(df.nunique())
""" By columns its doing unique , in A, B and C how many unique values
A    1
B    3
C    3
dtype: int64
"""
# print(df["A"].unique()) # [1]
# print(df["B"].unique()) # ['nishu' 4 8]
# print(df.shape) # (3, 3)
