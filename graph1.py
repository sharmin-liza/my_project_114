import plotly.graph_objects as go
slope=5
x_values=list(range(11))
y_values=[x*slope for x in x_values]
data=go.Scatter(x=x_values,y=y_values,mode='lines' )

layout=go.Layout(title=f"Slope={slope}")
fig=go.Figure(data=[data],layout=layout)
fig.show()

