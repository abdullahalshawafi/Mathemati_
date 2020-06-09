from Equation import Expression              # import Expression in the interface
import math
import numpy
#func = input("enter the equation Y' with regarding python format: \n")
#fix = int(input("enter the fixing point"))
#print("now, enter the last given four points....")
#x = [0.0, 0.0, 0.0, 0.0]
#y = [0.0, 0.0, 0.0, 0.0]
#for i in range(4):
#    x[i] = float(input("enter X coordindate of the " + str(i) + " point: "))
#    y[i] = float(input("enter the Y coordinate of the " + str(i) + " point: "))

#des = float(input("enter the X coordinate of the desired point : "))
#nom = int(input("enter the number of iterations: "))
#stop = float(input("enter the stopping criteria (relative error) in percentage"))


def milne(func, fix, X, Y, des, nom, stop):
    expr = Expression(func, ["y", "x"])
    f = [0.0, 0.0, 0.0, 0.0, 0.0]
    yc = [0.0]                                                   # virtual array to put numbers of Yc in it
    h = X[1] - X[0]                                            # calculating thee step size
    for i in range(4):
        f[i] = round(expr(float(Y[i]), float(X[i])), fix)                # filling the F array
    yp = round(Y[0] + ((4 * h / 3) * (2 * f[3] - f[2] + 2 * f[1])), fix)    # Yp
    yC = yp                                                                # initial value of yc which is = Yp
    yc[0] = yC
    yclist = ["Yc(initial) = " + str(yp) ]            # this is Y corrected string
    # it is viewed as "at i = none, Yc(initial) = ..., at i = 0, Yc(0) = ..., etc,)
    # it is returned as the list of iterations
    for i in range(nom):
        yC = round(Y[2] + ((h / 3) * (f[2] + 4 * f[3] + 2 * expr(float(yC), float(des)))), fix)
        yc.append(yC)
        RE = abs(float(((yc[i] - yC) / yC) * 100))
        yclist.append("at i = " + str(i) + ", Yc(" + str(i) + ") = " + str(yC) + "   " + "Relative error = " + str(RE) + " %" )
        if(RE <= stop):
            break
    return  RE,yc[-1], yclist


