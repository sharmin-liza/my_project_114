import plotly.graph_objects as go
x_values=list(range(11))
y_values=x_values
data=go.Scatter(x=x_values, y=y_values, mode='lines')
layout=go.Layout(title='y=x')
fig=go.Figure(data=[data],layout=layout)
fig.show()

