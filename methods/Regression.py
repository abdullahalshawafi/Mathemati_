
import math
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np #temporary
from numpy import *
import sympy
from sympy.abc import x,y
from sympy import symbols
from sympy import symbol
from sympy.plotting import plot
from mpl_toolkits.mplot3d import Axes3D
from sympy.plotting import plot3d


def Sround(x,n):
    if(x==0):
        return 0;
    elif (x != x):
        return 9e99;
    else:
        return  round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1));

def zEvalList(X,Y,RHS):
    x,y = symbols('x y');
    rhs=sympy.sympify(RHS)  
    RHS=sympy.lambdify([x,y], rhs)
    Answer = np.zeros((X.shape[0],X.shape[1]))
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Answer[i][j] = RHS(X[i][j],Y[i][j])

    return Answer


def PointsFor3DSF(xdata,ydata,RHS):
    Po = np.zeros((len(xdata),2))
    for i in range(len(xdata)):
        Po[i][0] = xdata[i]
        Po[i][1] = ydata[i]

    n1 = len(xdata)
    xmin = Po[0][0]
    xmax = Po[0][0]
    ymin = Po[0][1]
    ymax = Po[0][1]

    for i in range(1, n1):
        if Po[i][0] < xmin:
            xmin = Po[i][0]
        if Po[i][0] > xmax:
            xmax = Po[i][0]
        if Po[i][1] < ymin:
            ymin = Po[i][1]
        if Po[i][1] > ymax:
            ymax = Po[i][1]

    nx = 100
    ny = 200

    grid_x, grid_y = np.mgrid[xmin:xmax:((nx + 1) * 1j), ymin:ymax:((ny + 1) * 1j)]
    grid_x_out = np.mgrid[xmin:xmax:((nx + 1) * 1j)]
    grid_y_out = np.mgrid[ymin:ymax:((ny + 1) * 1j)]

    RangePo = np.zeros(((nx+1)*(ny+1),2))
    for i in range(nx+1):
        for j in range(ny+1):
            RangePo[i+(nx+1)*j][0] = grid_x[i][j]
            RangePo[i+(nx+1)*j][1] = grid_y[i][j]

    grid_z1 = zEvalList(grid_x, grid_y,RHS)

    return grid_x_out, grid_y_out, grid_z1


def Plot_3D_RHS(xdata,ydata,zdata,RHS):
    x,y = symbols('x y')
    rhs=sympy.sympify(RHS)
    RHS=sympy.lambdify([x,y], rhs)
    z=plot3d(rhs, (x, -5+min(xdata), 5+max(xdata)), (y, -5+min(ydata), 5+max(ydata)))
    plt.savefig('ThreeD.png')
    #3D graphing is pretty straight forward using Sympy, in contrast to how it's only done through parametric
    #equations in MPL, however it does not do scatter plots...
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(xdata, ydata, zdata, c = 'b', marker='o')
    #ax.set_xlabel('X-axis')
    #ax.set_ylabel('Y-axis')
    #ax.set_zlabel('Z-axis')
    #plt.show()


def Plot_2D_RHS(xdata,ydata,RHS,LHS):
    x,y = symbols('x y')
    RHS=sympy.sympify(RHS)
    RHS=sympy.lambdify([x], RHS)
    LHS=sympy.sympify(LHS)
    LHS=sympy.lambdify([x,y],LHS)
    Ydata=[]
    for i in xdata: #the scatter plot will involve (f(y),x) since we're plotting the linearized RHS
        Ydata.append(LHS(xdata,ydata))
    plt.figure(figsize=(6, 4))
    plt.scatter(xdata, Ydata[0], label='Data')
    xdata=np.linspace(min(xdata),max(xdata),10000)
    plt.plot(xdata, RHS(xdata), label='Fit')
    plt.legend(loc='best')
    plt.show()
    #A=plot(F,show=False, xlim=(min(xdata)-4,max(xdata)+4) , ylim=(min(ydata)-4,max(ydata)+4))
    #A.show()


def Linearized_Regression(xdata, ydata, Function,r):
    SympF = [] #Contains the functions in Sympy form
    F = [] #contains the function in classic form
    x, y = symbols('x, y')
    for i in range(0,len(Function)): #converting the string functions into a suitable form
        SympF.append(sympy.sympify(Function[i])) #The first function is that on the RHS (y)
        F.append(sympy.lambdify([x, y], SympF[i]))
    FL = []
    for i in range(0,len(F)): #this for loop goes through each function
        Z = [] #temporary list
        for j in range(0, len(xdata)):  #this one makes a new list by plugging each xdata, ydata for each function
            if(F[i](xdata[j], ydata[j])==F[i](xdata[j], ydata[j])):
                Z.append(F[i](xdata[j], ydata[j]))
            else:
                return '','','',''
        FL.append(Z) #FL contains a sublist     for each function, this sublist is the result from plugging each xdata and ydata into the function
        n=len(F)
    a = np.empty((n-1,n-1))
    b = np.empty((n-1,1))
    for i in range(1,n):
        for j in range(1,n):
            a[i-1][j-1] = np.sum(np.multiply(FL[i],FL[j]))
        b[i-1][0]= np.sum(np.multiply(FL[0],FL[i]))
    if(np.linalg.det(a)==0):
        return '','','',''
    Sol=np.round(np.transpose(np.linalg.solve(a, b)),r) #receiving the list, making it horizontal then rounding each element
    Solution = []
    for sublist in Sol: #Flattening the list ( from [[ ]] to [ ])
        for item in sublist:
            Solution.append(item)
    RegressionError = []
    for i in range(0,len(ydata)):
        Val = FL[0][i] #the first sublist inside FL corresponds to the outputs from the function in the LHS
        for j in range(1,n):
            Val -= (FL[j][i]*Solution[j-1]) #subtract each of the entries in the 1st sublist from each of the functions*constant in the RHS.
        RegressionError.append(Val**2) # square at each time.
    Sr = Sround(np.sum(RegressionError),r) #Sr = Sum((Yi-Y(regression))^2) = Sum((Yi-Const1*X1i-Const2*X2i-......)^2)
    StringSol = [str(Sround(c,4)) for c in Solution ] #converting each constant to a string
    LHS=Function.pop(0) #removing the LHS
    RHS=[' * '.join(x) for x in zip(StringSol, Function)]#multiplying the constants and the functions element wise

    RHS=(" + ".join(str(x) for x in RHS))
    return LHS,RHS,StringSol,Sr #LHS and RHS are just what's actually needed

def Surface_Fit_Beta(xdata, ydata, zdata, Function,r):
    SympF = [] #Contains the functions in Sympy form
    F = [] #contains the function in classic form
    x, y, z = symbols('x, y, z')
    for i in range(0,len(Function)): #converting the string functions into a suitable form
        SympF.append(sympy.sympify(Function[i])) #The first function is that on the RHS (y)
        F.append(sympy.lambdify([x, y,z], SympF[i]))

    FL = []
    for i in range(0,len(F)): #this for loop goes through each function
        Z = [] #temporary list
        for j in range(0, len(xdata)):  #this one makes a new list by plugging each xdata, ydata for each function
            Z.append(F[i](xdata[j], ydata[j], zdata[j]))
        FL.append(Z) #FL contains a sublist for each function, this sublist is the result from plugging each xdata,ydata,zdata into the function
        n=len(F)
    a = np.empty((n-1,n-1))
    b = np.empty((n-1,1))
    for i in range(1,n):
        for j in range(1,n):
            a[i-1][j-1] = np.sum(np.multiply(FL[i],FL[j]))
        b[i-1][0]= np.sum(np.multiply(FL[0],FL[i]))
    if(np.linalg.det(a)==0):
        return '','','',''
    Sol=np.round(np.transpose(np.linalg.solve(a, b)),r) #receiving the list, making it horizontal then rounding each element
    Solution = []
    for sublist in Sol: #Flattening the list ( from [[ ]] to [ ])
        for item in sublist:
            Solution.append(item)
    StringSol = [str(c) for c in Solution ] #converting each constant to a string
    RegressionError = []
    for i in range(0,len(ydata)):
        Val = FL[0][i] #the first sublist inside FL corresponds to the outputs from the function in the LHS
        for j in range(1,n):
            Val -= (FL[j][i]*Solution[j-1]) #subtract each of the entries in the 1st sublist from each of the functions*constant in the RHS.
        RegressionError.append(Val**2) # square at each time.
        Sr = Sround(np.sum(RegressionError),r) #Sr = Sum((Yi-Y(regression))^2) = Sum((Yi-Const1*X1i-Const2*X2i-......)^2)

    LHS=Function.pop(0) #removing the LHS
    rhs=[' * '.join(x) for x in zip(StringSol, Function)]#multiplying the constants and the functions element wise
    RHS=(" + ".join(str(x) for x in rhs))

    return LHS,RHS,StringSol,Sr #LHS and RHS are just what's actually needed


def Nonlinear_Regression(xdata,ydata,NonlinearFunction,r): #takes x,y lists and a nonlinear function string
  if('d' in NonlinearFunction):
      return Nonlinear_Regression_d(xdata,ydata,NonlinearFunction,r)
  x,a,b,c=symbols('x a b c')
  Function=sympy.sympify(NonlinearFunction) 
  true_len=len(Function.atoms(sympy.Symbol))
  if(len(xdata)<true_len-1):
     Sol=''
     return Sol,0;
  F=sympy.lambdify([x, a,b,c], Function)
  C, Covariance = curve_fit(F, xdata, ydata, maxfev=1500) #we don't need to show the covariance matrix
  Sol=Function.subs([(x, x), (a, Sround(C[0],r)), (b,Sround( C[1],r)), (c, Sround(C[2],r))])
                   #    ,(d, Sround(C[3],r))
  #,(e,Sround(C[4],r)),(f,Sround(C[5],r)),(g,Sround(C[6],r)),
                     #(h,Sround(C[7],r)),(i,Sround(C[8],r))])
  RegressionError = []
  val=ydata.copy()
  for i in range(0,len(ydata)):
      val[i] -= (Sol.subs(x,xdata[i])) #subtract each of the entries in the 1st sublist from each of the functions*constant in the RHS.
  RegressionError.append(val[i]**2) # square at each time.
  Sr = Sround(np.sum(RegressionError),r) #Sr = Sum((Yi-Y(regression))^2) = Sum((Yi-Const1*X1i-Const2*X2i-......)^2)
  return str(Sol) ,Sr

def Nonlinear_Regression_d(xdata,ydata,NonlinearFunction,r): #takes x,y lists and a nonlinear function string
  x,a,b,c,d=symbols('x a b c d')
  Function=sympy.sympify(NonlinearFunction)
  true_len=len(Function.atoms(sympy.Symbol))
  if(len(xdata)<true_len-1):
     Sol=''
     return Sol,0;
  F=sympy.lambdify([x, a,b,c,d], Function)
  C, Covariance = curve_fit(F, xdata, ydata, maxfev=1500) #we don't need to show the covariance matrix
  Sol=Function.subs([(x, x), (a, Sround(C[0],r)), (b,Sround( C[1],r)), (c, Sround(C[2],r))
                       ,(d, Sround(C[3],r))])
  #,(e,Sround(C[4],r)),(f,Sround(C[5],r)),(g,Sround(C[6],r)),
                     #(h,Sround(C[7],r)),(i,Sround(C[8],r))])
  RegressionError = []
  val=ydata.copy()
  for i in range(0,len(ydata)):
      val[i] -= (Sol.subs(x,xdata[i])) #subtract each of the entries in the 1st sublist from each of the functions*constant in the RHS.
  RegressionError.append(val[i]**2) # square at each time.
  Sr = Sround(np.sum(RegressionError),r) #Sr = Sum((Yi-Y(regression))^2) = Sum((Yi-Const1*X1i-Const2*X2i-......)^2)
  return str(Sol) ,Sr


def Nonlinear_Plot(xdata,ydata,NonlinearFunction):
    x=symbols('x');
    Function=sympy.sympify(NonlinearFunction);
    F=sympy.lambdify([x], Function);
    plt.figure(figsize=(6, 4));

    plt.scatter(xdata, ydata, label='Data');
    xdata=np.linspace(min(xdata),max(xdata),10000);
    plt.plot(xdata, F(xdata), label='Best Fit');
    plt.legend(loc='best');
    plt.show();

def Input_2D():
    xdata = []
    ydata = []
    n = int(input("Type in the no. of points : "))
    print('Insert each point as space seperated x & y')
    for i in range(0, n):
        x,y = map(float, input().split()) # splits a given input 'a b' , maps 'a' in x and 'b' in y
        xdata.append(float(x)) #filling the x,y lists
        ydata.append(float(y))
    return np.array(xdata),np.array(ydata)

def Input_3D():
    xdata = []
    ydata = []
    zdata= []
    n = int(input("Type in the no. of points : "))
    print('Insert each point as space seperated x & y & z')
    for i in range(0, n):
        x,y,z = map(float, input().split()) # splits a given input 'a b' , maps 'a' in x and 'b' in y
        xdata.append(float(x)) #filling the x,y lists
        ydata.append(float(y))
        zdata.append(float(z))
    return np.array(xdata),np.array(ydata),np.array(zdata)

def TrueError(ydata,r):
    TrueError=[]
    ydata_Avg = (np.sum(ydata))/len(ydata)
    for y in ydata:
        TrueError.append((y-ydata_Avg)**2)
    St = Sround(np.sum(TrueError),r)
    return St

def Curfe_Vamily_Detective(xdata,ydata,r):
    if(len(xdata)<4):
        return 0,0,0,0;
    Formulas=[ "a+b*x","a+b*x+c*x**2","a+b*x+c*x**2+d*x**3","a*exp(b*x)","a+b*log(x)","1/(a+b*x)","a*x**b","a+b*sin(c*x+d)"]
    Forms = ["linear", "quadratic", "cubic", "exponential", "logarithmic", "reciprocal", "power","Sinusoidal"]
    Str_Sol=[]
    reg_errors=[]
    for i in range(0,7):
        a,b=Nonlinear_Regression_d(xdata,ydata,str(Formulas[i]),r)
        Str_Sol.append(str(a))
        reg_errors.append(b)
    indm = reg_errors.index(min(reg_errors))
    err_copy=reg_errors
    err_copy.pop(indm);
    return Str_Sol[indm],Forms[indm],reg_errors[indm],Sround(np.std(err_copy),r)


def Curve_Family_Detective(xdata, ydata, r):
    formulas = {"linear": ["y", "1", "x"],
                "quadratic": ["y", "1","x","x**2"],
                "cubic": ["y", "1", "x", "x**2", "x**3"],
                "exponential": ["ln(y)", "1", "x"],
                "logarithmic": ["y", "1", "ln(x)"],
                "reciprocal": ["1/y", "1", "x"],
                "power": ["log(y)", "1", "log(x)"]}
    forms = ["linear", "quadratic", "cubic", "exponential", "logarithmic", "reciprocal", "power"]
    LHS = [] #holds the lhs for all possible forms
    RHS = [] #holds the rhs for all possible forms
    Str_Sol = [] #holds the constants for all possible forms
    reg_errors = [] #holds the constants for all possible forms
    str_equation = "" #holds a string representing the best-fitted equation chosen from the upove formulas
    for n in formulas:
        lhs, rhs, str_sol, sr = Linearized_Regression(xdata, ydata, formulas.get(n), r)
        LHS.append(lhs)
        RHS.append(rhs)
        Str_Sol.append(str_sol)
        reg_errors.append(sr)
    print(reg_errors)
    for x in reg_errors:
        for x in reg_errors:
            if(x==''):
                reg_errors.pop(reg_errors.index(x));
    print(reg_errors)

    indm = reg_errors.index(min(reg_errors))
    indM=reg_errors.index(max(reg_errors))
    if (indm == 3):
        #y=ae^(bx), Str_Sol[3] = ["ln(a)","b"]
        str_equation = str(Sround(exp(float(Str_Sol[indm][0])),r)) + " * exp(" + Str_Sol[indm][1] + " * x)"
    elif (indm == 5):
        #y=1/(a+bx), RHS[5] = "a+bx"
        str_equation = "1/("+RHS[indm]+")"
    elif (indm == 6):
        # y=a*x^(b),  Str_Sol[6] = ["ln(a)","b"]
        str_equation = str(Sround(exp(float(Str_Sol[indm][0])),r)) + " * x^(" + Str_Sol[indm][1] + ")"
    else:
        #The linearized form is the original form itself
        str_equation = RHS[indm]
    err_copy=reg_errors.copy()
    err_copy.pop(indm);

    return str_equation,forms[indm],reg_errors[indm],Sround(np.std(err_copy),r)


def main():
    repeat = True
    while (repeat):
            # Picking a choice:
            Choice = input(
                "Type \"N\" to curve fit using nonlinear least squares method, \"L\" to curve fit using linear least squares method,  \"S\" for surface fitting through linear least squares method, \"D\"  to detect a curve family given a data set: ")
            Choice=Choice.upper()

            if (Choice == 'N'):
                  r = int(input("Round the results to how many decimals ? :\n "))
                  xdata,ydata=Input_2D()
                  NonlinearFunction = input("Type in the Nonlinear Function : \n")
                  Sol,Sr=Nonlinear_Regression(xdata,ydata,NonlinearFunction,r)
                  if(Sol !=''):
                    print(Sol,'\n')
                    print("Regression Error(Sr)= ", Sr);
                    Nonlinear_Plot(xdata, ydata, Sol)
                  else:
                    print(" Levenberg-Marquardt requires a data set that has length larger than or equal to the no. of constants")
            elif (Choice == 'L'):
                r = int(input("Round the results to how many decimals ? :\n "))
                xdata, ydata = Input_2D()
                n = int(input(
                    "Type in the no. of functions in your linearized form Ex. Sin(x/y)=a*(x^2)+b*tan(x)+c/x involves 4 functions : "))
                Function = []
                for i in range(0, n):
                    Function.append(input("Insert your functions Y, X1, X2... : \n"))
                LHS, RHS, Constants, Sr = Linearized_Regression(xdata, ydata, Function, r)
                print(LHS, '=', RHS);
                print("Regression Error(Sr)= ", Sr);
                St = TrueError(ydata, r);
                print("True Error(St)= ", St);
                corrolation_coeff = Sround(sqrt((abs(St - Sr)) / St), r)
                print("Corrolation Coeffecient(r)= ", corrolation_coeff);
                Plot_2D_RHS(xdata, ydata, RHS, LHS)
            elif (Choice == 'S'):
                r = int(input("Round the results to how many decimals ? :\n "))
                xdata, ydata, zdata = Input_3D()
                n = int(input(
                    """Type in the no. of functions, Ex. the paraboloid : Z= f(x, y) = A * x^2 +B* x*y + C*y^2 + D*x + E*y + H corresponds to seven functions  z,x^2,x*y,y^2,x,y,1 : \n"""))
                Function = []
                for i in range(0, n):
                    Function.append(input("Insert your functions : \n"))
                LHS, RHS, Constants,Sr = Surface_Fit_Beta(xdata, ydata, zdata, Function, r);
                if(LHS==''):
                    print("Singular Matrix")
                print(LHS, '=', RHS,'\n');
                print("Regression Error(Sr)= ", Sr);
                Plot_3D_RHS(xdata, ydata, zdata, RHS)
            elif (Choice == 'D'):
                r = int(input("Round the results to how many decimals ? :\n "))
                xdata, ydata = Input_2D()
                str_equation, formula_Family, Sr,STnD= Curve_Family_Detective(xdata, ydata, r)
                print("The data set is related the most to the family of " + formula_Family + " curves: \n")
                print(str_equation,'\n')
                print("with a Regression Error(Sr) of ", Sr,'\n');
                print("The standard deviation of regression errors due to other families is " ,STnD , " \n")
                St = TrueError(ydata, r);
                #print("True Error(St)= ", St);
                corrolation_coeff = Sround(sqrt((abs(St - Sr)) / St), r)
                #print("and a Corrolation Coeffecient(r)= ", corrolation_coeff);
            elif (Choice == 'Q'): #Was trying non_linear curve fit for the detective and a+b*sin(c*x+d)
                r = int(input("Round the results to how many decimals ? :\n "))
                xdata, ydata = Input_2D()
                str_equation_m, formula_Family_m, Sr_m,ST = Curfe_Vamily_Detective(xdata, ydata, r)
                if(formula_Family_m=='0'):
                    print("Data sample is very small, please try again.")
                else:
                    print("The data set is best described by the family of " + formula_Family_m + " curves: \n")
                    print('y=',str_equation_m,'\n')
                    print("with a Regression Error(Sr) of ", Sr_m,'\n');
                    print("The standard deviation of regression errors due to other families is " ,ST , " \n")

                St = TrueError(ydata, r);
                #print("True Error(St)= ", St);
                corrolation_coeff = Sround(sqrt((abs(St - Sr_m)) / St), r)
                #print("and a Corrolation Coeffecient(r)= ", corrolation_coeff);

            else:
                print("You entered an invalid symbol")
            again = input("Do you want another try? type \"Y\" or \"N\": \n")
            if (again.lower() == "y"):
                repeat = True
            else:
                repeat = False
#main()
