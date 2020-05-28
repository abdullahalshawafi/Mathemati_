# Equations are entered after speration

from sympy import *
from decimal import *

# choose ==2 -------> if u solve 2 eq
# choose==3 --------> if u solve 3 eq

x, y, z = symbols('x y z')


def FixedPointIteration(choose, max_iteration, error, str_eq1, str_eq2, xo, yo, str_eq3=" ", zo=" "):
    x, y, z = symbols('x y z')
    Iteration_Error = []
    x_sol = []
    y_sol = []
    z_sol = []
    if choose == "2":

        eq1 = sympify(str_eq1)
        eq2 = sympify(str_eq2)

        x_new = xo
        y_new = yo

        i = 1
        while i <= int(max_iteration):
            xold = x_new

            x_new = eq1.evalf(subs={x: x_new, y: y_new}, n=6)
            y_new = eq2.evalf(subs={x: x_new, y: y_new}, n=6)

            x_sol.append(round(x_new, 4))
            y_sol.append(round(y_new, 4))
            e = ((abs(float(x_new) - float(xold))) / float(xold)) * 100
            Iteration_Error.append(round(e, 4))
            if e < float(error):
                break
            i += 1

    elif choose == "3":

        eq1 = sympify(str_eq1)
        eq2 = sympify(str_eq2)
        eq3 = sympify(str_eq3)

        x_new = xo
        y_new = yo
        z_new = zo

        i = 1
        while i <= int(max_iteration):
            xold = x_new
            x_new = eq1.evalf(subs={x: x_new, y: y_new, z: z_new}, n=6)
            y_new = eq2.evalf(subs={x: x_new, y: y_new, z: z_new}, n=6)
            z_new = eq3.evalf(subs={x: x_new, y: y_new, z: z_new}, n=6)
            x_sol.append(round(x_new, 4))
            y_sol.append(round(y_new, 4))
            z_sol.append(round(z_new, 4))
            e = ((abs(float(x_new) - float(xold))) / float(xold)) * 100
            Iteration_Error.append(round(e, 4))
            if e < float(error):
                break
            i += 1

    return x_sol, y_sol, z_sol, Iteration_Error

# Test
# u, w, m ,i= FixedPointIteration("2", "10", "0.005", .1 * x ** 2 + .1 * y ** 2 + .8, .8 + .1 * x + .1 * x * y ** 2, .5, .5)
# print(u)
# print(w)
# print(i)
# print(m)
