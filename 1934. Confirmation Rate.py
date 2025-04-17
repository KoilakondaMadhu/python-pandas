import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    confirmations['confirmation_rate'] = confirmations['action'].apply(lambda x:1 if x == 'confirmed' else 0)
    avg_conf = confirmations[['user_id','confirmation_rate']].groupby('user_id')['confirmation_rate'].mean().round(2).reset_index()
    output = pd.merge(signups['user_id'],avg_conf,how='left').fillna(0)  
    return output
