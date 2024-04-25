import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

    # OR

    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

#2882. Drop Duplicate Rows
# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.
#
# Write a solution to remove these duplicate rows and keep only the first occurrence.
#
# The result format is in the following example.