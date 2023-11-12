import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    Filter and sort a DataFrame of animals to find thos
    with a weight greater than 100.

    This function reduces memory usage by selecting only the necessary
    columns ['name', 'weight']
    and then filters animals based on their weight before sorting.
    Sorting is performed on the filtered subset of heavy animals,
    improving efficiency when dealing with large datasets.

    Parameters:
    - animals (pd.DataFrame): A DataFrame containing information
    about animals, including their names and weights.

    Returns:
    - pd.DataFrame: A DataFrame containing the names of animals with
    a weight greater than 100,
      sorted by weight in descending order.
    """
    # Reduce the memory usage by selecting only the needed columns
    animals = animals[["name", "weight"]]

    # Filter animals based on their weight before sorting
    heavy_animals = animals[animals["weight"] > 100]

    # Sort the smaller df which is more efficient
    heavy_animals = heavy_animals.sort_values(by="weight", ascending=False)[["name"]]

    return heavy_animals




# DataFrame animals
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | species     | object |
# | age         | int    |
# | weight      | int    |
# +-------------+--------+
# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

# Return the animals sorted by weight in descending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# DataFrame animals:
# +----------+---------+-----+--------+
# | name     | species | age | weight |
# +----------+---------+-----+--------+
# | Tatiana  | Snake   | 98  | 464    |
# | Khaled   | Giraffe | 50  | 41     |
# | Alex     | Leopard | 6   | 328    |
# | Jonathan | Monkey  | 45  | 463    |
# | Stefan   | Bear    | 100 | 50     |
# | Tommy    | Panda   | 26  | 349    |
# +----------+---------+-----+--------+
# Output: 
# +----------+
# | name     |
# +----------+
# | Tatiana  |
# | Jonathan |
# | Tommy    |
# | Alex     |
# +----------+
# Explanation: 
# All animals weighing more than 100 should be included in the results table.
# Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
# The results should be sorted in descending order of weight.
 
