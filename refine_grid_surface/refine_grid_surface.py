import numpy as np
import gempy as gp
from nptyping import Array


def split_cubes(xvals: Array[float], yvals: Array[float], zvals: Array[float]
                xincr: float, yincr: float, zincr: float)

    center_000 = np.array([xvals - xincr / 4,
                           yvals - yincr / 4,
                           xvals - zincr / 4]).T
    center_001 = np.array([xvals - xincr / 4,
                           yvals - yincr / 4,
                           xvals + zincr / 4]).T
    center_010 = np.array([xvals - xincr / 4,
                           yvals + yincr / 4,
                           xvals - zincr / 4]).T
    center_011 = np.array([xvals - xincr / 4,
                           yvals + yincr / 4,
                           xvals + zincr / 4]).T
    center_100 = np.array([xvals + xincr / 4,
                           yvals - yincr / 4,
                           xvals - zincr / 4]).T
    center_101 = np.array([xvals + xincr / 4,
                           yvals - yincr / 4,
                           xvals + zincr / 4]).T
    center_110 = np.array([xvals + xincr / 4,
                           yvals + yincr / 4,
                           xvals - zincr / 4]).T
    center_111 = np.array([xvals + xincr / 4,
                           yvals + yincr / 4,
                           xvals + zincr / 4]).T

    center_stack = np.concatenate((center_000,
                                   center_001,
                                   center_010,
                                   center_011,
                                   center_100,
                                   center_101,
                                   center_110,
                                   center_111))

    return center_stack


# def fing_surface(xvals: Array[float], yvals: Array[float], zvals: Array[float]
#                 xincr: float, yincr: float, zincr: float, lithology: int,
#                 interp_data)
#
#
#    nodes_000 = np.array([xvals - xincr / 2,
#                          yvals - yincr / 2,
#                          xvals - zincr / 2]).T
#    nodes_001 = np.array([xvals - xincr / 2,
#                          yvals - yincr / 2,
#                          xvals + zincr / 2]).T
#    nodes_010 = np.array([xvals - xincr / 2,
#                          yvals + yincr / 2,
#                          xvals - zincr / 2]).T
#    nodes_011 = np.array([xvals - xincr / 2,
#                          yvals + yincr / 2,
#                          xvals + zincr / 2]).T
#    nodes_100 = np.array([xvals + xincr / 2,
#                          yvals - yincr / 2,
#                          xvals - zincr / 2]).T
#    nodes_101 = np.array([xvals + xincr / 2,
#                          yvals - yincr / 2,
#                          xvals + zincr / 2]).T
#    nodes_110 = np.array([xvals + xincr / 2,
#                          yvals + yincr / 2,
#                          xvals - zincr / 2]).T
#    nodes_111 = np.array([xvals + xincr / 2,
#                          yvals + yincr / 2,
#                          xvals + zincr / 2]).T
#
#
#    nodes_stack = np.concatenate((nodes_000,
#                                  nodes_001,
#                                  nodes_010,
#                                  nodes_011,
#                                  nodes_100,
#                                  nodes_101,
#                                  nodes_110,
#                                  nodes_111))
