# Starter code for Python Data Visualization
# Use matplotlib or plotly to build charts and graphs.

# Sample dataset
months = ["January", "February", "March", "April", "May", "June"]
sales = [120, 150, 170, 130, 190, 220]
expenses = [80, 90, 100, 95, 110, 130]

# Example using matplotlib:

# import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 5))
# plt.plot(months, sales, marker='o', label='Sales')
# plt.plot(months, expenses, marker='s', label='Expenses')
# plt.title('Monthly Sales vs Expenses')
# plt.xlabel('Month')
# plt.ylabel('Amount ($)')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Example using plotly:

# import plotly.graph_objects as go

# fig = go.Figure()
# fig.add_trace(go.Bar(x=months, y=sales, name='Sales'))
# fig.add_trace(go.Bar(x=months, y=expenses, name='Expenses'))
# fig.update_layout(
#     title='Monthly Sales and Expenses',
#     xaxis_title='Month',
#     yaxis_title='Amount ($)',
#     barmode='group'
# )
# fig.show()

# You can change the chart type, add labels, and include a short analysis below.

def print_summary():
    total_sales = sum(sales)
    total_expenses = sum(expenses)
    print(f"Total sales: ${total_sales}")
    print(f"Total expenses: ${total_expenses}")
    print("Insight: Sales are increasing overall, and April has the lowest sales.")

if __name__ == '__main__':
    print_summary()
