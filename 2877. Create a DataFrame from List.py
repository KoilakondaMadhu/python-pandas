# Importing the List type from the typing module
from typing import List

# Importing the pandas library and renaming it as pd for convenience
import pandas as pd

# Defining a function named createDataframe that takes a List of Lists of integers as input
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    # Specifying the column names for the DataFrame
    column_names = ['student_id', 'age']
    
    # Creating a pandas DataFrame from the input student_data and assigning column names
    result = pd.DataFrame(student_data, columns=column_names)
    
    # Returning the resulting DataFrame
    return result
