from sympy import *

'''
This Sub-Project Is done By:
Team IV(Ammar Mohamed, Ahmed Ayman, Mohamed Akram, Omar Ahmed, Youssef Atef)

This Code contains three Numerical techinques for Interpolation:
Newton General
Newton-Gregory
La Grange
'''

def RoundExpression(expr, num_digits): #Rounds Expression Coefficients
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})


def NewtonGeneral(Xi, Yi, n, value):
    '''
    This function uses Newton General technique for Interpolation

    Xi: List contains x values of the points
    Yi: List contains y values of the points
    n: Number of points
    value: The x value to get the interpolation at

    returns -> DDT,Yint,RE,Exp 
    DDT: Divided Difference Table
    Yint: A list to contain the answer at each order
    RE: A list of Residual Errors at each order
    Exp: Full simplified Expression in terms of X
    '''
    #reversing the order of points if the last point is closer to the value than the first point
    if(abs(Xi[n-1]-value) < abs(Xi[0]-value)): 
        Xi.reverse()
        Yi.reverse()
    x = Symbol('x') #Symbolizing X to get the expression
    Yint = [0 for i in range(n)] #A list to contain the answer at each order
    Exp = [0 for i in range(n)]
    RE = [0 for i in range(n)] #A list to contain Residual Error at each order
    DDT = [[0 for i in range(j,n)] for j in range(n)]  #Initializing Divided Difference Table
    for i in range(n):
        DDT[i][0] = Yi[i] #Adding Y values at the first column
    for j in range(1,n):
        for i in range(0,n-j):
            DDT[i][j] = (DDT[i+1][j-1] - DDT[i][j-1])/(Xi[i+j]-Xi[i]) #Calculating Divided Difference
   
    xterm = 1 #to be used in calculating Yint
    Yint[0] = DDT[0][0]
    Exp = [0 for i in range(n)]
    ExpXterm = 1 #to be used to get the expression in terms of X
    Exp[0] = Yi[0] #Exp will have the expression in terms of X
    for order in range(1,n): #Calculating Yint for each order and the Expression
        xterm = xterm*(value-Xi[order-1])
        ExpXterm = ExpXterm*(x - Xi[order-1])
        Yint2 = Yint[order-1] + DDT[0][order]*xterm
        Exp[order] = Exp[order-1] + ExpXterm*DDT[0][order]
        Yint[order] = Yint2
    for order in range(0,n):  #Calculating Residual error for each order
        RE[order] = Yint[n-1] - Yint[order]
        Exp[order] = RoundExpression(expand(Exp[order]),6)
        Yint[order] = round(Yint[order],6)
        RE[order] = round(RE[order],6)
        

    return DDT,Yint,RE,Exp




def NewtonGregory(Xi, Yi, n, value):

    '''
    This function uses Newton-Gregory technique for Interpolation

    Xi: List contains x values of the points
    Yi: List contains y values of the points
    n: Number of points
    value: The x value to get the interpolation at

    returns -> DT,Yint,RE,Exp 
    DT: Differences Table
    Yint: A list to contain the answer at each order
    RE: A list of Residual Errors at each order
    Exp: Full simplified Expression in terms of X
    '''
    x = Symbol('x') #Symbolizing X to get the expression
    #reversing the order of points if the last point is closer to the value than the first point
    if(abs(Xi[n-1]-value) < abs(Xi[0]-value)): 
        Xi.reverse()
        Yi.reverse()
    h = Xi[1]-Xi[0]
    alpha = (value-Xi[0])/h
    AlphaOfX = (x - Xi[0])/h #Getting Alpha in terms of X to get the expression
    Yint = [0 for i in range(n)] #A list to contain the answer at each order
    Exp = [0 for i in range(n)]
    RE = [0 for i in range(n)] #A list to contain Residual Error at each order
    DT = [[0 for i in range(j,n)]  #Initializing Differences Table
        for j in range(n)]
    for i in range(n):
        DT[i][0] = Yi[i]
    for j in range(1,n):
        for i in range(0,n-j):
           DT[i][j] = DT[i+1][j-1] - DT[i][j-1] #Calculating Differences Table

    alphaterm = 1 
    ExpAlphaTerm = 1
    
    Exp[0] = Yi[0]
    Yint[0] = DT[0][0]
    for order in range(1,n):
        alphaterm = alphaterm*((alpha-order+1)/order)
        ExpAlphaTerm = ExpAlphaTerm*((AlphaOfX-order+1)/order)
        Yint2 = Yint[order-1] + DT[0][order]*alphaterm
        Exp[order] = Exp[order-1] + ExpAlphaTerm*DT[0][order]
        Yint[order] = Yint2

    for order in range(0,n):
        RE[order] = Yint[n-1] - Yint[order]
        Exp[order] = RoundExpression(expand(Exp[order]),6)
        Yint[order] = round(Yint[order],6)
        RE[order] = round(RE[order],6)

    return DT,Yint,RE,Exp


def Newton(Xi,Yi,n,value,order): #for the interface team
    '''
    Considering you didn't determine which type of Newton techinque 
    you will use, this function will determine if you need Newton General
    or Newton Gregory (in case x values are equidistant)

    Xi: List contains x values of the points
    Yi: List contains y values of the points
    n: Number of points
    value: The x value to get the interpolation at
    order: to determine the order of answer

    returns->DT,Yint,RE,Exp 
    DT: Differences Table
    Yint: The value of interpolation at a given order and value
    Exp: The Expression in terms of X at a given order
    DiffYint: The value of Expression derivative at a given order
    DiffExp: The Expression derivative in terms of X at a given order 
    RE: The Residual Error at a given order
    '''

    x = Symbol('x')
    equidistant = True
    h = Xi[1]-Xi[0]
    for i in range(2,n):
        if (Xi[i]-Xi[i-1] != h):
            equidistant = False
            break
    if (equidistant):
        DT,Yint,RE,Exp = NewtonGregory(Xi,Yi,n,value)
    else:
        DT,Yint,RE,Exp = NewtonGeneral(Xi,Yi,n,value)

    DiffExp = [0 for i in range(n)]
    DiffYint = [0 for i in range(n)]
    for i in range(n):
        DiffExp[i] = diff(Exp[i],x)
        DiffYint[i] = round(DiffExp[i].subs(x,value),6)
    
    return DT,Yint[order],Exp[order],DiffYint[order],DiffExp[order],RE[order]




def LaGrange(Xi, Yi, n, value):
    '''
    This function uses La Grange technique for Interpolation

    Xi: List contains x values of the points
    Yi: List contains y values of the points
    n: Number of points
    value: The x value to get the interpolation at

    returns -> Yint,Exp
    Yint: The value of interpolation at a given value
    Exp: Full simplified Expression in terms of X
    '''
    x = Symbol('x') #Symbolizing X to get the expression
    sum = 0 
    Exp = 0
    for i in range(0,n):
        product = Yi[i]
        ExpProduct = Yi[i]
        for j in range(0,n):
            if (i != j):
                product = product*(value-Xi[j])/(Xi[i]-Xi[j])
                ExpProduct = ExpProduct*(x-Xi[j])/(Xi[i]-Xi[j])
        sum = sum + product
        Exp = Exp + ExpProduct

    Exp = RoundExpression(expand(Exp),6)
    Yint = sum
    Yint = round(Yint,8)
    return Yint,Exp

