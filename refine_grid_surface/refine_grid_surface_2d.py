import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


def create_sqrs_cntr_trace(xy_coor, xy_incr):

    if xy_coor.shape[0] != 2:
        print('xy must be shape(2,-1)')

    if len(xy_coor.shape) != 2:
        print('xy_coor must be 2 dimensional')

    return go.Scattergl(
        x=xy_coor[0, :],
        y=xy_coor[1, :],
        mode='markers',
        marker=dict(
            color='red',
            line=dict(width=1)
        ),
        showlegend=False,
    )


def creat_sqr_traces(xy_coor, xy_incr):

    traces = []

    for i in range(xy_coor.shape[1]):

        x_0 = xy_coor[0, i] - xy_incr[0] / 2
        x_1 = xy_coor[0, i] + xy_incr[0] / 2
        y_0 = xy_coor[1, i] - xy_incr[1] / 2
        y_1 = xy_coor[1, i] + xy_incr[1] / 2

        xcoor = np.array([x_0, x_0, x_1, x_1, x_0])
        ycoor = np.array([y_0, y_1, y_1, y_0, y_0])

        trace = go.Scattergl(
            x=xcoor,
            y=ycoor,
            marker=dict(
                color='black',
            ),
            showlegend=False,
        )

        traces.append(trace)

    return traces


def split_sqrs(xy_coor, xy_incr):

    if xy_coor.shape[0] != 2:
        print('xy must be shape(2,-1)')

    if len(xy_coor.shape) != 2:
        print('xy_coor must be 2 dimensional')

    sqrs_00 = np.array([
        xy_coor[0, :] - xy_incr[0] / 4,
        xy_coor[1, :] - xy_incr[1] / 4,
    ])

    sqrs_01 = np.array([
        xy_coor[0, :] - xy_incr[0] / 4,
        xy_coor[1, :] + xy_incr[1] / 4,
    ])

    sqrs_10 = np.array([
        xy_coor[0, :] + xy_incr[0] / 4,
        xy_coor[1, :] - xy_incr[1] / 4,
    ])

    sqrs_11 = np.array([
        xy_coor[0, :] + xy_incr[0] / 4,
        xy_coor[1, :] + xy_incr[1] / 4,
    ])

    if sqrs_00.shape != xy_coor.shape:
        print('sqrss_ij should be of same shape as xy_coor')
        print()

    return np.hstack((sqrs_00, sqrs_01, sqrs_10, sqrs_11))
