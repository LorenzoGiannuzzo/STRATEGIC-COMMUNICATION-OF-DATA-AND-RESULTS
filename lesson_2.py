
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import pandas as pd

# Load the US states shapefile directly from the URL
url = 'https://github.com/PublicaMundi/MappingAPI/raw/master/data/geojson/us-states.json'
us_states = gpd.read_file(url)

# Sample population data for each state (in millions)
population_data = {
    'Alabama': 4.9,
    'Alaska': 0.7,
    'Arizona': 7.3,
    'Arkansas': 3.0,
    'California': 39.5,
    'Colorado': 5.8,
    'Connecticut': 3.6,
    'Delaware': 0.9,
    'Florida': 21.5,
    'Georgia': 10.7,
    'Hawaii': 1.4,
    'Idaho': 1.8,
    'Illinois': 12.8,
    'Indiana': 6.7,
    'Iowa': 3.2,
    'Kansas': 2.9,
    'Kentucky': 4.5,
    'Louisiana': 4.6,
    'Maine': 1.3,
    'Maryland': 6.0,
    'Massachusetts': 6.9,
    'Michigan': 10.0,
    'Minnesota': 5.6,
    'Mississippi': 2.9,
    'Missouri': 6.1,
    'Montana': 1.1,
    'Nebraska': 1.9,
    'Nevada': 3.1,
    'New Hampshire': 1.4,
    'New Jersey': 8.9,
    'New Mexico': 2.1,
    'New York': 19.3,
    'North Carolina': 10.5,
    'North Dakota': 0.8,
    'Ohio': 11.7,
    'Oklahoma': 4.0,
    'Oregon': 4.2,
    'Pennsylvania': 12.8,
    'Rhode Island': 1.1,
    'South Carolina': 5.1,
    'South Dakota': 0.9,
    'Tennessee': 6.8,
    'Texas': 29.1,
    'Utah': 3.3,
    'Vermont': 0.6,
    'Virginia': 8.5,
    'Washington': 7.6,
    'West Virginia': 1.8,
    'Wisconsin': 5.8,
    'Wyoming': 0.6
}

# Convert the population data to a DataFrame
population_df = pd.DataFrame(list(population_data.items()), columns=['name', 'population'])

# Merge the population data with the GeoDataFrame
us_states = us_states.merge(population_df, on='name')

# Create a directory for saving graphs if it doesn't exist
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the US states map with a pink color map based on population
us_states.boundary.plot(ax=ax, linewidth=1, color='black')  # Draw state boundaries
cmap = 'Blues'  # Pink color map
us_states.plot(column='population', ax=ax, legend=True,
               cmap=cmap,
               missing_kwds={'color': 'lightgray', 'label': 'Missing values'},
               legend_kwds={'label': "Population by State (in millions)",
                            'orientation': "horizontal",
                            'shrink': 0.5})  # Reduce legend bar size

# Add title
plt.title('Map of US States Colored by Population', fontsize=20)

# Remove latitude and longitude axes
ax.set_axis_off()

# Save the figure in the 'Graphs' directory
plt.savefig('Graphs/us_states_population_map.png', bbox_inches='tight')

# Show the plot
plt.tight_layout()
plt.show()