import plotly.graph_objects as go
slope=45
intercept=7
x_values=list(range(11))
y_values=[x*slope + intercept for x in x_values]
data=go.Scatter(x=x_values, y=y_values, mode='lines')
layout=go.Layout(title=f"Slope={slope} intercept={intercept}")
fig=go.Figure(data=[data],layout=layout)
fig.show()
