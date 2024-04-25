from typing import List
import pandas as pd

#2880. Select Data
#  less runtime
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=students[students['student_id']==101]
    return df[['name','age']]

# alias1

    return students.loc[students["student_id"] == 101, ["name", "age"]]
    # OR
    return students.loc[students["student_id"] == 101, "name" :]
    # OR
    return students[students['student_id'] == 101][['name', 'age']]

# alias 3
    df=students[students['student_id']==101]
    return df[['name','age']]

# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
#
# Write a solution to select the name and age of the student with student_id = 101.

