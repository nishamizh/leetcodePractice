from typing import List

import pandas as pd

#2878. Get the Size of a DataFrame


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row,column = players.shape
    return [row,column]

# alias 2 - with less runtime
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.
#
# Return the result as an array:
# [number of rows, number of columns]
# Output:
# [10, 5]
# Explanation:
# This DataFrame contains 10 rows and 5 columns.


