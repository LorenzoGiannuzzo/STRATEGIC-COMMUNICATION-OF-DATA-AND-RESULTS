# LINEPLOT -------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Generate data
x = np.linspace(0, 10, 100)
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 10, 25)
y2 = 4 + 1 * np.sin(2 * x2)

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# Plot data
ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2, label='Sample Points')
ax.plot(x, y, linewidth=2.0, label='Sine Wave')
ax.plot(x2, y2 - 2.5, 'o-', linewidth=2, label='Another Sample')

# Set limits and ticks
ax.set(xlim=(0, 10), ylim=(-2, 8))
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 9, 1))

# Hide the tick labels
ax.set_xticks([])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labels

plt.title('Line Plot of Sine Function')
plt.legend()
plt.tight_layout()
plt.savefig('Graphs/lineplot.png', bbox_inches='tight')
plt.show()


# SCATTER PLOT ---------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Generate data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# Scatter plot
scatter = ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100, alpha=0.6)

# Set limits and ticks
ax.set(xlim=(0, 8), ylim=(0, 8))
ax.set_xticks(np.arange(0, 9, 1))
ax.set_yticks(np.arange(0, 9, 1))

# Hide the tick labels
ax.set_xticks([])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labels

plt.title('Scatter Plot of Random Data')
plt.colorbar(scatter, label='Color Scale')
plt.tight_layout()
plt.savefig('Graphs/scatterplot.png', bbox_inches='tight')
plt.show()


# HIST2D ---------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# Generate data
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# 2D histogram
hist = ax.hist2d(x, y, bins=(30, 30), cmap='Greens')

# Set limits
ax.set(xlim=(-3, 3), ylim=(-3, 3))

# Hide the tick labels
ax.set_xticks([])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labels

plt.title('2D Histogram of Correlated Data')
plt.colorbar(hist[3], label='Counts')
plt.tight_layout()
plt.savefig('Graphs/hist2d.png', bbox_inches='tight')
plt.show()

# STACK PLOT -----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Generate data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# Stack plot
ax.stackplot(x, y, labels=['Group A', 'Group B', 'Group C'])

# Set limits and ticks
ax.set(xlim=(0, 10), ylim=(0, 5))
ax.set_xticks(np.arange(0, 11, 2))
ax.set_yticks(np.arange(0, 6, 1))

# Hide the tick labels
ax.set_xticks([])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labels

plt.title('Stack Plot of Group Data')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Graphs/stackplot.png', bbox_inches='tight')
plt.show()


# HEXBIN ---------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# Generate data
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# Hexbin plot
hb = ax.hexbin(x, y, gridsize=30, cmap="Oranges")

# Set limits
ax.set(xlim=(-3, 3), ylim=(-3, 3))

# Hide the tick labels
ax.set_xticks([])  # Remove x-axis tick labels
ax.set_yticks([])  # Remove y-axis tick labels

plt.title('Hexbin Plot of Correlated Data')
plt.colorbar(hb, label='Counts')
plt.tight_layout()
plt.savefig('Graphs/hexbin.png', bbox_inches='tight')
plt.show()

# TRIP COLOR -----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# Generate data
np.random.seed(1)
x = np.random.uniform(-3, 3, 256)
y = np.random.uniform(-3, 3, 256)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# Create the plot with a specific figure size
fig, ax = plt.subplots(figsize=(8, 4))  # Width: 8, Height: 4

# Scatter plot of points
ax.plot(x, y, 'o', markersize=2, color='grey', label='Data Points')

# Triangular color plot
tri = ax.tripcolor(x, y, z, shading='gouraud', cmap='viridis')

# Set limits
ax.set(xlim=(-3, 3), ylim=(-3, 3))

# Add a colorbar to indicate the scale of z values
plt.colorbar(tri, ax=ax, label='Function Value')

# Title and labels
plt.title('Triangular Color Plot of Function Values')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.savefig('Graphs/triangular_color_plot.png', bbox_inches='tight')
plt.show()

# LINE PLOT EXAMPLE ----------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create synthetic data for monthly energy consumption (in kWh) for multiple households
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
household_1 = [320, 280, 300, 350, 400, 450, 500, 480, 420, 380, 340, 310]
household_2 = [290, 310, 330, 370, 390, 430, 460, 490, 410, 360, 330, 300]
household_3 = [350, 300, 320, 360, 410, 440, 480, 500, 430, 390, 360, 340]

# Create a DataFrame
data = pd.DataFrame({
    'Month': months,
    'Household 1': household_1,
    'Household 2': household_2,
    'Household 3': household_3
})

# Create a color palette from orange to violet
colors = sns.color_palette("magma", n_colors=len(data.columns) - 1)

# Create the line plot
plt.figure(figsize=(12, 6))
for i, household in enumerate(data.columns[1:]):
    sns.lineplot(data=data, x='Month', y=household, marker='o', color=colors[i], linewidth=2.5, label=household)

# Add titles and labels with units
plt.title('Monthly Energy Consumption of Households (2023)', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Energy Consumption [kWh]', fontsize=14)

# Add gridlines for better readability
plt.grid(True)

# Set x-ticks for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend(title='Households', fontsize=12)

# Tight layout for better spacing
plt.tight_layout()

# Save the figure
plt.savefig('Graphs/monthly_energy_consumption_multiple_households.png', bbox_inches='tight')

# Show the plot
plt.show()

# SCATTER PLOT EXAMPLE -------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create synthetic data
np.random.seed(42)  # For reproducibility
months = np.tile(np.arange(1, 13), 5)  # Repeat months for 5 years
average_temperature = np.random.uniform(5, 30, size=len(months))  # Average temperature in degrees Celsius
energy_consumption = average_temperature * 15 + np.random.normal(0, 10, size=len(months))  # Energy consumption in kWh

# Create a DataFrame
data = pd.DataFrame({
    'Month': months,
    'Average Temperature (°C)': average_temperature,
    'Energy Consumption (kWh)': energy_consumption
})

# Create the scatter plot
plt.figure(figsize=(12, 6))
scatter = plt.scatter(data['Average Temperature (°C)'],
                      data['Energy Consumption (kWh)'],
                      c=data['Month'],
                      cmap='viridis',
                      s=100,
                      alpha=0.7,
                      edgecolor='w')

# Add titles and labels with units
plt.title('Energy Consumption vs. Average Temperature', fontsize=18)
plt.xlabel('Average Temperature [°C]', fontsize=14)
plt.ylabel('Energy Consumption [kWh]', fontsize=14)

# Create a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Month', fontsize=12)

# Show the plot
plt.tight_layout()
plt.savefig('Graphs/energy_consumption_vs_temperature.png', bbox_inches='tight')
plt.show()
