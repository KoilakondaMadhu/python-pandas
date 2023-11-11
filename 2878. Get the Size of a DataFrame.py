# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Importing the List type from the typing module
from typing import List

# Defining a function named getDataframeSize that takes a pandas DataFrame as input
def getDataframeSize(players: pd.DataFrame) -> List:
    # Using the shape attribute of the DataFrame to get the number of rows and columns
    # The shape attribute returns a tuple (number_of_rows, number_of_columns)
    size_list = [players.shape[0], players.shape[1]]
    
    # Returning the list containing the number of rows and columns
    return size_list


# Example 1:

# Input:
# +-----------+----------+-----+-------------+--------------------+
# | player_id | name     | age | position    | team               |
# +-----------+----------+-----+-------------+--------------------+
# | 846       | Mason    | 21  | Forward     | RealMadrid         |
# | 749       | Riley    | 30  | Winger      | Barcelona          |
# | 155       | Bob      | 28  | Striker     | ManchesterUnited   |
# | 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
# | 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
# | 883       | Ava      | 23  | Defender    | Chelsea            |
# | 355       | Violet   | 18  | Striker     | Juventus           |
# | 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
# | 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
# | 642       | Charlie  | 36  | Center-back | Arsenal            |
# +-----------+----------+-----+-------------+--------------------+
# Output:
# [10, 5]
# Explanation:
# This DataFrame contains 10 rows and 5 columns.
