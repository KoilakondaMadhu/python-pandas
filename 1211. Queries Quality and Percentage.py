import pandas as pd

def queries_stats(df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Add two new columns to the DataFrame:
    
    # 1. 'quality' is defined as rating / position.
    #    Adding a small value (1e-10) avoids division by zero errors.
    df = df.assign(
        quality = df.rating / df.position + 1e-10,
        
        # 2. 'poor_query_percentage' is 100 if rating < 3, otherwise 0.
        #    This treats any query with a rating below 3 as "poor."
        poor_query_percentage = (df.rating < 3).astype(int) * 100
    )
    
    # Step 2: Group by 'query_name' and calculate the mean of 'quality' and 'poor_query_percentage'
    # Round the results to 2 decimal places.
    return df.groupby("query_name", as_index=False)[["quality", "poor_query_percentage"]].mean().round(2)
