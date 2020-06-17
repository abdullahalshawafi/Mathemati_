# Python program to implement Runge Kutta method
# function to get the value of f(x,y)
import sympy

def functionOf(x, y, equ):
    X = sympy.symbols('x')
    Y = sympy.symbols('y')

    return sympy.sympify(equ).evalf(subs={X: x, Y: y})


# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h, equ):
    # Count number of iterations using step size or
    # step height h
    n = int((x - x0) / h)
    iterations = []
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * functionOf(x0, y, equ)
        k2 = h * functionOf(x0 + 0.5 * h, y + 0.5 * k1, equ)
        k3 = h * functionOf(x0 + 0.5 * h, y + 0.5 * k2, equ)
        k4 = h * functionOf(x0 + h, y + k3, equ)

        # Update next value of y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        iterations.append(y)

        # Update next value of x
        x0 = x0 + h
    return iterations


# Driver method
def Demo():
    equation = input("Enter The Equation ")
    x0 = 0
    y0 = 1
    x = 0.1
    h = 0.001
    print('The value of y at x is:', rungeKutta(x0, y0, x, h, equation)[-1])


#Demo()
