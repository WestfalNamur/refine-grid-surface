import numpy as np


def grid_split_cells(cell_coords, incr):

    if cell_coords.shape[0] == 2:

        cell_00 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
        ])

        cell_01 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
        ])

        cell_10 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
        ])

        cell_11 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
        ])

        return np.hstack((
            cell_00,
            cell_01,
            cell_10,
            cell_11,
        ))

    if cell_coords.shape[0] == 3:

        cell_000 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
            cell_coords[2, :] - incr[2] / 4,
        ])
        cell_001 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
            cell_coords[2, :] + incr[2] / 4,
        ])
        cell_010 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
            cell_coords[2, :] - incr[2] / 4,
        ])
        cell_011 = np.array([
            cell_coords[0, :] - incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
            cell_coords[2, :] + incr[2] / 4,
        ])
        cell_100 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
            cell_coords[2, :] - incr[2] / 4,
        ])
        cell_101 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] - incr[1] / 4,
            cell_coords[2, :] + incr[2] / 4,
        ])
        cell_110 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
            cell_coords[2, :] - incr[2] / 4,
        ])
        cell_111 = np.array([
            cell_coords[0, :] + incr[0] / 4,
            cell_coords[1, :] + incr[1] / 4,
            cell_coords[2, :] + incr[2] / 4,
        ])

        return np.hstack((
            cell_000,
            cell_001,
            cell_010,
            cell_011,
            cell_100,
            cell_101,
            cell_110,
            cell_111,
        ))
