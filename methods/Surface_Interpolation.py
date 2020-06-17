import numpy as np
from math import isnan
from scipy.interpolate import griddata


def Plane_3P(P1, P2, P3):
    vec1 = np.zeros((3, 1))
    vec2 = np.zeros((3, 1))
    for i in range(3):
        vec1[i] = P1[i] - P2[i]
        vec2[i] = P3[i] - P2[i]
    coff = list(np.cross(vec1.transpose(), vec2.transpose()).transpose())

    coff.append(-1 * (P1[0] * coff[0] + P1[1] * coff[1] + P1[2] * coff[2]))
    return coff


def BiLinearInt():
    Po1 = np.array([[1, 1], [2, 6], [4, 10], [5, 9], [6, 4], [8, 2], [10, 12], [13, 24], [15, 30], [18, 18],
                       [20, 4], [23, 1], [24, 2], [25, 4]])
    Z = np.array([3, 6, 1, 6, 4, 6, 7, 14, 4, 10, 11, 10, 5, 7])
    n1 = len(Z)
    xmin = Po1[0][0]
    xmax = Po1[0][0]
    ymin = Po1[0][1]
    ymax = Po1[0][1]

    for i in range(1, n1):
        if Po1[i][0] < xmin:
            xmin = Po1[i][0]
        if Po1[i][0] > xmax:
            xmax = Po1[i][0]
        if Po1[i][1] < ymin:
            ymin = Po1[i][1]
        if Po1[i][1] > ymax:
            ymax = Po1[i][1]

    nx = 3
    ny = 5

    grid_x, grid_y = np.mgrid[xmin:xmax:((nx + 1) * 1j), ymin:ymax:((ny + 1) * 1j)]
    grid_x_out = np.mgrid[xmin:xmax:((nx + 1) * 1j)]
    grid_y_out = np.mgrid[ymin:ymax:((ny + 1) * 1j)]

    grid_z1 = griddata(Po1, Z, (grid_x, grid_y), method='linear')
    

    SurfaceCoff = np.empty((nx, ny, 4, 4))
    SurfaceCoff[:] = np.nan

    for i in range(nx):
        for j in range(ny):
            if not isnan(grid_z1[i][j]) and not isnan(grid_z1[i + 1][j + 1]):
                if not isnan(grid_z1[i][j + 1]):
                    SurfaceCoff[i][j][0] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                    [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                    [grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]])
                if not isnan(grid_z1[i + 1][j]):
                    SurfaceCoff[i][j][1] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                    [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                    [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]])
            elif not isnan(grid_z1[i + 1][j]) and not isnan(grid_z1[i][j + 1]):
                if not isnan(grid_z1[i][j]):
                    SurfaceCoff[i][j][2] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                    [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]],
                                                    [grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]])
                if not isnan(grid_z1[i + 1][j + 1]):
                    SurfaceCoff[i][j][3] = Plane_3P([grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]],
                                                    [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                    [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]])
    return SurfaceCoff, grid_x_out, grid_y_out, grid_z1


def GetPlane_of_P(SurfaceCoff, grid_x, grid_y, xn, yn):
    xcount = np.shape(grid_x)[0]
    ycount = np.shape(grid_y)[0]

    xmin = grid_x[0]
    xmax = grid_x[xcount - 1]
    ymin = grid_y[0]
    ymax = grid_y[ycount - 1]

    if xn < xmin and xn > xmax and yn < ymin and yn > ymax:
        return "out of bounds"

    xstep = (xmax - xmin) / (xcount - 1)
    ystep = (ymax - ymin) / (ycount - 1)

    xindex = int(np.trunc((xn - xmin) / xstep))
    yindex = int(np.trunc((yn - ymin) / ystep))

    planeindex = 2
    priorityindex = 2

    if not isnan(SurfaceCoff[xindex][yindex][0][0]) or not isnan(SurfaceCoff[xindex + 1][yindex + 1][1][0]):
        planeindex = 0
    elif not isnan(SurfaceCoff[xindex][yindex][2][0]) or not isnan(SurfaceCoff[xindex + 1][yindex + 1][3][0]):
        planeindex = 1

    if planeindex == 0:
        if (xn - xindex * xstep + xmin) / xstep > 0.5 and (yn - yindex * ystep + ymin) / ystep < 0.5:
            priorityindex = 1
        else:
            priorityindex = 0
    if planeindex == 1:
        if (xn - xindex * xstep + xmin) / xstep < 0.5 and (yn - yindex * ystep + ymin) / ystep < 0.5:
            priorityindex = 0
        else:
            priorityindex = 1

    if planeindex == 0 and isnan(SurfaceCoff[xindex][yindex][0][0]):
        priorityindex = 1
    if planeindex == 0 and isnan(SurfaceCoff[xindex][yindex][1][0]):
        priorityindex = 0
    if planeindex == 1 and isnan(SurfaceCoff[xindex][yindex][2][0]):
        priorityindex = 1
    if planeindex == 1 and isnan(SurfaceCoff[xindex][yindex][3][0]):
        priorityindex = 0

    if planeindex == 2:
        return "out of bounds"
    else:
        return SurfaceCoff[xindex][yindex][planeindex * 2 + priorityindex]



#OOP Design 
class Surface_Interpolation:

    def __init__(self,Points,Z):
        self.Points=Points
        self.Z=Z

    def Plane_3P(self,P1, P2, P3):
        vec1 = np.zeros((3, 1))
        vec2 = np.zeros((3, 1))
        for i in range(3):
            vec1[i] = P1[i] - P2[i]
            vec2[i] = P3[i] - P2[i]
        coff = list(np.cross(vec1.transpose(), vec2.transpose()).transpose())

        coff.append(-1 * (P1[0] * coff[0] + P1[1] * coff[1] + P1[2] * coff[2]))
        return coff
    
    def BiLinearInt(self):
        Po1 = self.Points
        Z = self.Z
        n1 = len(Z)
        xmin = Po1[0][0]
        xmax = Po1[0][0]
        ymin = Po1[0][1]
        ymax = Po1[0][1]

        for i in range(1, n1):
            if Po1[i][0] < xmin:
                xmin = Po1[i][0]
            if Po1[i][0] > xmax:
                xmax = Po1[i][0]
            if Po1[i][1] < ymin:
                ymin = Po1[i][1]
            if Po1[i][1] > ymax:
                ymax = Po1[i][1]

        nx = 40
        ny = 40

        grid_x, grid_y = np.mgrid[xmin:xmax:((nx + 1) * 1j), ymin:ymax:((ny + 1) * 1j)]
        grid_x_out = np.mgrid[xmin:xmax:((nx + 1) * 1j)]
        grid_y_out = np.mgrid[ymin:ymax:((ny + 1) * 1j)]

        grid_z1 = griddata(Po1, Z, (grid_x, grid_y), method='linear')
    

        SurfaceCoff = np.empty((nx, ny, 4, 4))
        SurfaceCoff[:] = np.nan

        for i in range(nx):
            for j in range(ny):
                if not isnan(grid_z1[i][j]) and not isnan(grid_z1[i + 1][j + 1]):
                    if not isnan(grid_z1[i][j + 1]):
                        SurfaceCoff[i][j][0] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                        [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                        [grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]])
                    if not isnan(grid_z1[i + 1][j]):
                        SurfaceCoff[i][j][1] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                        [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                        [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]])
                elif not isnan(grid_z1[i + 1][j]) and not isnan(grid_z1[i][j + 1]):
                    if not isnan(grid_z1[i][j]):
                        SurfaceCoff[i][j][2] = Plane_3P([grid_x[i][j], grid_y[i][j], grid_z1[i][j]],
                                                        [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]],
                                                        [grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]])
                if not isnan(grid_z1[i + 1][j + 1]):
                        SurfaceCoff[i][j][3] = Plane_3P([grid_x[i][j + 1], grid_y[i][j + 1], grid_z1[i][j + 1]],
                                                        [grid_x[i + 1][j + 1], grid_y[i + 1][j + 1], grid_z1[i + 1][j + 1]],
                                                        [grid_x[i + 1][j], grid_y[i + 1][j], grid_z1[i + 1][j]])
    
        return SurfaceCoff, grid_x_out, grid_y_out, grid_z1

    def GetPlane_of_P(self,xn,yn):
        SurfaceCoff, grid_x, grid_y,grid_z=self.BiLinearInt()
        xcount = np.shape(grid_x)[0]
        ycount = np.shape(grid_y)[0]

        xmin = grid_x[0]
        xmax = grid_x[xcount - 1]
        ymin = grid_y[0]
        ymax = grid_y[ycount - 1]

        if xn < xmin and xn > xmax and yn < ymin and yn > ymax:
            return "out of bounds"

        xstep = (xmax - xmin) / (xcount - 1)
        ystep = (ymax - ymin) / (ycount - 1)

        xindex = int(np.trunc((xn - xmin) / xstep))
        yindex = int(np.trunc((yn - ymin) / ystep))

        planeindex = 2
        priorityindex = 2

        if not isnan(SurfaceCoff[xindex][yindex][0][0]) or not isnan(SurfaceCoff[xindex + 1][yindex + 1][1][0]):
            planeindex = 0
        elif not isnan(SurfaceCoff[xindex][yindex][2][0]) or not isnan(SurfaceCoff[xindex + 1][yindex + 1][3][0]):
            planeindex = 1

        if planeindex == 0:
            if (xn - xindex * xstep + xmin) / xstep > 0.5 and (yn - yindex * ystep + ymin) / ystep < 0.5:
                priorityindex = 1
            else:
                priorityindex = 0
        if planeindex == 1:
            if (xn - xindex * xstep + xmin) / xstep < 0.5 and (yn - yindex * ystep + ymin) / ystep < 0.5:
                priorityindex = 0
            else:
                priorityindex = 1

        if planeindex == 0 and isnan(SurfaceCoff[xindex][yindex][0][0]):
            priorityindex = 1
        if planeindex == 0 and isnan(SurfaceCoff[xindex][yindex][1][0]):
            priorityindex = 0
        if planeindex == 1 and isnan(SurfaceCoff[xindex][yindex][2][0]):
            priorityindex = 1
        if planeindex == 1 and isnan(SurfaceCoff[xindex][yindex][3][0]):
            priorityindex = 0

        if planeindex == 2:
            return "out of bounds"
        else:
            return SurfaceCoff[xindex][yindex][planeindex * 2 + priorityindex]
    



def DEMO():
    Po1 = np.array([[1, 1], [2, 6], [4, 10], [5, 9], [6, 4], [8, 2], [10, 12], [13, 24], [15, 30], [18, 18],
                       [20, 4], [23, 1], [24, 2], [25, 4]])
    Z = np.array([3, 6, 1, 6, 4, 6, 7, 14, 4, 10, 11, 10, 5, 7])
    surf=Surface_Interpolation(Po1,Z)
    w=surf.GetPlane_of_P(1,1)
    print(w)

DEMO()