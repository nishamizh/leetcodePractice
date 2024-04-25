import pandas as pd
#2881. Create a New Column

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['bonus'] = df['salary']*2
    return df
# alias -2 - faster execution
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# A company plans to provide its employees with a bonus.
#
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.
# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+