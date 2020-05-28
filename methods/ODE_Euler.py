from typing import Any
from math import pow,log,exp,sin,cos,tan,atan,acos,asin,sqrt,log10,pi
from sympy import *
from sympy import symbols
import plotly.graph_objects as go
import numpy as np
#from matplotlib import pyplot as plt
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import sympy as sym
from math import *
from math import fabs
ch=int(input("For Euler, Enter (1) and for Heun, Enter (2) : "))
if(ch==1):
 print(" -----------------------------------------------------------------------------------------------------------------")
 print(" |for example :"
     "f=3y+z----> 3*y+z //y=x^2 -----> Pow(x,2) // y=ln(x^2) ----> log(exp(1),Pow(x,2)) // e^2 --> exp(2)  .. etc |")
 print(" ------------------------------------------------------------------------------------------------------------------")
#********************************************
 x = symbols('x')
 y = symbols('y')
 z = symbols('z')
 num_eq=int(input("How many equations do you want to solve?"))

 # creation of the function
 def func(m_eq,x,y):
     e = lambda x, y: eval(m_eq)
     return e(x, y)


 def func_xyz(m_eq, x, y,z):
     e = lambda x,y,z: eval(m_eq)
     return e(x,y,z)

 # To know whether the user want to calculate the error or not
 calc = str(input(
     "If you want to claculate the Truncation error enter yes, if not enter no, (be careful it's case sensitive ) "))
 if (calc == "yes"):
     num = int(input(" enter number of terms to stop at ="))
 # Function for euler formula
 def euler(eq,x0, yp, h, xp):
     temp = 0
     y0 = yp
     print("******************")
     # Iterating till the point at which we need approximation
     i = 1
     sum = 0
     fun=eq
     y_prime = fun
     x_prime = fun
     tempf = fun
     while x0 < xp:
         temp = yp
         yp = yp + h * func(eq,x0, yp)
         if (calc == "yes"):
             if ("y" in eq):
                 y_prime = Derivative(fun,x)
                 y_p = y_prime.doit().subs({x: x0, y: temp})
                 tempf = lambdify([x,y],fun)
                 x_prime = Derivative(fun, y)
                 x_p = x_prime.doit().subs({x: x0, y: temp}) * tempf(x0,temp)
                 prime = y_p + x_p
                 sum = pow(h, 2) * prime.doit() / np.math.factorial(2)
             else:
                 nu = 1
                 prime = fun
                 while (nu <= num):
                     prime = Derivative(prime,x)
                     sum += (pow(h, nu + 1) * prime.doit().subs({x: x0}) / np.math.factorial(nu + 1))
                     nu = nu + 1
         x0 = x0 + h
         x0 = float("{:.1f}".format(x0))
         print("Approximate solution at x = ", x0, "-->", "Y=", "%.6f" % yp)
         if (calc == "yes"):
             print("the approximate error is = ", sum)
     out = yp

     print("******************")


     return (out, x0)
 def euler2(eq1,eq2, yi, zi, h):

     print("******************")
     # Iterating till the point at which we need approximation
     yn = yi + h * func_xyz(eq1,h,yi, zi)
     zn = zi + h * func_xyz(eq2,h, yi, zi)
     print("Approximate solution at x = ", h, "-->", "Y=", "%.6f" % yn)
     print("Approximate solution at x = ", h, "-->", "Z=", "%.6f" % zn)

     outy = yn
     outz = zn

     print("******************")


     return (outy, outz,h)
 def euler3(eq1,eq2,eq3,xi,yi,zi, h):

     print("******************")

     xn= xi +  h * func_xyz(eq1,xi,yi,zi)
     yn = yi + h * func_xyz(eq2,xi,yi,zi)
     zn = zi + h * func_xyz(eq3,xi, yi, zi)
     print("Approximate solution at h = ", h, "-->", "X=", "%.6f" % xn)
     print("Approximate solution at h = ", h, "-->", "Y=", "%.6f" % yn)
     print("Approximate solution at h = ", h, "-->", "Z=", "%.6f" % zn)
     outx = xn
     outy = yn
     outz = zn

     print("******************")


     return (outx,outy, outz,h)

 # Initial Values
 if (num_eq ==1):
  equation = input("Enter your equation here :f(x,y)=")
  x0 = float(input(" enter Xo ="))
  x0 = float("{:.1f}".format(x0))
  y0 = float(input(" enter Yo ="))
  y0 = float("{:.1f}".format(y0))
 # *******************************
 # Value of x at which we need approximation
  xt = float(input(" enter X value to evaluate Y  at , x ="))
  xt = float("{:.1f}".format(xt))  # round to one decimal
 # ***************************************
  choice = str(input(" want to enter stepsize (h) or number of steps (n), enter h or n ="))
  h = 0
  n = 0
  if choice == "h":
     h = float(input(" enter stepsize (h) ="))
     n = 0
  elif choice == "n":
     n = float(input(" enter number of steps(n) ="))
     h = float(xt - x0) / float(n)
     # **********************************

  (out, xin) = euler(equation,x0, y0, h, xt)
  choice = str(input(" want to evaluate at another(enter yes or no)--> ="))
  while choice == "yes":  # for more than one value of x to calculate at
     x2 = float(input(" enter X value to evaluate Y at ="))
     x2 = float("{:.2f}".format(x2))  # round to one decimal
     if n == 0:
         h = h
     else:
         h = float(x2 - xt) / float(n)
     out, xin = euler(xin, out, h, x2)
     choice = str(input(" want to evaluate at another (enter yes or no)-->="))
 elif (num_eq==2):
  equation1 = input("Enter your first equation here :Y'=")
  equation2 = input("Enter your second equation here :Z'=")
  x0 = float(input(" enter Xo ="))
  x0 = float("{:.1f}".format(x0))
  y0 = float(input(" enter Yo ="))
  y0 = float("{:.1f}".format(y0))
  z0 = float(input(" enter Z0 ="))
  z0 = float("{:.1f}".format(z0))
 # *******************************
 # Value of x at which we need approximation
  xt = float(input(" enter X value to evaluate Y and Z at , x ="))
  xt = float("{:.1f}".format(xt))  # round to one decimal
 # ***************************************
  (out1, out2,s1) = euler2(equation1,equation2,y0, z0, float(xt-x0))

  choice = str(input(" want to evaluate at another x (enter yes or no)--> ="))
  while choice == "yes":  # for more than one value of x to calculate at
     x2 = float(input(" enter X value to evaluate Y and Z at ="))
     x2 = float("{:.2f}".format(x2))  # round to one decimal
     out1, out2,s1 =euler2(equation1,equation2,out1, out2, x2-s1)
     choice = str(input(" want to evaluate at another (enter yes or no)-->="))
 elif (num_eq==3):
  equation1 = input("Enter your first equation here :X'=")
  equation2 = input("Enter your second equation here :Y'=")
  equation3 = input("Enter your third equation here :Z'=")
  x0 = float(input(" enter Xo ="))
  x0 = float("{:.1f}".format(x0))
  y0 = float(input(" enter Yo ="))
  y0 = float("{:.1f}".format(y0))
  z0 = float(input(" enter Z0 ="))
  z0 = float("{:.1f}".format(z0))
 # *******************************
 # Value of x at which we need approximation
  xt = float(input(" enter step size value to evaluate X, Y and Z at , h ="))
  xt = float("{:.1f}".format(xt))  # round to one decimal
 # ***************************************
  (out1, out2,out3,s1) = euler3(equation1,equation2,equation3,x0,y0, z0,xt)

  choice = str(input(" want to evaluate at another h (enter yes or no)--> ="))
  while choice == "yes":  # for more than one value of x to calculate at
     x2 = float(input( "enter step size value to evaluate X, Y and Z at , h ="))
     x2 = float("{:.2f}".format(x2))  # round to one decimal
     out1, out2,out3,s1 =euler3(equation1,equation2,equation3,out1, out2,out3,x2)
     choice = str(input(" want to evaluate at another (enter yes or no)-->="))


else:
    x, y ,z,w,u= sym.symbols('x,y,z,w,u')
    run = "yes"
#1-->  6 output lines explaining the input criteria
    print("Criteria of entering the functions : You can enter the function just like the calculator except for :")
    print("1-for  e^x --> exp(x)")
    print("2-for multiplication like : 4x --> 4*x , xy--> x*y, xsinh(x)--> x*sinh(x), xsin(y)--> x*sin(y),etc.. ")
    print("3-for log2(x)--->log(x,2.0), logx(2)---> log(2.0,x), log(x)--->log(x,10.0), but (ln) could be entered normally -->ln(x) or ln(x^3)")
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

    while run == "yes":
#2--> asking for the degree of the ODE
     l=int(input("Want to solve 1st (1), 2nd (2), 3rd (3) or 4th (4) ODE : "))
     if(l==1):
#2.1--> asking for number of equations
        q = int(input("Want to solve 1 equation (1) or 2 simultinuous equations (2) : "))
        if(q==1):
#2.1.1--> asking for the equation, x0,y0,x1, stopping condition-->  5 inputs & 1 output
            f = input("Please,  Enter y' : ")
            x0 = float(input("         Enter x0 : "))
            y0 = float(input("         Enter y({}) : ".format(x0)))
            x1 = float(input("         Enter x at which you want to calculate y :"))
            m = input("         Enter level of approximation (n) or Stopping error% (e) : ")
            print("********************************************************************************")
            h = x1 - x0
            f = simplify(f)
            y2 = y0
            y1=0
            r0 = f.subs({x: x0, y: y0})
            r = r0
            if(m=='n'):
# 2.1.1.1-> asking for number of iterations
             n=int(input("         Enter n : "))
             for i in range(n):
                y2 = y0 + h * r
                r = (r0 + f.subs({x: x1, y: y2})) / 2.0
                ea=fabs((y2-y1)/y2)*100
#2.1.1.2--> every iteration-> output y & Ea at i
                print("At i={} --> y={} ,  Ea%={}%".format(i+1,y2,ea))
                y1=y2
            else:
#2.1.2.1--> enter stoping error
             e=float(input("         Enter e : "))
             ea=9000
             i=1
             while ea>e:
                y2 = y0 + h * r
                r = (r0 + f.subs({x: x1, y: y2})) / 2.0
                ea = fabs((y2 - y1) / y2) * 100
#2.1.2.2--> every iteration-> output y & Ea at i
                print("At i={} --> y={} ,  Ea%={}%".format(i, y2, ea))
                y1 = y2
                i+=1
#2.2--> output final answer of y
            print("y({})={}".format(x1,y2))
        else:
            f1 = input("Please,  Enter y' : ")
            f2 = input("Please, Enter Z' : ")
            x0 = float(input("         Enter x0 : "))
            y0 = float(input("         Enter y0 : "))
            z0 = float(input("         Enter z0 : "))
            x1 = float(input("         Enter x at which you want to calculate y and z :"))
            m = input("         Enter level of approximation(n) or Stopping error% (e) : ")
            print("********************************************************************************")
            h = x1 - x0
            f1 = simplify(f1)
            f2 = simplify(f2)
            y2 = y0
            y1 = 0
            z2 = y0
            z1 = 0
            r01 = f1.subs({y: y0, z: z0})
            r02 = f2.subs({y: y0, z: z0})
            r1 = r01
            r2 = r02
            if (m == 'n'):
                n = int(input("         Enter n : "))
                for i in range(n):
                    y2 = y0 + h * r1
                    z2 = z0 + h * r2
                    r1 = (r01 + f1.subs({y: y2, z: z2})) / 2.0
                    r2 = (r02 + f2.subs({y: y2, z: z2})) / 2.0
                    ea1 = fabs((y2 - y1) / y2) * 100
                    ea2 = fabs((z2 - z1) / z2) * 100
                    print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea1))
                    print("At i={} --> z={} ,  Ea%={}%".format(i + 1, z2, ea2))
                    y1 = y2
                    z1 = z2
            else:
                e = float(input("         Enter e : "))
                ea1 = 9000
                ea2 = 9000
                i = 1
                while ea1 > e and ea2 > e:
                    y2 = y0 + h * r1
                    z2 = z0 + h * r2
                    r1 = (r01 + f1.subs({y: y2, z: z2})) / 2.0
                    r2 = (r02 + f2.subs({y: y2, z: z2})) / 2.0
                    ea1 = fabs((y2 - y1) / y2) * 100
                    ea2 = fabs((z2 - z1) / z2) * 100
                    print("At i={} --> y={} ,  Ea%={}%".format(i, y2, ea1))
                    print("At i={} --> z={} ,  Ea%={}%".format(i, z2, ea2))
                    y1 = y2
                    z1 = z2
                    i += 1
            print("y={}".format(y2))
            print("z={}".format(z2))
     elif l == 2:
#All the coming is the same as l=1 & q=1 but every time addinal input is required y'->l=2 , y" -> l=3 ,y"'->l=4
            f = input("Please,  Enter y\" ( substituting y' ---> z ): ")
            x0 = float(input("         Enter x0 : "))
            y0 = float(input("         Enter y({}) : ".format(x0)))
            z0 = float(input("         Enter y'({}) : ".format(x0)))
            x1 = float(input("         Enter x at which you want to calculate y & y' : "))
            m = input("         Enter level of approximation (n) or Stopping error% (e) : ")
            print("********************************************************************************")
            h = x1 - x0
            f = simplify(f)
            r0 = f.subs({x: x0, y: y0, z: z0})
            y2 = y0 + h * z0
            z1 = z0 + h * r0
            y1 = y2
            r = f.subs({x: x1, y: y2, z: z1})
            # solving for n iterations
            if (m == 'n'):
                n = int(input("         Enter n : "))
                for i in range(n):
                    y2 = y0 + h * (z0 + z1) / 2.0
                    z1 = z0 + h * (r0 + r) / 2.0
                    r = f.subs({x: x1, y: y2, z: z1})
                    ea = fabs((y2 - y1) / y2) * 100
                    print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
                    y1 = y2
            else:
                # solving until stopping error e%
                e = float(input("         Enter e : "))
                ea = 9000
                i = 1
                while ea > e:
                    y2 = y0 + h * (z0 + z1) / 2.0
                    z1 = z0 + h * (r0 + r) / 2.0
                    r = f.subs({x: x1, y: y2, z: z1})
                    ea = fabs((y2 - y1) / y2) * 100
                    print("At i={} --> y={} ,  Ea%(y)={}%".format(i, y2, ea))  # printing y,Ea at every i
                    y1 = y2
                    i += 1
            print("y({})={} , y'({})={}".format(x1, y2, x1, z1))
     elif l == 3:
        f = input("Please,  Enter y\"' ( substituting y' ---> z , y\" --->w): ")
        x0 = float(input("         Enter x0 : "))
        y0 = float(input("         Enter y({}) : ".format(x0)))
        z0 = float(input("         Enter y'({}) : ".format(x0)))
        w0 = float(input("         Enter y\"({}) : ".format(x0)))
        x1 = float(input("         Enter x at which you want to calculate y & y' & y\" : "))
        m = input("         Enter level of approximation(n) or Stopping error% (e) : ")
        print("********************************************************************************")
        h = x1 - x0
        f = simplify(f)
        r0 = f.subs({x: x0, y: y0, z: z0, w: w0})
        y2 = y0 + h * z0
        z1 = z0 + h * w0
        w1 = w0 + h * r0
        y1 = y2
        r = f.subs({x: x1, y: y2, z: z1, w: w1})
        # solving for n iterations
        if (m == 'n'):
            n = int(input("         Enter n : "))
            for i in range(n):
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (w0 + w1) / 2.0
                w1 = w0 + h * (r0 + r) / 2.0
                r = f.subs({x: x1, y: y2, z: z1, w: w1})
                ea = fabs((y2 - y1) / y2) * 100
                print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
                y1 = y2
        else:
            # solving until stopping error e%
            e = float(input("         Enter e : "))
            ea = 9000
            i = 1
            while ea > e:
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (w0 + w1) / 2.0
                w1 = w0 + h * (r0 + r) / 2.0
                r = f.subs({x: x1, y: y2, z: z1, w: w1})
                ea = fabs((y2 - y1) / y2) * 100
                print("At i={} --> y={} ,  Ea%(y)={}%".format(i, y2, ea))  # printing y,Ea at every i
                y1 = y2
                i += 1
        print("y({})={} , y'({})={} , y\"({})={}".format(x1, y2, x1, z1, x1, w1))
     else:
         f = input("Please,  Enter y\"\" ( substituting y' --> z , y\" -->w , y\"' -->u ): ")
         x0 = float(input("         Enter x0 : "))
         y0 = float(input("         Enter y({}) : ".format(x0)))
         z0 = float(input("         Enter y'({}) : ".format(x0)))
         w0 = float(input("         Enter y\"({}) : ".format(x0)))
         u0 = float(input("         Enter y\"'({}) : ".format(x0)))
         x1 = float(input("         Enter x at which you want to calculate y & y' & y\" & y\"' : "))
         m = input("         Enter level of approximation(n) or Stopping error% (e) : ")
         print("********************************************************************************")
         h = x1 - x0
         f = simplify(f)
         r0 = f.subs({x: x0, y: y0, z: z0, w: w0, u: u0})
         y2 = y0 + h * z0
         z1 = z0 + h * w0
         w1 = w0 + h * u0
         u1 = u0 + h * r0
         y1 = y2
         r = f.subs({x: x1, y: y2, z: z1, w: w1, u: u1})
         # solving for n iterations
         if (m == 'n'):
             n = int(input("         Enter n : "))
             for i in range(n):
                 y2 = y0 + h * (z0 + z1) / 2.0
                 z1 = z0 + h * (w0 + w1) / 2.0
                 w1 = w0 + h * (u1 + u0) / 2.0
                 u1 = u0 + h * (r0 + r) / 2.0
                 r = f.subs({x: x1, y: y2, z: z1, w: w1, u: u0})
                 ea = fabs((y2 - y1) / y2) * 100
                 print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
                 y1 = y2
         else:
             # solving until stopping error e%
             e = float(input("         Enter e : "))
             ea = 9000
             i = 1
             while ea > e:
                 y2 = y0 + h * (z0 + z1) / 2.0
                 z1 = z0 + h * (w0 + w1) / 2.0
                 w1 = w0 + h * (u1 + u0) / 2.0
                 u1 = u0 + h * (r0 + r) / 2.0
                 r = f.subs({x: x1, y: y2, z: z1, w: w1, u: u0})
                 ea = fabs((y2 - y1) / y2) * 100
                 print("At i={} --> y={} ,  Ea%(y)={}%".format(i, y2, ea))  # printing y,Ea at every i
                 y1 = y2
                 i += 1
         print("y({})={} , y'({})={} , y\"({})={} , y\"'({})={}".format(x1, y2, x1, z1, x1, w1, x1, u1))
     run = input("If you want to calculate y at another x, Enter (yes), otherwise, Enter any thing else : ")




