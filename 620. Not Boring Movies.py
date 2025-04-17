import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return (
        # Step 1: Filter rows where:
        # - Movie ID is odd (id % 2 == 1)
        # - Description is NOT 'boring'
        cinema[(cinema.id % 2 == 1) & (cinema.description != 'boring')]
        
        # Step 2: Sort the filtered DataFrame by 'rating' in descending order
        .sort_values('rating', ascending=False)
    )
