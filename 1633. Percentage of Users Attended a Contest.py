import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby('contest_id', as_index=False).agg(count=('user_id','nunique'))
    df['percentage'] = df['count']/len(users)*100
    return df[['contest_id','percentage']].sort_values(by=['percentage', 'contest_id'], ascending=[False, True]).round(2)
