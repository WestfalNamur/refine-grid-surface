import numpy as np
from nptyping import Array


def split_cubes(
        xyz_cube_cntrs: Array[float, 3, ...],
        cube_incr: Array[int, float, 3]):

    center_000 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 4,
    ])
    center_001 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 4,
    ])
    center_010 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 4,
    ])
    center_011 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 4,
    ])
    center_100 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 4,
    ])
    center_101 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 4,
    ])
    center_110 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 4,
    ])
    center_111 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 4,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 4,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 4,
    ])

    return np.hstack((
        center_000,
        center_001,
        center_010,
        center_011,
        center_100,
        center_101,
        center_110,
        center_111,
    ))
