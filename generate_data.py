import pandas as pd
import numpy as np

np.random.seed(42)

categories = ['Food & Drink', 'Travel', 'Rent', 'Entertainment', 
              'Shopping', 'Utilities', 'Health & Fitness', 
              'Investment', 'Other', 'Salary']

dates = pd.date_range(start='2020-01-01', end='2024-12-31', periods=1500)

rows = []
for date in dates:
    category = np.random.choice(categories, p=[0.15,0.10,0.12,0.08,0.12,0.08,0.07,0.06,0.07,0.15])
    if category == 'Salary':
        amount = round(np.random.uniform(4000, 6000), 2)
        type_ = 'Income'
    elif category == 'Rent':
        amount = round(np.random.uniform(800, 1500), 2)
        type_ = 'Expense'
    elif category == 'Travel':
        amount = round(np.random.uniform(200, 2000), 2)
        type_ = 'Expense'
    else:
        amount = round(np.random.uniform(20, 500), 2)
        type_ = 'Expense'
    rows.append({'Date': date, 'Category': category, 'Amount': amount, 'Type': type_})

df = pd.DataFrame(rows)
df.to_csv('finance_data.csv', index=False)
print(f"Generated {len(df)} transactions")