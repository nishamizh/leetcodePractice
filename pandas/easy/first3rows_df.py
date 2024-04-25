#Write a solution to display the first 3 rows of this DataFrame.

#2879. Display the First Three Rows
from typing import List
import pandas as pd

#2879. Display the First Three Rows

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=students[students['student_id']==101]
    return df[['name','age']]