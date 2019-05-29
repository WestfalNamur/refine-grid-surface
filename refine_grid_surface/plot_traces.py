from nptyping import Array
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


def create_cube_trace_3D(
        xyz_cube_cntr: Array[int, float, 3],
        cube_incr: Array[int, float, 3]):

    x0 = xyz_cube_cntr[0] - cube_incr[0] / 2
    x1 = xyz_cube_cntr[0] + cube_incr[0] / 2
    y0 = xyz_cube_cntr[1] - cube_incr[1] / 2
    y1 = xyz_cube_cntr[1] + cube_incr[1] / 2
    z0 = xyz_cube_cntr[2] - cube_incr[2] / 2
    z1 = xyz_cube_cntr[2] + cube_incr[2] / 2

    xcoo = np.stack((
        x0, x1, x1, x1,
        x1, x1, x1, x0,
        x0, x0, x0, x0,
        x1, x1, x0, x0,
    ))
    ycoo = np.stack((
        y0, y0, y0, y0,
        y1, y1, y1, y1,
        y1, y1, y0, y0,
        y0, y1, y1, y0,
    ))
    zcoo = np.stack((
        z0, z0, z1, z0,
        z0, z1, z0, z0,
        z1, z0, z0, z1,
        z1, z1, z1, z1,
    ))

    return go.Scatter3d(
        x=xcoo.reshape(-1),
        y=ycoo.reshape(-1),
        z=zcoo.reshape(-1),
        mode='lines',
        marker=dict(
            color='black'
        )
    )


def create_cube_traces_3D(
        xyz_cube_cntrs: Array[float, 3, ...],
        cube_incr: Array[float, 3]):

    cube_traces = []

    for i in range(xyz_cube_cntrs.shape[1]):

        cube_trace = create_cube_trace_3D(
            xyz_cube_cntr=xyz_cube_cntrs[:, i],
            cube_incr=cube_incr,
        )
        cube_traces.append(cube_trace)

    return cube_traces
