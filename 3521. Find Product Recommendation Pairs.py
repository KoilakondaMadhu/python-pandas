import pandas as pd
from collections import defaultdict

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # Create a mapping from product_id to its category
    product_info_map = dict(zip(product_info.product_id, product_info.category))

    # Track which users bought which product
    product_user_map = defaultdict(set)
    for pid, uid in zip(product_purchases.product_id, product_purchases.user_id):
        product_user_map[pid].add(uid)

    # List of all products
    products = sorted(product_user_map.keys())
    n = len(products)

    # To store pairwise intersection sizes
    common_users_count = defaultdict(list)

    for i in range(n):
        pid1 = products[i]
        users1 = product_user_map[pid1]
        for j in range(i + 1, n):
            pid2 = products[j]
            users2 = product_user_map[pid2]
            common_users = users1 & users2
            count = len(common_users)
            if count >= 3:  # Only keep if at least 3 users bought both
                common_users_count[count].append((pid1, pid2))

    # Prepare the result
    result = {
        'product1_id': [],
        'product2_id': [],
        'product1_category': [],
        'product2_category': [],
        'customer_count': []
    }

    # Sort by number of common users (desc)
    for count in sorted(common_users_count.keys(), reverse=True):
        for pid1, pid2 in common_users_count[count]:
            result['product1_id'].append(pid1)
            result['product2_id'].append(pid2)
            result['product1_category'].append(product_info_map[pid1])
            result['product2_category'].append(product_info_map[pid2])
            result['customer_count'].append(count)

    return pd.DataFrame(result)
