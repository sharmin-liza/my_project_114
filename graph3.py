import plotly.graph_objects as go

# Define data
x_array = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
y_array = [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15]

# Define Data
data = go.Scatter(x=x_array, y=y_array, mode='markers')

# Define Layout
layout = go.Layout(
    xaxis=dict(range=[40, 160], title='Square Meters'),
    yaxis=dict(range=[5, 16], title='Price in Millions'),
    title='House Prices vs. Size'
)

# Create figure and plot
fig = go.Figure(data=[data], layout=layout)
fig.show()
