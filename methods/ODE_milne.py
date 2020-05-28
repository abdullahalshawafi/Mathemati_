from Equation import Expression              # import Expression in the interface
import math
import numpy
"""
func = input("enter the equation Y' with regarding python format: \n")
fix = int(input("enter the fixing point"))
print("now, enter the last given four points....")
for i in range(4):
    X[i] = float(input("enter X coordindate of the " + str(i) + " point: "))
    Y[i] = float(input("enter the Y coordinate of the " + str(i) + " point: "))

des = float(input("enter the X coordinate of the desired point : "))
nom = int(input("enter the number of iterations: "))
stop = float(input("enter the stopping criteria"))
exact = float(input("enter the exact value of Y"))
choice = int(input("enter your choice. 1 to get Yc in first iteration, 2 to get Yc after last iteration, 3 to get Yc after the stopping criteria: \n"))
"""
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

    return yp, YC, relative_error


#  example :
# [yps, ycs, re] = milne('y**2-x**2', 4, [0, 0.1, 0.2, 0.3], [1, 1.11, 1.25, 1.42], 0.4, '2', 2, 3, 1.75)
# print(str(yps)+" "+str(ycs)+" "+str(re))
