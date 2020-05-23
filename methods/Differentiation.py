from sympy import *
# import numpy as np
import math
import sys
#############################################EXTRAPOLATION#############################################

def Extrapolation(list ,ord,table) :
   counter = int(ord / 2 - 1)
   k = 2
   if (table == False):
       ######For Formula#####
    while (k < ord / 2 + 1):
        for v in range(counter):
            list[v] = (pow(4, k - 1) * list[v] - list[v + 1]) / (
                    pow(4, k - 1) - 1)  # Calculates the extrapolation using the general formula
            # print(RichardList_func) #Reserved for debugging
        k = k + 1
        counter = counter - 1
    print('Final Answer =', list[0])
    ######For Table#####
   else :
       while (k < ord / 2 + 1):
           for v in range(counter):
               RichardList[0][v] = (pow(4, k - 1) * list[0][v] - list[0][v + 1]) / (
                       pow(4, k - 1) - 1)# Calculates the extrapolation using the general formula
           k = k + 1
       print('Final Answer =',list[0][0])


#################################################DERIVATIVE FOR TABLE#################################################
# Pretty much the same as "derivativeForFunction" but here we already have the points and their values
def derivativeForTable(h, x, method, mat, order):
    m = mat[0].index(x)  # to get index of X(i)
    try:
        w = mat[0].index(round(x + h, 1))  # to get index of X(i+1)
        z = mat[0].index(round(x - h, 1))  # to get index of X(i-1)

    except ValueError:
        sys.stdout.flush()
        print('Cannot apply the central difference formula, aborting...')
        input('Press any key to abort...')
        quit()

        # Failed attempt at making the program more flexible
        # next2_index = mat[0].index(round(x+2*h,2))
        # if method == '1':
        # The other methods have an error of h^2
        # This one has an error of h
        # So we must compensate in the order
        # order = order**2
        # return ((4*mat[1][w] - 3* mat[1][m] - mat[1][next2_index]) / 2*h )

    if method == '1':
        return (mat[1][w] - mat[1][z]) / (2 * h)
    elif method == '2':
        return (mat[1][w] - 2 * mat[1][m] + mat[1][z]) / (pow(h, 2))
    elif method == '3':
        l = mat[0].index(round(x + (2 * h)), 5)  # to get index of X(i+2)
        g = mat[0].index(round(x - (2 * h)), 5)  # to get index of X(i-2)
        return (-mat[1][g] + 2 * mat[1][z] - 2 * mat[1][w] + mat[1][l]) / (2 * pow(h, 3))


#################################################DERIVATIVE FOR FUNCTION#################################################
def derivativeForFunction(h, x, method, formula):
    w = formula.subs({'x': float(x + h)}).evalf()  # to get index of X(i+1)
    z = formula.subs({'x': float(x - h)}).evalf()  # to get index of X(i-1)
    m = formula.subs({'x': x}).evalf()  # to get index of X(i)

    if method == '1':
        return (w - z) / (
                    2 * h)  # Uses the centeral difference formula to obtain the first derivative (f'(x) = [f(x+h) - f(x-h)]/2h

    elif method == '2':
        return (w - 2 * m + z) / (
            pow(h, 2))  # Uses the formula f''(x) = [f(x+h) - 2f(x) + f(x-h)]/h^2 to obtain the second derivative

    elif method == '3':  # Uses the formula [f(x-2h) + 2f(x-h) - 2f(x+h) + f(x+2h)]/2h^3 to obtain the third derivative
        l = f.subs({'x': float(x + (2 * h))}).evalf()  # to get index of X(i+2)
        g = f.subs({'x': float(x - (2 * h))}).evalf()  # to get index of X(i-2)
        return (-1 * g + 2 * z - 2 * w + l) / (2 * pow(h, 3))


############################################################################################################


points = 0
answer = input("If you want to use a function enter 1, a table enter 2 : ")
if answer == '1':
    func = input("Please enter your function: ")  # The function is input here as a string
    f = sympify(func)  # Converts the input function into a format Sympy can work with
    h_func = float(
        input("Please enter the h you want to use: "))  # Step size is entered here and converted from string into float
    min = input(
        "If it is a minimum h enter 1, maximum h enter 2  : ")  # Here the user chooses whether the step size just entered is the min or max
    RichardList_func = []  # Creates a list that will be used later
else:
    points = int(input(
        "Please enter the number of points : "))  # If the user chooses to enter a table, they are asked to enter the number of points for the table

order = int(input(
    "Enter the order of extrapolation : "))  # The order of extrapolation converted into integer, note
method = input(
    "If you want the 1st derivative enter 1, the 2nd enter 2, the 3rd enter 3 : ")  # The user chooses the order of differentiation
X = float(input(
    "Enter the X coordinate of the point where you want to get the derivative : "))  # The point we want the derivative at converted from string into float

if answer == '1':
    #order = order + 3  # Just to make it work properly
    if min == '2':  # The the step size is the maximum step size
        h_func = h_func / pow(2, (order / 2) - 1)  # Divides the step size by a power of 2

    for a in range(int(order / 2)):  # Loops from 0 to order/2 using the iterator "a"
        # Calculates the derivative using the "derivativeForFunction" function and add it to the list delcared previously
        # It also multiplies the step size by 2^a each iteration
        # In the end this should give us multiple derivatives using different step size (multiplied by or divided by a power of 2)
        RichardList_func.append(derivativeForFunction(h_func * pow(2, a), X, method, f))

        # print(RichardList_func) #Print the list of less accurate derivatives, reserved for debugging
    # This last part I'm a bit lost on
    # It's meant to calculate the extrapolations depending on the order of extrapolations
    # Don't know how to explain the details though
    Extrapolation(RichardList_func,order ,False)

elif answer == '2':
    # The table option is pretty similar to the function option
    # The main difference is that we have to prepare the table and fill it.
    # The rest is pretty similar
    #order = order + 4  # Just to make it work properly
    mat = []  # Declaring a list for the table
    for i in range(0, 2):  # Creating a list with two rows
        mat.append([])
    for j in range(0, points):  # Creating number of coloumns required according to #of points
        for i in range(0, 2):
            mat[i].append(j)
            if i == 0:
                print("Enter x of point " + str(j + 1) + " : ", end='')
                mat[i][j] = float(input())
            else:
                print("Enter y of point " + str(j + 1) + " : ", end='')
                mat[i][j] = float(input())
    step = round(mat[0][1] - mat[0][0], 5)
    print("Step size = ", step)
    RichardList = []
    for i in range(0, 1):
        RichardList.append([])
    for i in range(0, 1):
        for j in range(0, int(order / 2)):
            RichardList[0].append(j)
    for a in range(int(order / 2)):
        RichardList[0][a] = derivativeForTable(step * pow(2, a), X, method, mat, order)
    Extrapolation(RichardList,order , True)
