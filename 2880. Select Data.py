# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named selectData that takes a pandas DataFrame as input
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Using the loc method to select rows where "student_id" is equal to 101,
    # and selecting only the "name" and "age" columns
    selected_data = students.loc[students["student_id"] == 101, ["name", "age"]]
    
    # Returning the resulting DataFrame
    return selected_data





# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+

# Write a solution to select the name and age of the student with student_id = 101.

# The result format is in the following example.

 

# Example 1:
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# +------------+---------+-----+
# Output:
# +---------+-----+
# | name    | age | 
# +---------+-----+
# | Ulysses | 13  |
# +---------+-----+
# Explanation:
# Student Ulysses has student_id = 101, we select the name and age.






# Accepted
# Runtime: 476 ms
# Case 1
# Input
# students =
# | student_id | name    | age |
# | ---------- | ------- | --- |
# | 101        | Ulysses | 13  |
# | 53         | William | 10  |
# | 128        | Henry   | 6   |
# | 3          | Henry   | 11  |
# Output
# | name    | age |
# | ------- | --- |
# | Ulysses | 13  |
# Expected
# | name    | age |
# | ------- | --- |
# | Ulysses | 13  |
