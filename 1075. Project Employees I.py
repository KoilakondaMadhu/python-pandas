import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(project, employee, how='left')

    return df[['project_id','experience_years']
                    ].groupby('project_id').mean().round(2).reset_index(
                    ).rename(columns = {'experience_years':'average_years'})
