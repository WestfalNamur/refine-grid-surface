import numpy as np


def find_heterogeneous_cells(cell_coords, incr, condition):

    n_cells = cell_coords.shape[1]

    if cell_coords.shape[0] == 2:

        node_00 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
        ])

        node_01 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
        ])

        node_10 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
        ])

        node_11 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
        ])

        node_stack = np.hstack((
            node_00,
            node_01,
            node_10,
            node_11,
        ))

        scalar = np.sqrt((node_stack[0, :] ** 2 + node_stack[1, :]**2))

        boolean = scalar.astype(int) == condition

        return (
            ~(np.all(boolean.reshape(4, n_cells) == True, axis=0)
                | np.all(boolean.reshape(4, n_cells) == False, axis=0)),
            np.all(boolean.reshape(4, n_cells) == True, axis=0),
        )

    if cell_coords.shape[0] == 3:

        node_000 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
            cell_coords[2, :] - incr[2] / 2,
        ])

        node_001 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
            cell_coords[2, :] + incr[2] / 2,
        ])

        node_010 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
            cell_coords[2, :] - incr[2] / 2,
        ])

        node_011 = np.array([
            cell_coords[0, :] - incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
            cell_coords[2, :] + incr[2] / 2,
        ])

        node_100 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
            cell_coords[2, :] - incr[2] / 2,
        ])

        node_101 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] - incr[1] / 2,
            cell_coords[2, :] + incr[2] / 2,
        ])

        node_110 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
            cell_coords[2, :] - incr[2] / 2,
        ])

        node_111 = np.array([
            cell_coords[0, :] + incr[0] / 2,
            cell_coords[1, :] + incr[1] / 2,
            cell_coords[2, :] + incr[2] / 2,
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

        scalar = np.sqrt((
            node_stack[0, :] ** 2
            + node_stack[1, :] ** 2
            + node_stack[2, :] ** 2
        ))

        boolean = scalar.astype(int) == condition

        return (
            ~(np.all(boolean.reshape(8, n_cells) == True, axis=0)
                | np.all(boolean.reshape(8, n_cells) == False, axis=0)),
            np.all(boolean.reshape(8, n_cells) == True, axis=0),
        )
