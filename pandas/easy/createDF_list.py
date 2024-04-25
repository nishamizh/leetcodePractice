import pandas as pd
from typing import List

# Leet-2877 Create a Data from List

list_2d = [[1,15],[2,11],[3,11],[4,20]]

# alias 1 - method
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id','age'])
    return df

print(createDataframe(list_2d))

# Alias 2
df = pd.DataFrame(list_2d, columns=['student_id','age'])
print(df)

# alias 3 - has less runtime
column_name = ['student_id','age']
df=pd.DataFrame(list_2d,columns=column_name)
print(df)

#Write a solution to create a DataFrame from a 2D list called student_data.This 2D list contains the IDs and ages of some students.
#The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
#The result format is in the following example.
# Example
# 1:Input:
# student_data:
# [
#     [1, 15],
#     [2, 11],
#     [3, 11],
#     [4, 20]
# ]
# Output:
# +------------+-----+
# | student_id | age |
# +------------+-----+
# | 1 | 15 |
# | 2 | 11 |
# | 3 | 11 |
# | 4 | 20 |
# +------------+-----+
# Explanation:
# A DataFrame was created on top of student_data,with two columns named student_id and age.

