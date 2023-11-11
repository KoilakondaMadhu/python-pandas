# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named modifySalaryColumn that takes a pandas DataFrame as input
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Modifying the values in the "salary" column by multiplying them by 2
    employees['salary'] = employees['salary'] * 2
    
    # Returning the modified DataFrame
    return employees




# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.

# Write a solution to modify the salary column by multiplying each salary by 2.

# The result format is in the following example.

 

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+
# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# Explanation:
# Every salary has been doubled.
# Case 1
# Input
# employees =
# | name    | salary |
# | ------- | ------ |
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# Output
# | name    | salary |
# | ------- | ------ |
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# Expected
# | name    | salary |
# | ------- | ------ |
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
