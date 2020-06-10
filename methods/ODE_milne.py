import math
import numpy
from Equation import Expression  


def milne(func, fix, X, Y, des, nom, stop, exact):

    expr = Expression(func, ["y", "x"])

    F = [0.0, 0.0, 0.0, 0.0, 0.0]
    YC=[0.0]

    h = X[1] - X[0]

    for i in range(4):
        F[i] = round(expr(float(Y[i]), float(X[i])), fix)

    yp = round(Y[0] + ((4 * h / 3) * (2 * F[3] - F[2] + 2 * F[1])), fix)


    yc = yp
    YC[0] = yc

    for i in range(nom):
        bef = yc
        yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)
        sc = yc - bef
        YC.append(yc)
        if sc > (0.5 * (10 ** (2 - stop))) :
            break
        


    relative_error = float((exact - yc) * 100 / exact)
    relative_error=abs(relative_error)
    return yp, YC, relative_error

