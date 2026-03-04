# 💰 End-to-End Personal Finance Data Analysis

A complete data analysis project exploring personal finance transaction data to uncover spending patterns, identify trends, and forecast future expenses.

---

## 📌 Project Overview

This project follows the full data analysis workflow — from raw data ingestion and cleaning, through SQL-based analysis and visualisation, to predictive modelling. The dataset contains 1,500 transactions spanning 5 years (2020–2024) across 10 spending categories.

**Key Question:** *Where is money being spent, how has spending changed over time, and what can we expect in the future?*

---

## 🗂️ Project Structure

```
end-to-end-finance-data-analysis/
├── data/                          # Data files (not included in repo — see below)
├── notebooks/
│   ├── 01_cleaning.ipynb          # Data cleaning and preparation
│   ├── 02_sql_analysis.ipynb      # SQL queries and business insights
│   ├── 03_visualizations.ipynb    # Data visualisations
│   └── 04_forecasting.ipynb       # Predictive modelling
└── README.md
```

---

## 📊 Dataset

**Source:** [Personal Finance Dataset — Kaggle](https://www.kaggle.com)

The dataset is not included in this repository due to licensing restrictions. To reproduce this project:
1. Download the dataset from Kaggle (search: *personal spending habits dataset*)
2. Place the CSV file in the `data/` folder
3. Rename it to `Personal_Finance_Dataset.csv`

**Dataset Overview:**
- 1,500 transactions across 5 years (2020–2024)
- 5 columns: `Date`, `Transaction Description`, `Category`, `Amount`, `Type`
- 10 categories: Travel, Rent, Food & Drink, Entertainment, Shopping, Utilities, Health & Fitness, Investment, Other, Salary

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| SQLite3 | In-memory SQL database |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Scikit-learn | Linear regression model |
| Jupyter Notebook | Development environment |
| uv | Package management |

---

## 📁 Notebook Summaries

### 01 — Data Cleaning
- Loaded raw CSV and inspected structure, data types, and missing values
- Converted `Date` column from string to datetime
- Extracted `Year`, `Month`, `Month_Name`, and `Day_of_Week` columns
- **Identified and corrected a data quality issue:** 146 Salary transactions were incorrectly labelled as `Expense` — corrected to `Income`
- Saved cleaned dataset for downstream analysis

### 02 — SQL Analysis
- Loaded cleaned data into a SQLite in-memory database
- Wrote queries to answer key business questions:
  - Total income vs total expenses
  - Highest spending categories
  - Monthly income and expense trends
  - Average, min, and max transaction by category

### 03 — Visualisations
Four charts were produced to communicate key findings:

**Chart 1 — Total Income vs Expenses**

![Income vs Expenses](data/chart1_income_vs_expenses.png)

**Chart 2 — Spending by Category**

![Spending by Category](data/chart2_spending_by_category.png)

**Chart 3 — Monthly Trend (2020–2024)**

![Monthly Trend](data/chart3_monthly_trend.png)

**Chart 4 — Spending Heatmap by Day of Week**

![Heatmap](data/chart4_spending_heatmap.png)

### 04 — Forecasting
- Aggregated monthly expenses and created a sequential month number feature
- Split data 80/20 (train/test) using chronological ordering
- Trained a **Linear Regression** model using Scikit-learn
- Evaluated model performance and forecasted the next 6 months of expenses

---

## 📈 Key Findings

- 💸 **Total expenses ($1,227,194) significantly exceed total income ($734,087)** across the dataset period
- 🏖️ **Travel is the highest expense category** at $169,498 across 160 transactions
- 📅 **Income is highly volatile** month to month while expenses remain more consistent
- 🍔 **Food & Drink spending peaks mid-week (Wednesday) and on Sundays**
- 🏋️ **Health & Fitness spending is highest on Saturdays**
- 📉 **Expenses show a slight downward trend** of ~$24 per month over the 5 year period

---

## 🤖 Model Performance

| Metric | Value |
|--------|-------|
| Model | Linear Regression |
| Train/Test Split | 80% / 20% (48 / 12 months) |
| Mean Absolute Error | $3,420.24 |
| Root Mean Squared Error | $4,328.71 |

**6 Month Forecast:**
| Month | Predicted Expenses |
|-------|--------------------|
| Month 61 | $17,095.90 |
| Month 62 | $17,071.61 |
| Month 63 | $17,047.33 |
| Month 64 | $17,023.04 |
| Month 65 | $16,998.75 |
| Month 66 | $16,974.46 |

> **Note:** The linear model captures the overall trend well but the high month-to-month volatility suggests a more advanced time series model (ARIMA, Random Forest) could improve forecast accuracy — a natural next iteration of this project.

---

## 🚀 How to Run This Project

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/end-to-end-finance-data-analysis.git
cd end-to-end-finance-data-analysis
```

**2. Set up the virtual environment**
```bash
uv venv
uv add pandas numpy matplotlib seaborn scikit-learn ipykernel jupyter
```

**3. Download the dataset** (see Dataset section above) and place it in `data/`

**4. Run the notebooks in order**
```
01_cleaning.ipynb → 02_sql_analysis.ipynb → 03_visualizations.ipynb → 04_forecasting.ipynb
```

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](#) or reach out via [GitHub](#) if you have any questions about this project.