# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named dropMissingData that takes a pandas DataFrame as input
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Using boolean indexing to select rows where the "name" column is not null
    result = students[students['name'].notnull()]
    
    # Returning the resulting DataFrame
    return result




# Case 1
# Input
# students =
# | student_id | name    | age |
# | ---------- | ------- | --- |
# | 32         | Piper   | 5   |
# | 217        | null    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# Output
# | student_id | name    | age |
# | ---------- | ------- | --- |
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# Expected
# | student_id | name    | age |
# | ---------- | ------- | --- |
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# Contrib







# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.

# Write a solution to remove the rows with missing values.

# The result format is in the following example.

 

# Example 1:

# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  | 
# | 849        | Willow  | 14  | 
# +------------+---------+-----+
# Explanation: 
# Student with id 217 havs empty value in the name column, so it will be removed.
