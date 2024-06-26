import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ['name'])

# less Time Complexity
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
  return students[students['name'].notnull()]




# 2883. Drop Missing Data
# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.
#
# Write a solution to remove the rows with missing values.