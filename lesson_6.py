import plotly.express as px
import pandas as pd

# Example dataset: average residential energy consumption (fictional values)
data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Energy_Consumption_kWh': [5700, 8300, 4600, 6900, 6100]
}

df = pd.DataFrame(data)

# Use state abbreviations to match map locations
state_abbrev = {
    'California': 'CA', 'Texas': 'TX', 'New York': 'NY',
    'Florida': 'FL', 'Illinois': 'IL'
}
df['State_Code'] = df['State'].map(state_abbrev)

# Create choropleth map
fig = px.choropleth(
    df,
    locations='State_Code',
    locationmode='USA-states',
    color='Energy_Consumption_kWh',
    scope='usa',
    color_continuous_scale='YlOrRd',
    labels={'Energy_Consumption_kWh': 'Avg kWh'},
    title='Average Residential Energy Consumption by State'
)

fig.show()

# SANKEY DIAGRAM -------------------------------------------------------------------------------------------------------

import plotly.graph_objects as go

# Nodes: Funding Sources → Departments → Projects
labels = [
    "Total Budget",         # 0
    "R&D", "Marketing", "Operations",  # 1-3
    "AI Project", "Product Dev",       # 4-5
    "Ads", "Events",                   # 6-7
    "Manufacturing", "Logistics"      # 8-9
]

# Links (source → target)
sources = [0, 0, 0,         1, 1,       2, 2,       3, 3]
targets = [1, 2, 3,         4, 5,       6, 7,       8, 9]
values  = [100, 80, 120,    60, 40,     50, 30,     70, 50]

# Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=["#8dd3c7", "#80b1d3", "#fdb462", "#fb8072",
               "#bebada", "#b3de69", "#fccde5", "#d9d9d9", "#bc80bd", "#ccebc5"]
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=["rgba(140,211,199,0.5)"]*3 +
              ["rgba(128,177,211,0.5)"]*2 +
              ["rgba(253,180,98,0.5)"]*2 +
              ["rgba(251,128,114,0.5)"]*2
    )
)])

fig.update_layout(
    title_text="Company Budget Allocation Flow",
    font=dict(size=13),
    height=500,
    margin=dict(l=30, r=30, t=40, b=20)
)

fig.show()