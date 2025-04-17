import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Merge price and units_sold data on product_id using LEFT JOIN to retain all price periods
    df = pd.merge(prices, units_sold, on='product_id', how='left')

    # Filter rows where either:
    # - there's no purchase (purchase_date is NaN), OR
    # - the purchase_date falls within the valid pricing period (start_date to end_date)
    df = df[df.purchase_date.isna() | ((df.purchase_date >= df.start_date) & (df.purchase_date <= df.end_date))]

    # Group by product_id and calculate weighted average price:
    # - Multiply price by units, sum it up for each product
    # - Divide by total units sold
    # - Round to 2 decimal places
    # - If total units = 0, return 0 instead of division by zero
    result = df.groupby('product_id').apply(
        lambda x: round((x['price'] * x['units']).sum() / x['units'].sum(), 2)
        if x['units'].sum() != 0 else 0
    ).reset_index(name='average_price')

    return result
