# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named dropDuplicateEmails that takes a pandas DataFrame as input
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Using the drop_duplicates method to remove duplicate rows based on the "email" column
    # The resulting DataFrame is returned
    return customers.drop_duplicates(subset=['email'])



#++++++++++++++++++ second


# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named dropDuplicateEmails that takes a pandas DataFrame as input
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Using the drop_duplicates method with inplace=True to remove duplicate rows based on the "email" column
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    
    # The modified DataFrame is returned (though this is not necessary due to inplace=True)
    return customers




# Case 1
# Input
# customers =
# | customer_id | name    | email               |
# | ----------- | ------- | ------------------- |
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# Output
# | customer_id | name    | email               |
# | ----------- | ------- | ------------------- |
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# # | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# Expected
# | customer_id | name    | email               |
# | ----------- | ------- | ------------------- |
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# Contribut



# ===================================================================



# DataFrame customers
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | customer_id | int    |
# | name        | object |
# | email       | object |
# +-------------+--------+
# There are some duplicate rows in the DataFrame based on the email column.

# Write a solution to remove these duplicate rows and keep only the first occurrence.

# The result format is in the following example.

 

# Example 1:
# Input:
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 5           | Finn    | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Output:  
# +-------------+---------+---------------------+
# | customer_id | name    | email               |
# +-------------+---------+---------------------+
# | 1           | Ella    | emily@example.com   |
# | 2           | David   | michael@example.com |
# | 3           | Zachary | sarah@example.com   |
# | 4           | Alice   | john@example.com    |
# | 6           | Violet  | alice@example.com   |
# +-------------+---------+---------------------+
# Explanation:
# Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.
