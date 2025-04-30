# BOXPLOT --------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Simulate energy consumption data for 3 buildings over 100 days
np.random.seed(10)
energy_data = np.random.normal(loc=(30, 45, 38), scale=(5, 7, 6), size=(100, 3))

# Define pastel colors
colors = ['#FFECB3', '#C8E6C9', '#FFE0B2']  # pastel yellow, green, orange

# Create the plot with a better figure size
fig, ax = plt.subplots(figsize=(8, 5))

# Draw the box plot
positions = [2, 4, 6]
VP = ax.boxplot(energy_data, positions=positions, widths=1.5, patch_artist=True,
                showmeans=False, showfliers=True,
                medianprops={"color": "white", "linewidth": 0.5},
                whiskerprops={"color": "gray", "linewidth": 1.5},
                capprops={"color": "gray", "linewidth": 1.5},
                flierprops={"marker": "o", "color": "red", "markersize": 4, "alpha": 0.5})

# Apply pastel colors to each box
for patch, color in zip(VP['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor("white")
    patch.set_linewidth(0.5)

# Add labels, title, and grid
ax.set_title("Daily Energy Consumption by Building [kWh]", fontsize=14)
ax.set_xlabel("Building", fontsize=12)
ax.set_ylabel("Energy Consumption [kWh]", fontsize=12)
ax.set_xticks(positions)
ax.set_xticklabels(["Building A", "Building B", "Building C"])
ax.set_xlim(0, 8)
ax.set_ylim(10, 70)
ax.set_yticks(np.arange(10, 75, 10))
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('Graphs/boxplot.png', bbox_inches='tight')
plt.show()

# CARPET PLOT ----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.colors import LinearSegmentedColormap

# Set the seed for reproducibility
np.random.seed(42)

# Simulate hourly energy consumption for one year (365 days * 24 hours)
hours_per_year = 365 * 24
average_consumption = 1.2  # kWh per hour
std_dev = 0.3

# Generate normal consumption data
consumption = np.random.normal(loc=average_consumption, scale=std_dev, size=hours_per_year)

# Reshape into a 2D array: rows = days, columns = hours (365 x 24)
consumption_matrix = consumption.reshape(365, 24)

# Set low values for sleeping hours (00:00–08:00 and 22:00–00:00)
consumption_matrix[:, 0:8] = np.random.normal(loc=0.1, scale=0.05, size=(365, 8))
consumption_matrix[:, 22:24] = np.random.normal(loc=0.1, scale=0.05, size=(365, 2))

# Increase values slightly during morning activity (08:00–11:00)
consumption_matrix[:, 8:12] += np.random.normal(loc=0.5, scale=0.2, size=(365, 4))

# Flatten to introduce outliers
flat_data = consumption_matrix.flatten()
outlier_indices = np.random.choice(flat_data.shape[0], size=50, replace=False)
flat_data[outlier_indices] += np.random.uniform(2, 5, size=50)
consumption_matrix = flat_data.reshape(365, 24)

# Create a custom blue-green-red colormap
colors = ['#08306b', '#41ab5d', '#f03b20']  # blue, green, red
custom_cmap = LinearSegmentedColormap.from_list('BlueGreenRed', colors, N=256)

# Create the carpet plot
fig, ax = plt.subplots(figsize=(10, 6))
c = ax.imshow(consumption_matrix, aspect='auto', cmap=custom_cmap, interpolation='nearest')

# Add color bar
cbar = fig.colorbar(c, ax=ax)
cbar.set_label('Hourly Energy Consumption [kWh]', fontsize=12)

# Set labels and title
ax.set_title('Carpet Plot of Hourly Energy Consumption Over a Year', fontsize=14)
ax.set_xlabel('Hour of Day (0–23)', fontsize=12)
ax.set_ylabel('Day of Year (1–365)', fontsize=12)
ax.set_xticks(np.arange(0, 24, 3))
ax.set_yticks(np.linspace(0, 364, 12).astype(int))
ax.set_yticklabels([f'Month {i+1}' for i in range(12)])

plt.tight_layout()

# Save the plot
os.makedirs('Graphs', exist_ok=True)
plt.savefig('Graphs/carpet.png', bbox_inches='tight')
plt.show()