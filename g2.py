for i in range(num_points):
    color='blue'
    if desired[i]:
        color='black'
    plotter.plot_point(x_points[i],y_points[i],color)

