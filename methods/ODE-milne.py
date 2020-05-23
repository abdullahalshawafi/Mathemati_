from Equation import Expression
import math
import numpy
flag = True
while(flag == True):
    try:
        func = input("enter function Y' (with regarding python syntax) : ").lower()
        expr = Expression(func, ["y", "x"])

        fix = int(input("enter fixing decimals: "))  # We only need 4 points, the fifth one for the desired point
        X = [0.0, 0.0, 0.0, 0.0, 0.0]
        Y = [0.0, 0.0, 0.0, 0.0, 0.0]
        F = [0.0, 0.0, 0.0, 0.0, 0.0]

        for i in range(4):
            X[i] = float(input(f"enter X[{i}]: "))
            Y[i] = float(input(f"enter Y[{i}]: "))

        des = float(input("enter desired point: "))
        h = X[1] - X[0]

        for i in range(4):
            F[i] = round(expr(float(Y[i]), float(X[i])), fix)

        yp = round(Y[0] + ((4 * h / 3) * (2 * F[3] - F[2] + 2 * F[1])), fix)

        print(f"Y predicted = {yp} \n")
        yc = yp

        choice = input("enter :\n(1) for Ycorrected in first iteration \n(2) for iterations \n(3) for stopping criteria \n(4) for relative error\n")
        if choice == '1':
            yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)

        elif choice == '2':
            nom = int(input("enter number of iterations: "))
            for i in range(nom):
                yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)
                print(f"Y corrected({i}) = {yc}")

        elif choice == '3':
            stop = int(input("enter stopping criteria significant figures: "))
            bef = yc
            yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)
            sc = yc - bef
            i = 0
            while sc > (0.5 * (10 ** (2 - stop))):
                bef = yc
                print(f"Y corrected({i}) = {yc}")
                i += 1
                yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)
                sc = yc - bef

        elif choice == '4':
            exact = float(input("enter exact value: "))
            #    i = 0
            yc = round(Y[2] + ((h / 3) * (F[2] + 4 * F[3] + 2 * expr(float(yc), float(des)))), fix)
            relative_error = float((exact - yc) * 100 / exact)
            print("Relative error = ")
            print(relative_error, '%')

        print(f"final answer Ycorrected = {yc}")
        flag = False
    except:
        print("error, enter the function Y' in its correct syntax...\n")


