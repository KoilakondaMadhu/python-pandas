import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values in the 'quantity' column with zeros
    products["quantity"] = products["quantity"].fillna(0)
    
    # Return the modified DataFrame
    return products












# DataFrame products
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+
# Write a solution to fill in the missing value as 0 in the quantity column.

# The result format is in the following example.

 

# Example 1:
# Input:+-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | None     | 135   |
# | WirelessEarbuds | None     | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# Output:
# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# Explanation: 
# The quantity for Wristwatch and WirelessEarbuds are filled by 0.







# Case 1
# Input
# products =
# | name            | quantity | price |
# | --------------- | -------- | ----- |
# | Wristwatch      | null     | 135   |
# | WirelessEarbuds | null     | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# Output
# | name            | quantity | price |
# | --------------- | -------- | ----- |
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# Expected
# | name            | quantity | price |
# | --------------- | -------- | ----- |
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
