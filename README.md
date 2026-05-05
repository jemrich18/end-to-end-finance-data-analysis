# 💰 Personal Finance Analysis Dashboard

An interactive data analysis dashboard exploring 1,500 personal finance transactions across 5 years (2020–2024). Built with Python, Pandas, and Streamlit to uncover spending patterns, identify trends, and forecast future expenses using Linear Regression.

**[Live Demo](https://end-to-end-finance-data-analysis-4qjvmptdvwcv5mcrfkydze.streamlit.app/)** | **[GitHub](https://github.com/jemrich18/end-to-end-finance-data-analysis)**

---

## Overview

This project follows the full data analysis workflow — from raw data generation and cleaning, through SQL-based analysis and visualization, to predictive modelling and interactive deployment. The dataset contains 1,500 transactions spanning 5 years across 10 spending categories.

**Key Question:** Where is money being spent, how has spending changed over time, and what can we expect in the future?

---

## Interactive Dashboard Features

- **KPI Metrics** — total income, total expenses, net balance, and transaction count update dynamically with filters
- **Sidebar Filters** — filter by year, transaction type, and spending category
- **Income vs Expenses by Year** — grouped bar chart comparing annual income and spending
- **Spending by Category** — pie chart breaking down expense distribution across 10 categories
- **Monthly Spending Trend** — 5 year line chart showing month to month expense volatility
- **Spending by Day of Week** — identifies which days drive the most spending
- **6 Month Forecast** — Linear Regression model projecting future expenses based on historical trends
- **Transaction Data Table** — searchable and sortable raw transaction records

---

## Project Structure

```
personal-finance-dashboard/
├── app.py                  # Streamlit dashboard application
├── generate_data.py        # Synthetic dataset generator
├── finance_data.csv        # Generated transaction dataset
├── requirements.txt        # Python dependencies
├── notebooks/
│   ├── 01_cleaning.ipynb          # Data cleaning and preparation
│   ├── 02_sql_analysis.ipynb      # SQL queries and business insights
│   ├── 03_visualizations.ipynb    # Static data visualizations
│   └── 04_forecasting.ipynb       # Predictive modelling
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| SQLite3 | In-memory SQL database |
| Streamlit | Interactive web dashboard |
| Plotly | Interactive charts and visualizations |
| Scikit-learn | Linear Regression forecasting model |
| Matplotlib / Seaborn | Static notebook visualizations |
| Jupyter Notebook | Exploratory analysis environment |

---

## Dataset

The dataset is synthetically generated using `generate_data.py` to simulate realistic personal finance transactions across 10 categories:

- Travel, Rent, Food & Drink, Entertainment, Shopping
- Utilities, Health & Fitness, Investment, Other, Salary

**Dataset overview:**
- 1,500 transactions across 5 years (2020–2024)
- Columns: Date, Category, Amount, Type
- Transaction types: Income and Expense

---

## Key Findings

- Income consistently exceeds expenses across all 5 years resulting in a healthy surplus
- Rent is the largest single expense category at approximately 33% of total spending
- Travel represents significant discretionary spending at roughly 25% of expenses
- Monthly expenses show high volatility suggesting irregular large purchases
- Wednesday and Saturday drive the highest spending by day of week
- Linear Regression forecasts stable expenses around $10,000–$12,000 per month going forward

---

## Running Locally

```bash
# Clone the repository
git clone https://github.com/jemrich18/personal-finance-dashboard.git
cd personal-finance-dashboard

# Install dependencies
pip install -r requirements.txt

# Generate the dataset (if needed)
python generate_data.py

# Run the dashboard
streamlit run app.py
```

---

## Notebook Analysis

The `notebooks/` folder contains the full exploratory analysis:

- **01 — Data Cleaning** — data types, missing values, feature engineering
- **02 — SQL Analysis** — SQLite queries answering key business questions
- **03 — Visualizations** — static charts communicating key findings
- **04 — Forecasting** — Linear Regression model with train/test split and 6 month projection

---

## About the Developer

I'm an FAA certified Airframe Mechanic transitioning into software and data development. I built this project to demonstrate end-to-end data analysis skills — from raw data through cleaning, SQL analysis, visualization, machine learning, and interactive deployment.

Portfolio: [jemrich.dev](https://www.jemrich.dev)
GitHub: [github.com/jemrich18](https://github.com/jemrich18)

---

## License

MIT License — free to use and modify with attribution.