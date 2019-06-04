import plotly.graph_objs as go
import numpy as np


def create_grid_plot_traces(cell_coords, incr, color='black'):

    if cell_coords.shape[0] == 2:

        traces = []
        for i in range(cell_coords.shape[1]):

            x0 = cell_coords[0, i] - incr[0] / 2
            x1 = cell_coords[0, i] + incr[0] / 2
            y0 = cell_coords[1, i] - incr[1] / 2
            y1 = cell_coords[1, i] + incr[1] / 2

            xvals = np.array([x0, x0, x1, x1, x0])
            yvals = np.array([y0, y1, y1, y0, y0])

            trace = go.Scattergl(
                x=xvals,
                y=yvals,
                mode='lines',
                marker=dict(
                    color=color,
                ),
                showlegend=False,
            )

            traces.append(trace)

        return traces

    if cell_coords.shape[0] == 3:

        traces = []
        for i in range(cell_coords.shape[1]):

            x0 = cell_coords[0, i] - incr[0] / 2
            x1 = cell_coords[0, i] + incr[0] / 2
            y0 = cell_coords[1, i] - incr[1] / 2
            y1 = cell_coords[1, i] + incr[1] / 2
            z0 = cell_coords[2, i] - incr[2] / 2
            z1 = cell_coords[2, i] + incr[2] / 2

            xvals = np.array((
                x0, x1, x1, x1,
                x1, x1, x1, x0,
                x0, x0, x0, x0,
                x1, x1, x0, x0,
            ))
            yvals = np.array((
                y0, y0, y0, y0,
                y1, y1, y1, y1,
                y1, y1, y0, y0,
                y0, y1, y1, y0,
            ))
            zvals = np.array((
                z0, z0, z1, z0,
                z0, z1, z0, z0,
                z1, z0, z0, z1,
                z1, z1, z1, z1,
            ))

            trace = go.Scatter3d(
                x=xvals,
                y=yvals,
                z=zvals,
                mode='lines',
                marker=dict(
                    color=color
                ),
                showlegend=False,
            )

            traces.append(trace)

        return traces


def create_grid_plot_scatter(cell_coords):

    if cell_coords.shape[0] == 2:

        scalar = np.sqrt((cell_coords[0, :] ** 2 + cell_coords[1, :]**2))

        return [go.Scatter(
            x=cell_coords[0, :],
            y=cell_coords[1, :],
            mode='markers',
            marker=dict(
                color=scalar,
                colorscale='Viridis',
                showscale=True,
            )
        )]

    if cell_coords.shape[0] == 3:

        scalar = np.sqrt((
            cell_coords[0, :] ** 2
            + cell_coords[1, :] ** 2
            + cell_coords[2, :] ** 2
        ))

        return [go.Scatter3d(
            x=cell_coords[0, :],
            y=cell_coords[1, :],
            z=cell_coords[2, :],
            mode='markers',
            marker=dict(
                color=scalar,
                colorscale='Viridis',
                showscale=True,
            )
        )]
