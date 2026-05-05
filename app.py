import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("finance_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Month_Name'] = df['Date'].dt.strftime('%B')
    df['Day_of_Week'] = df['Date'].dt.strftime('%A')
    return df

df = load_data()

st.title("💰 Personal Finance Analysis Dashboard")
st.markdown("Interactive analysis of 1,500 transactions across 5 years (2020–2024)")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filters")
years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect("Year", years, default=years)
selected_type = st.sidebar.multiselect("Transaction Type", ['Income', 'Expense'], default=['Income', 'Expense'])
selected_categories = st.sidebar.multiselect("Category", df['Category'].unique(), default=df['Category'].unique())

filtered = df[
    (df['Year'].isin(selected_years)) &
    (df['Type'].isin(selected_type)) &
    (df['Category'].isin(selected_categories))
]

# --- KPI METRICS ---
total_income = filtered[filtered['Type'] == 'Income']['Amount'].sum()
total_expenses = filtered[filtered['Type'] == 'Expense']['Amount'].sum()
net_balance = total_income - total_expenses
total_transactions = len(filtered)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Income", f"${total_income:,.2f}")
col2.metric("Total Expenses", f"${total_expenses:,.2f}")
col3.metric("Net Balance", f"${net_balance:,.2f}", delta=f"{'Surplus' if net_balance > 0 else 'Deficit'}")
col4.metric("Total Transactions", f"{total_transactions:,}")

st.divider()

# --- INCOME VS EXPENSES BY YEAR ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Income vs Expenses by Year")
    yearly = filtered.groupby(['Year', 'Type'])['Amount'].sum().reset_index()
    fig1 = px.bar(yearly, x='Year', y='Amount', color='Type',
                  barmode='group', color_discrete_map={'Income': '#2ecc71', 'Expense': '#e74c3c'})
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Spending by Category")
    expenses_by_cat = filtered[filtered['Type'] == 'Expense'].groupby('Category')['Amount'].sum().reset_index()
    fig2 = px.pie(expenses_by_cat, values='Amount', names='Category',
                  color_discrete_sequence=px.colors.sequential.RdBu)
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# --- MONTHLY TREND ---
col3, col4 = st.columns(2)

with col3:
    st.subheader("Monthly Spending Trend")
    monthly = filtered[filtered['Type'] == 'Expense'].groupby(
        filtered['Date'].dt.to_period('M')
    )['Amount'].sum().reset_index()
    monthly['Date'] = monthly['Date'].astype(str)
    fig3 = px.line(monthly, x='Date', y='Amount', markers=False,
                   color_discrete_sequence=['#e74c3c'])
    fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig3.update_xaxes(tickangle=45, nticks=20)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Spending by Day of Week")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow = filtered[filtered['Type'] == 'Expense'].groupby('Day_of_Week')['Amount'].sum().reset_index()
    dow['Day_of_Week'] = pd.Categorical(dow['Day_of_Week'], categories=day_order, ordered=True)
    dow = dow.sort_values('Day_of_Week')
    fig4 = px.bar(dow, x='Day_of_Week', y='Amount',
                  color='Amount', color_continuous_scale='Reds')
    fig4.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# --- FORECAST ---
st.subheader("6 Month Expense Forecast (Linear Regression)")
monthly_expenses = df[df['Type'] == 'Expense'].groupby(
    df['Date'].dt.to_period('M')
)['Amount'].sum().reset_index()
monthly_expenses['Month_Num'] = range(1, len(monthly_expenses) + 1)

X = monthly_expenses[['Month_Num']]
y = monthly_expenses['Amount']
model = LinearRegression()
model.fit(X, y)

future_months = pd.DataFrame({'Month_Num': range(len(monthly_expenses) + 1, len(monthly_expenses) + 7)})
forecast = model.predict(future_months)

fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    x=monthly_expenses['Month_Num'], y=monthly_expenses['Amount'],
    mode='lines', name='Historical', line=dict(color='#e74c3c')
))
fig5.add_trace(go.Scatter(
    x=future_months['Month_Num'], y=forecast,
    mode='lines+markers', name='Forecast',
    line=dict(color='#f39c12', dash='dash')
))
fig5.update_layout(
    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Month Number', yaxis_title='Expenses ($)'
)
st.plotly_chart(fig5, use_container_width=True)

st.divider()

# --- RAW DATA ---
st.subheader("Transaction Data")
st.dataframe(
    filtered[['Date', 'Category', 'Amount', 'Type']].sort_values('Date', ascending=False),
    use_container_width=True
)