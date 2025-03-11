import matplotlib.pyplot as plt
import numpy as np
import os

# Sample data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_A_sales = [150, 200, 250, 300]
product_B_sales = [180, 220, 270, 320]
product_C_sales = [120, 160, 210, 260]

# Number of bars
bar_width = 0.25
x = np.arange(len(quarters))

# Create a directory for saving graphs if it doesn't exist
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')

# Create a figure
plt.figure(figsize=(12, 6))

# Poorly designed graph
plt.subplot(1, 2, 1)
plt.bar(x - bar_width, product_A_sales, width=bar_width, label='Product A', color='red', alpha=0.5)
plt.bar(x, product_B_sales, width=bar_width, label='Product B', color='orange', alpha=0.5)
plt.bar(x + bar_width, product_C_sales, width=bar_width, label='Product C', color='yellow', alpha=0.5)

# Title and labels for poorly designed graph
#plt.title('Poorly Designed Graph', fontsize=16)
plt.xticks(x, quarters, fontsize=12)
plt.ylim(0, 350)

# Adding grid lines behind the bars
plt.grid(axis='y', linestyle='-', alpha=1, zorder=0)

# Adding misleading elements (keeping them empty for clarity)
plt.text(0, 350, '', ha='center', color='black', fontsize=12)
plt.text(1, 350, '', ha='center', color='black', fontsize=12)
plt.text(2, 350, '', ha='center', color='black', fontsize=12)
plt.text(3, 350, '', ha='center', color='black', fontsize=12)

# ----------------------------------------------------------------------------------------------------------------------

# Well-designed graph
plt.subplot(1, 2, 2)
bars_A = plt.bar(x - bar_width, product_A_sales, width=bar_width, label='Product A', color='#4CAF50', edgecolor='black')
bars_B = plt.bar(x, product_B_sales, width=bar_width, label='Product B', color='#2196F3', edgecolor='black')
bars_C = plt.bar(x + bar_width, product_C_sales, width=bar_width, label='Product C', color='#FFC107', edgecolor='black')

# Title and labels for well-designed graph
#plt.title('Well-Designed Graph', fontsize=16, fontweight='bold')
plt.xlabel('Quarters', fontsize=14)
plt.ylabel('Sales [units]', fontsize=14)
plt.xticks(x, quarters, fontsize=12)
plt.ylim(0, 350)

# Adding grid lines behind the bars
plt.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)

# Adding data labels
for bars in [bars_A, bars_B, bars_C]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, str(yval), ha='center', fontsize=10, fontweight='bold')

# Adding a legend
plt.legend(loc='upper left', fontsize=12)

# Save the figure in the 'Graphs' directory
plt.savefig('Graphs/graph_comparison.png', bbox_inches='tight')

# Show the plots
plt.tight_layout()
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
