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


def find_transition_cubes(
        xyz_cube_cntrs: Array[float, 3, ...],
        cube_incr: Array[int, float, 3],
        distance: int,):

    print('Currently interpolation and condtiotion are distsances, not gp!')

    node_000 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 2,
    ])
    node_001 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 2,
    ])
    node_010 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 2,
    ])
    node_011 = np.array([
        xyz_cube_cntrs[0, :] - cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 2,
    ])
    node_100 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 2,
    ])
    node_101 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] - cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 2,
    ])
    node_110 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] - cube_incr[2] / 2,
    ])
    node_111 = np.array([
        xyz_cube_cntrs[0, :] + cube_incr[0] / 2,
        xyz_cube_cntrs[1, :] + cube_incr[1] / 2,
        xyz_cube_cntrs[2, :] + cube_incr[2] / 2,
    ])

    node_stack = np.hstack((
        node_000,
        node_001,
        node_010,
        node_011,
        node_100,
        node_101,
        node_110,
        node_111,
    ))

    dist = np.sqrt(node_stack[0, :] ** 2
                   + node_stack[1, :] ** 2
                   + node_stack[2, :] ** 2)

    dist_bool = dist.astype(int) == distance

    dist_bool_rshp = np.reshape(dist_bool, (-1, 8))

    dist_bool_rshp_heterogeneous = ~(np.all(
        dist_bool_rshp == True, axis=1) | np.all(dist_bool_rshp == False, axis=1))

    print('node_stack', '\n',
          'shape: ', node_stack.shape, '\n',
          'axis0: xyz', '\n',
          'axis1: inner-recursion=cubes, outer-recursion=nodes')

    print('dist', '\n',
          'shape: ', dist.shape, '\n',
          'axis0: inner-recursion=cubes, outer-recursion=nodes')

    print('condtiotion: dist.astype(int) == distance')

    print('dist_bool_rshp', '\n',
          'shape: ', dist_bool_rshp.shape, '\n',
          'axis0: cubes', '\n',
          'axis1: nodes')

    print(np.reshape(dist, (-1, 8)).astype(int))

    print(dist_bool_rshp.astype(int))

    print(dist_bool_rshp_heterogeneous)
