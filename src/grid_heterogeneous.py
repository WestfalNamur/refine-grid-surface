import numpy as np


def find_heterogeneous_cells(cell_coords, incr, condition):

    if cell_coords.shape[0] == 2:

        n_cells = cell_coords.shape[1]

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

        boolean_reshaped = np.reshape(boolean, (n_cells, 4))

        return ~(
            np.all(boolean_reshaped == True, axis=1)
            | np.all(boolean_reshaped == False, axis=1)
        )
