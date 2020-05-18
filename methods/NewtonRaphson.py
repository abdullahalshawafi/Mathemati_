import cmath
import math
import numpy as np
from sympy import var
from sympy import sympify
import sympy

#Defining variables to replace the characters x,y & z
x = var('x')
y = var('y')
z = var('z')

def Newton_Raphson(num,iterations,exp1,exp2,exp3,xval,yval,zval,Es):
    exp1=sympify(exp1)
    exp2=sympify(exp2)
    exp3=sympify(exp3)
    Storage=[[0 for x in range(1)] for y in range(num*iterations)]
    Error = [[0 for x in range(1)] for y in range(num)]
    Approximate_Error =  [[0 for x in range(1)] for y in range(iterations)]
    Ea = 1000
    dim1=0
    number=iterations
    counter=0;
    while iterations!=0:
     if (Ea<Es):
      print("Ea<Es: Stopping Criteria Reached")
      break;
     print("At iteration number",number-iterations,"  r=",number-iterations,":")
     expression =exp1
     Jacob_Matrix = [[0 for x in range(num)] for y in range(num)]
     for i in range(num):
      if i==0:
         expression=exp1
      if i==1:
        expression=exp2
      if i==2:
        expression=exp3
      for j in range(num):
        if num==1: #if the num of variable is 1 we will make the steps w.r.t x only
           Jacob_Matrix[i][j]=sympy.diff(expression,x)
           Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval)])
        if num==2: #if the num of variable is 2 we will make the steps w.r.t x & y
          if j==0:
            Jacob_Matrix[i][j]=sympy.diff(expression,x)
            Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval),(y,yval)])
          if j==1:
            Jacob_Matrix[i][j]=sympy.diff(expression,y)
            Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval),(y,yval)])
        if num==3: #if the num of variable is 3 we will make the steps w.r.t x & y & z
          if j==0:
            Jacob_Matrix[i][j]=sympy.diff(expression,x)
            Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval),(y,yval),(z,zval)])
          if j==1:
            Jacob_Matrix[i][j]=sympy.diff(expression,y)
            Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval),(y,yval),(z,zval)])
          if j==2:
            Jacob_Matrix[i][j]=sympy.diff(expression,z)
            Jacob_Matrix[i][j]=Jacob_Matrix[i][j].subs([(x,xval),(y,yval),(z,zval)])

    #getting the Matrix of functions & the matrix of inverse jacobian & the matrix with XYZ values
     FunctionMatrix=[[0 for x in range(1)] for y in range(num)]
     Jacob_MatrixInv= [[0 for x in range(num)] for y in range(num)]
     XYZprev=[[0 for x in range(1)] for y in range(num)]
     if num==1:
      Jacob_Matrix=np.array([[float(Jacob_Matrix[0][0])]])
      FunctionMatrix[0][0]=exp1.subs([(x,xval)])
      XYZprev[0][0]=float(xval)
     if num==2:
      Jacob_Matrix=np.array([[float(Jacob_Matrix[0][0]),float(Jacob_Matrix[0][1])],[float(Jacob_Matrix[1][0]),float(Jacob_Matrix[1][1])]])
      FunctionMatrix[0][0]=exp1.subs([(x,xval),(y,yval)])
      FunctionMatrix[1][0]=exp2.subs([(x,xval),(y,yval)])
      XYZprev[0][0]=float(xval)
      XYZprev[1][0]=float(yval)
     if num==3:
      Jacob_Matrix=np.array([[float(Jacob_Matrix[0][0]),float(Jacob_Matrix[0][1]),float(Jacob_Matrix[0][2])],[float(Jacob_Matrix[1][0]),float(Jacob_Matrix[1][1]),float(Jacob_Matrix[1][2])],[float(Jacob_Matrix[2][0]),float(Jacob_Matrix[2][1]),float(Jacob_Matrix[2][2])]])
      FunctionMatrix[0][0]=exp1.subs([(x,xval),(y,yval),(z,zval)])
      FunctionMatrix[1][0]=exp2.subs([(x,xval),(y,yval),(z,zval)])
      FunctionMatrix[2][0]=exp3.subs([(x,xval),(y,yval),(z,zval)])
      XYZprev[0][0]=float(xval)
      XYZprev[1][0]=float(yval)
      XYZprev[2][0]=float(zval)


     Jacob_MatrixInv= [[0 for x in range(num)] for y in range(num)]
     if np.linalg.det(Jacob_Matrix)!=0:
       Jacob_MatrixInv=np.linalg.inv(Jacob_Matrix)
     else:
        print("ERROR! The Jacobian Determinant Equals Zero Can't Get Its Inverse")
        break;
     Main=Jacob_MatrixInv.dot(FunctionMatrix)  #multiplying the jacobian inverse with the matrix function

    #the last step to calculate the new XYZ values
     XYZnew=[[0 for x in range(1)] for y in range(num)]

     for i in range(num):
      XYZnew[i][0]=XYZprev[i][0]-Main[i][0]
      if i==0:
        xval=XYZnew[i][0]
      if i==1:
        yval=XYZnew[i][0]
      if i==2:
        zval=XYZnew[i][0]
    #storing the values
     for j in range(num):
         Storage[dim1][0]=XYZnew[j][0]
         Error[j][0] = (abs(XYZnew[j][0]-XYZprev[j][0])/XYZnew[j][0])*100
         dim1=dim1+1
     Ea = np.max(Error)
     Approximate_Error[number-iterations] = Ea
    #printing the outputs of the new values XYZ (won't affect function if removed)
     if num==1:
      print ("x=",xval,"Ea=", Approximate_Error[number-iterations] )
     elif num==2:
      print ("x=",xval,"  y=",yval,"Ea=", Approximate_Error[number-iterations])
     elif num==3:
      print ("x=",xval,"  y=",yval,"  z=",zval, "Ea=",Approximate_Error[number-iterations])
     iterations=iterations-1
     counter = counter +1

    # end of while loop
    RealStorage=[[0 for x in range(1)] for y in range(num*counter)]
    Real_Approximate_Error =  [[0 for x in range(1)] for y in range(counter)]

    for j in range (num*counter):
      RealStorage[j][0]= round(Storage[j][0], 4)
    for j in range(counter):
      Real_Approximate_Error[j] = round(Approximate_Error[j], 4)
    return RealStorage ,Real_Approximate_Error
#End of function
