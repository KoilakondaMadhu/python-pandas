
import pandas as pd

# Define a function named pivotTable that takes a pandas DataFrame as input
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Use the pivot method to create a pivot table
    # 'month' will be the index of the new table
    # 'city' will be the columns of the new table
    # 'temperature' will be the values of the new table
    ans = weather.pivot(index='month', columns='city', values='temperature')
    
    # Return the resulting pivoted DataFrame
    return ans





# 2889. Reshape Data: Pivot

# DataFrame weather
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | city        | object |
# | month       | object |
# | temperature | int    |
# +-------------+--------+
# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

# The result format is in the following example.

 

# Example 1:
# Input:
# +--------------+----------+-------------+
# | city         | month    | temperature |
# +--------------+----------+-------------+
# | Jacksonville | January  | 13          |
# | Jacksonville | February | 23          |
# | Jacksonville | March    | 38          |
# | Jacksonville | April    | 5           |
# | Jacksonville | May      | 34          |
# | ElPaso       | January  | 20          |
# | ElPaso       | February | 6           |
# | ElPaso       | March    | 26          |
# | ElPaso       | April    | 2           |
# | ElPaso       | May      | 43          |
# +--------------+----------+-------------+
# Output:
# +----------+--------+--------------+
# | month    | ElPaso | Jacksonville |
# +----------+--------+--------------+
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March   | 26     | 38           |
# | May      | 43     | 34           |
# +----------+--------+--------------+
# Explanation:
# The table is pivoted, each column represents a city, and each row represents a specific month.


#   Accepted
# Runtime: 446 ms
# Case 1
# Input
# weather =
# Open Raw
# | city         | month    | temperature |
# | ------------ | -------- | ----------- |
# | Jacksonville | January  | 13          |
# | Jacksonville | February | 23          |
# | Jacksonville | March    | 38          |
# | Jacksonville | April    | 5           |
# | Jacksonville | May      | 34          |
# | ElPaso       | January  | 20          |...
# Output
# | month    | ElPaso | Jacksonville |
# | -------- | ------ | ------------ |
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March    | 26     | 38           |
# | May      | 43     | 34           |
# Expected
# | month    | ElPaso | Jacksonville |
# | -------- | ------ | ------------ |
# | April    | 2      | 5            |
# | February | 6      | 23           |
# | January  | 20     | 13           |
# | March    | 26     | 38           |
# | May      | 43     | 34           |
