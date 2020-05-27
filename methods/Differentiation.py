from sympy import *
import numpy as np
import math
import sys

class FirstOrSecondDerivError(BaseException):
    pass
class ThirdDerivError(BaseException):
    pass
class WrongFunctionFormat(BaseException):
    pass

#Some notes:
#Exponentials should be in the form of exp, so e^(-x) = exp(-x)
#Multiplication should be done using an asterisk, so xe^x should be entered in the form x * exp(x) or else the final answer won't be calculated correctly.

########################################Utility Functions#############################################

#Returns the final answer
def Extrapolation(list, ord, table) :
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
    return list[0]
    #print('Final Answer =', list[0])
    ######For Table#####
   else :
       while (k < ord / 2 + 1):
           for v in range(counter):
               list[0][v] = (pow(4, k - 1) * list[0][v] - list[0][v + 1]) / (
                       pow(4, k - 1) - 1)# Calculates the extrapolation using the general formula
           k = k + 1
       #print('Final Answer =',list[0][0])
       return list[0][0]


def CalcTrueError(ApproxValue, DerivFunc, DerivPoint, DerivOrder):
    #Deriving the exact value
    x = Symbol('x') #specifies a symbol for calculations
    init_printing(use_unicode=True) #No idea
    ExactValue = diff(DerivFunc, 'x', DerivOrder) #Obtains the analytical form of the derivative
    DerivEqu = lambdify(x,ExactValue) #No idea 2

    try:
      ExactValue = DerivEqu(DerivPoint)

    except (Exception, TypeError, AttributeError):
     raise WrongFunctionFormat

    if(round(ApproxValue,5) == round(ExactValue,5) == 0):
        return "0/0, Undefined value"
    if (round(ApproxValue,5) == round(ExactValue,5)):
        return 0
    elif (ExactValue == 0): #To avoid oo error
        return str(round(ApproxValue,5))+'/0'


    TrueError = abs( (ExactValue - ApproxValue)/ExactValue ) * 100 #Calculates the true error

    return TrueError

#Generously funded by the interface guild.
#Thanks Essam!
def Input_2D():
    xdata = []
    ydata = []
    n = int(input("Type in the no. of points : "))
    print('Insert each point as space seperated x & y')
    for i in range(0, n):
        x,y = map(float, input().split()) # splits a given input 'a b' , maps 'a' in x and 'b' in y
        xdata.append(float(x)) #filling the x,y lists
        ydata.append(float(y))
    return np.array(xdata),np.array(ydata) #Returns 2 numpy arrays

# Pretty much the same as "derivativeForFunction" but here we already have the points and their values
def derivativeForTable(h, x, method, mat, order):
    m = mat[0].index(x)  # to get index of X(i)
    try:
        w = mat[0].index(round(x + h, 1))  # to get index of X(i+1)
        z = mat[0].index(round(x - h, 1))  # to get index of X(i-1)

    except ValueError: #Sometimes python likes to add 0.0000000000001 or something and screw with the numbers so you'd get this exception whenver python feels like a dick.
        raise FirstOrSecondDerivError

        # Failed attempt at making the program more flexible
        # next2_index = mat[0].index(round(x+2*h,2))
        # if method == '1':
        # The other methods have an error of h^2
        # This one has an error of h
        # So we must compensate in the order
        # order = order**2
        # return ((4*mat[1][w] - 3* mat[1][m] - mat[1][next2_index]) / 2*h )
    try:
        if method == '1':
            return (mat[1][w] - mat[1][z]) / (2 * h)
        elif method == '2':
            return (mat[1][w] - 2 * mat[1][m] + mat[1][z]) / (pow(h, 2))

        elif method == '3':
            l = mat[0].index(round(x + (2 * h)), 5)  # to get index of X(i+2)
            g = mat[0].index(round(x - (2 * h)), 5)  # to get index of X(i-2)
            return (-mat[1][g] + 2 * mat[1][z] - 2 * mat[1][w] + mat[1][l]) / (2 * pow(h, 3))
    except ValueError:
        raise ThirdDerivError

#Some clarification for what "method" is, it is the order of derivation, as in a first derivative (1), second derivative (2) and so on..
def derivativeForFunction(h, x, method, formula):
    w = formula.subs({'x': float(x + h)}).evalf()  # to get index of X(i+1)
    z = formula.subs({'x': float(x - h)}).evalf()  # to get index of X(i-1)
    m = formula.subs({'x': x}).evalf()  # to get index of X(i)

    try:
     if method == '1':
        return (w - z) / (
                    2 * h)  # Uses the centeral difference formula to obtain the first derivative (f'(x) = [f(x+h) - f(x-h)]/2h

     elif method == '2':
        return (w - 2 * m + z) / (
            pow(h, 2))  # Uses the formula f''(x) = [f(x+h) - 2f(x) + f(x-h)]/h^2 to obtain the second derivative

     elif method == '3':  # Uses the formula [f(x-2h) + 2f(x-h) - 2f(x+h) + f(x+2h)]/2h^3 to obtain the third derivative
        l = formula.subs({'x': float(x + (2 * h))}).evalf()  # to get index of X(i+2)
        g = formula.subs({'x': float(x - (2 * h))}).evalf()  # to get index of X(i-2)
        return (-1 * g + 2 * z - 2 * w + l) / (2 * pow(h, 3))
    except OverflowError:
        raise OverflowError



############################################################################################################
def FuncDeriv(func, h, order, x):


    formula = sympify(func)  # converts the input function into a format sympy can work with

    order = 2*(order+1) #So the order of extrapolation is entered as 1,2,3 or any other number
    #The extrapolating function takes the order as O(h^order), so for a first order extrapolation O(h^4) the user would enter 1 and it would become 2*2 =4
    #For a second order extrapolation O(h^6), the user would enter 2 which would become 2*3 =6
    #For a third order O(h^8), the user would enter 3 which would become 2*4 = 8


    FirstDerivList = []
    SecondDerivList = []
    ThirdDerivList = []
    try:
     for a in range(int(order / 2)):  # Loops from 0 to order/2 using the iterator "a"
        # Calculates the derivative using the "derivativeForFunction" function and add it to the list delcared previously
        # It also multiplies the step size by 2^a each iteration
        # In the end this should give us multiple derivatives using different step size (multiplied by or divided by a power of 2)
        FirstDerivList.append(derivativeForFunction(h * pow(2, a), x, '1', formula))
        SecondDerivList.append(derivativeForFunction(h * pow(2, a), x, '2', formula))
        ThirdDerivList.append(derivativeForFunction(h * pow(2, a), x, '3', formula))
    except OverFlowError:
        return "OverFlow", "OverFlow", "OverFlow", "OverFlow", "OverFlow", "OverFlow"

    FirstDerivApprox = Extrapolation(FirstDerivList, order, False) #Extrapolates the derivative values
    SecondDerivApprox = Extrapolation(SecondDerivList, order, False)
    ThirdDerivApprox = Extrapolation(ThirdDerivList, order, False)

    try:
      FirstDerivTrueError = CalcTrueError(FirstDerivApprox, formula, x, '1') #Calculates the true error
      SecondDerivTrueError = CalcTrueError(SecondDerivApprox, formula, x, '2')
      ThirdDerivTrueError = CalcTrueError(ThirdDerivApprox, formula, x, '3')

    except WrongFunctionFormat:
        return "Wrong Function Format",None , "Wrong Function Format", None  ,"Wrong Function Format", None

    if type(FirstDerivTrueError) is str and type(SecondDerivTrueError) is str and type(ThirdDerivTrueError) is str:
        return round(FirstDerivApprox, 5), round(FirstDerivTrueError, 5), round(SecondDerivApprox, 5), round(SecondDerivTrueError, 5),round(ThirdDerivApprox, 5), round(ThirdDerivTrueError, 5)

    return round(FirstDerivApprox, 5), FirstDerivTrueError, round(SecondDerivApprox, 5), SecondDerivTrueError,round(ThirdDerivApprox, 5), ThirdDerivTrueError

def TableDeriv(x, Xlist, Ylist):


    points = len(Xlist)#Gets the length of the Xlist array and therefore the number of points entered. I know I could've made the input function return it but I didn't want to screw over the interface team.
    try:
        index = np.where(Xlist == x)[0] #Finds the index of the input point for the derivative
    #Note that np.where returns a matrix of the indices where the value is found, hence the [0][0] to get the first occurance.

    except IndexError:
        return "Point not in table, aborting..."


    #We need to now know which side is shorter to truncate the list

    after = points - (index +1) #Sees how many indices/points are after the wanted element, this is more compact than after = points - 1 - index
    before = index  #Finds the number of incdices/points are before the wanted element. Excludes the index of the point entered as the indexing starts at 0 anyway, no need for index - 1
    order = math.floor(math.log2(points)) * 2  #The number of extrapolations depends logarithmically on the number of data points
    #We need at least 4 data points + the middle one to extrapolate once (one CD with h and another with 2h)
    #We need 8  + the middle one to extrapolate twice (one CD with, another with 2h and another with 4h)
    #And it goes on like this..


    if (after != before): #If the point isn't centered, we need to truncate the point so it's in the middle.
        diff = abs(after-before)
        #print("Aysemmtric table, need to truncate") #Tested with sheet V part I problem 1 with points 2.2 and 1.2, both truncated fine  #For debugging
        if(after > before): #More points after than before, we need to truncate the Xlist and Ylist so they start from 0 to (points - diff)
            Xlist = Xlist[ : points - diff]
            Ylist = Ylist[ : points - diff]
            order = math.floor(math.log2(before*2)) * 2 #Untested, no sheet problems have the required points in a place other than the middle

        else:
            Xlist = Xlist[diff:]
            Ylist = Ylist[diff:]
            order = math.floor(math.log2(after*2)) * 2

    #print(Xlist) #For debugging
    #print(Ylist) #For debugging

    mat = np.row_stack((Xlist,Ylist)) #Requested by the interface team, this takes 2 lists and stacks them into a matrix
    mat = mat.tolist() #This was required to create the correct input for the function to work without any modifications, there might be a better way but this works fine for now.

    #print(mat) #For debugging
    #print(mat2) #For debugging

    step = round(mat[0][1] - mat[0][0], 5)

    #Preparing the lists
    FirstDerivList = []
    SecondDerivList = []
    ThirdDerivList = []

    for i in range(0, 1):
        FirstDerivList.append([])
        SecondDerivList.append([])
        ThirdDerivList.append([])

    for i in range(0, 1):
        for j in range(0, int(order / 2)):
            FirstDerivList[0].append(j)
            SecondDerivList[0].append(j)
            ThirdDerivList[0].append(j)

    for a in range(int(order / 2)):
        try:
        #Calculating the derivatives in each list
            FirstDerivList[0][a] = derivativeForTable(step * pow(2, a), x, '1', mat, order)
            SecondDerivList[0][a] = derivativeForTable(step * pow(2, a), x, '2', mat, order)
            ThirdDerivList[0][a] = derivativeForTable(step * pow(2, a), x, '3', mat, order)

        except FirstOrSecondDerivError: #If the function cannot calculate x+1 or x-1, then the first, second and third derivatives cannot be calculated
            return "Calculation point doesn't exist on the table","Calculation point doesn't exist on the table","Calculation point doesn't exist on the table"
        except ThirdDerivError: #If the function is able to calculate the first and second derivatives but not the third, it starts over and calculates only the first and the second
                                #Could be optimized by not starting over but It's not that big of a deal with our usecase.
            for a in range(int(order / 2)):
                FirstDerivList[0][a] = derivativeForTable(step * pow(2, a), x, '1', mat, order)
                SecondDerivList[0][a] = derivativeForTable(step * pow(2, a), x, '2', mat, order)
            FirstDerivApprox = Extrapolation(FirstDerivList,order , True) #Extrapolates the derivative values
            SecondDerivApprox = Extrapolation(SecondDerivList,order , True)
            return FirstDerivApprox,SecondDerivApprox,"Calculation point doesn't exist on the table"


    FirstDerivApprox = Extrapolation(FirstDerivList,order , True)
    SecondDerivApprox = Extrapolation(SecondDerivList,order , True)
    ThirdDerivApprox = Extrapolation(ThirdDerivList,order , True)

    return round(FirstDerivApprox, 5),round(SecondDerivApprox, 5),round(ThirdDerivApprox, 5)

############################################################################################################
def Main():
    answer = input("If you want to use a function enter 1, a table enter 2 : ")
    if answer == '1':
        func = input("please enter your function: ")  # the function is input here as a string
        h_func = float( input("please enter the h you want to use: ") )  # step size is entered here and converted from string into float
        order = int( input("Enter the order of extrapolation : ") )  # The order of extrapolation converted into integer, note
        X = float( input("Enter the X coordinate of the point where you want to get the derivative : ") )  # The point we want the derivative at converted from string into float


        print(FuncDeriv(func, h_func, order, X))

    elif answer == '2':
        Xlist,Ylist = Input_2D() #Asks the user to input the number of points, takes the input points and returns 2 numpy arrays
        X = float( input("Enter the X coordinate of the point where you want to get the derivative : ") )  # The point we want the derivative at converted from string into float

        print(TableDeriv(X, Xlist, Ylist))


#Main()
