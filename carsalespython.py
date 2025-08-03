import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your Excel file
df = pd.read_excel('sample dataset.xlsx')

# Group data by Year and sum the Total_Revenue
revenue_by_year = df.groupby('Year')['Total_Revenue'].sum().reset_index()

# Set Seaborn style
sns.set(style="whitegrid")

# Create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=revenue_by_year, x='Year', y='Total_Revenue', marker='o', color='blue')

# Customize the plot
plt.title('Total Revenue by Year (Car Dealership)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Revenue (USD)', fontsize=12)
plt.xticks(revenue_by_year['Year'])
plt.tight_layout()

# Show the plot
plt.savefig('c:\Users\hp\Documents\GitHub\Car-dealership-sales/carsalespython.png')

plt.show()
