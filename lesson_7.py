# INTERACTIVE CHARTS ---------------------------------------------------------------------------------------------------

import plotly.graph_objects as go

# Define monthly sales data
months = ['January', 'February', 'March', 'April', 'May']
sales_2024 = [1500, 1800, 2200, 2100, 2400]
sales_2025 = [1700, 2000, 2500, 2600, 2800]

# Initialize the figure
fig = go.Figure()

# Add 2024 sales trace
fig.add_trace(go.Scatter(
    x=months,
    y=sales_2024,
    mode='lines+markers',
    name='Sales 2024',
    line=dict(color='royalblue', width=2),
    marker=dict(size=7)
))

# Add 2025 sales trace
fig.add_trace(go.Scatter(
    x=months,
    y=sales_2025,
    mode='lines+markers',
    name='Sales 2025',
    line=dict(color='darkorange', width=2),
    marker=dict(size=7)
))

# Update layout for full-page responsiveness
fig.update_layout(
    title=dict(
        text='Monthly Sales Comparison: 2024 vs 2025',
        x=0.5,
        xanchor='center',
        font=dict(size=22, family='Segoe UI', color='black')
    ),
    xaxis=dict(
        title='Month',
        tickmode='array',
        ticks='outside',
        showgrid=False,
        linecolor='black',
        mirror=True
    ),
    yaxis=dict(
        title='Sales (USD)',
        ticks='outside',
        showgrid=True,
        gridcolor='lightgray',
        zeroline=False,
        linecolor='black',
        mirror=True
    ),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=1.05,
        xanchor='center',
        x=0.5,
        font=dict(size=12)
    ),
    margin=dict(l=30, r=30, t=60, b=40),  # Minimal margins for full-page fit
    hovermode='x unified',
    template='plotly_white',
    autosize=True
)

# Show the full-page responsive chart
fig.show()