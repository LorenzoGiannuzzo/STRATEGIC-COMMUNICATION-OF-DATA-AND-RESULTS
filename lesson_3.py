# SORTING --------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'City': ['Chicago', 'Los Angeles', 'New York',  'Houston', 'Phoenix'],
    'Population': [2716000, 3980400,8419600, 2328000, 1680000]
}

df = pd.DataFrame(data)

# Sort by Population
df_sorted = df.sort_values(by='Population', ascending=False)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Before Sorting
ax[0].bar(df['City'], df['Population'], color='lightgray')
ax[0].set_title('Population of Cities (Before Sorting)', fontsize=16)
ax[0].set_xlabel('City', fontsize=14)
ax[0].set_ylabel('Population [millions]', fontsize=14)
ax[0].tick_params(axis='x', rotation=45)

# After Sorting
ax[1].bar(df_sorted['City'], df_sorted['Population'], color='skyblue')
ax[1].set_title('Population of Cities (After Sorting)', fontsize=16)
ax[1].set_xlabel('City', fontsize=14)
ax[1].set_ylabel('Population [millions]', fontsize=14)
ax[1].tick_params(axis='x', rotation=45)

plt.savefig('Graphs/sorting.png', bbox_inches='tight')

plt.tight_layout()
plt.show()

# AGGREGATION ----------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'State': ['California', 'Texas', 'Florida', 'New York', 'Illinois', 'California', 'Texas'],
    'City': ['Los Angeles', 'Houston', 'Miami', 'New York', 'Chicago', 'San Francisco', 'Dallas'],
    'Population': [3980400, 2328000, 4670000, 8419600, 2716000, 883305, 1340000]
}

df = pd.DataFrame(data)

# Aggregate population by State
df_agg = df.groupby('State')['Population'].sum().reset_index()

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Left: Non-Aggregated Values
df.plot(kind='bar', x='City', y='Population', ax=ax[0], color='lightblue', legend=False)
ax[0].set_title('Population of Cities (Non-Aggregated)', fontsize=16)
ax[0].set_xlabel('City', fontsize=14)
ax[0].set_ylabel('Population [millions]', fontsize=14)
ax[0].tick_params(axis='x', rotation=45)
ax[0].grid(axis='y', linestyle='--', alpha=0.3)

# Right: Aggregated Values
ax[1].bar(df_agg['State'], df_agg['Population'], color='lightgreen')
ax[1].set_title('Total Population by State (Aggregated)', fontsize=16)
ax[1].set_xlabel('State', fontsize=14)
ax[1].set_ylabel('Total Population [millions]', fontsize=14)
ax[1].tick_params(axis='x', rotation=45)
ax[1].grid(axis='y', linestyle='--', alpha=0.3)

# Adding population values on the bars for aggregated values
for index, value in enumerate(df_agg['Population']):
    ax[1].text(index, value, f'{value:,}', ha='center', va='bottom', fontsize=10)

plt.savefig('Graphs/aggregation.png', bbox_inches='tight')

plt.tight_layout()
plt.show()

# FILTERING ------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8419600, 3980400, 2716000, 2328000, 1680000]
}

df = pd.DataFrame(data)

# Filter cities with population greater than 3 million
df_filtered = df[df['Population'] > 3000000]

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Before Filtering
ax[0].bar(df['City'], df['Population'], color='lightblue')
ax[0].set_title('Population of Cities (Before Filtering)', fontsize=16)
ax[0].set_xlabel('City', fontsize=14)
ax[0].set_ylabel('Population [millions]', fontsize=14)
ax[0].tick_params(axis='x', rotation=45)

# After Filtering
# Create a color list for the bars
colors = ['salmon' if city in df_filtered['City'].values else 'lightgrey' for city in df['City']]
ax[1].bar(df['City'], df['Population'], color=colors)
ax[1].set_title('Cities with Population Greater than 3 Million (After Filtering)', fontsize=16)
ax[1].set_xlabel('City', fontsize=14)
ax[1].set_ylabel('Population [millions]', fontsize=14)
ax[1].tick_params(axis='x', rotation=45)

# Adding population values on the bars
for index, value in enumerate(df['Population']):
    ax[1].text(index, value, f'{value:,}', ha='center', va='bottom', fontsize=10)

plt.savefig('Graphs/filtering.png', bbox_inches='tight')

plt.tight_layout()
plt.show()

# JOIN/MERGE -----------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data for populations
data_population = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8419600, 3980400, 2716000, 2328000, 1680000]
}

# Sample data for areas
data_area = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Area (sq mi)': [302.6, 503, 227.3, 637.4, 517.6]
}

df_population = pd.DataFrame(data_population)
df_area = pd.DataFrame(data_area)

# Merge DataFrames
df_merged = pd.merge(df_population, df_area, on='City')

# Plotting
fig, ax1 = plt.subplots(figsize=(15, 6))

# Set bar width
bar_width = 0.35
index = np.arange(len(df_merged['City']))

# Bar plot for Population
bars1 = ax1.bar(index, df_merged['Population'], bar_width, color='lightblue', label='Population')

# Create a second y-axis for Area
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, df_merged['Area (sq mi)'], bar_width, color='gold', label='Area (sq mi)')

# Labels and title
ax1.set_xlabel('City', fontsize=14)
ax1.set_ylabel('Population [millions]', fontsize=14, )
ax2.set_ylabel('Area [sq miles]', fontsize=14, )
ax1.set_title('Population and Area of Cities', fontsize=16)

# Set x-ticks
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(df_merged['City'], rotation=45)

# Adding legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Adding grid lines
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)

plt.savefig('Graphs/merge.png', bbox_inches='tight')

plt.tight_layout()
plt.show()