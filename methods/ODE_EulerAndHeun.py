from typing import Any
from math import pow,log,exp,sin,cos,tan,atan,acos,asin,sqrt,log10
from sympy import *
from sympy import symbols
#import plotly.graph_objects as go
import numpy as np
from sympy.interactive import printing
#printing.init_printing(use_latex=True)
import sympy as sym
from math import *
from math import fabs

 # creation of the functions
#//////////////////////////////
def func(m_eq,x,y):
     e = lambda x, y: eval(m_eq)
     return e(x, y)
#////////////////////////////////
def func_xyz(m_eq, x, y,z):
     e = lambda x,y,z: eval(m_eq)
     return e(x,y,z)


def func_xyzt(m_eq, x, y, z,t):
    e = lambda x, y, z,t: eval(m_eq)
    return e(x, y, z,t)


#////////////used symbols////////////////////
x = symbols('x')
y = symbols('y')
z = symbols('z')
t = symbols('t')
############################################ Helper functions #####################################################################
#####################EULER 1 eqs ############################
 # Function for euler1 formula
def euler(num,eq,x0, yp, h, xp):
     ##### outputs #####
     List_x_values=[]
     List_y_values=[]
     List_approx_error=[]
     ###############
     temp = 0
     y0 = yp
     i = 1
     sum = 0
     fun=eq
     y_prime = fun
     x_prime = fun
     tempf = fun
     # Iterating till the point at which we need approximation
     while x0 < xp:
         temp = yp
         yp = yp + h * func(eq,x0, yp)
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
        # print("Approximate solution at x = ", x0, "-->", "Y=", "%.6f" % yp)
         List_x_values.append(x0)
         List_y_values.append(yp)
         List_approx_error.append(sum)
     out = yp
     return (out, x0,List_x_values,List_y_values,List_approx_error,sum)
 #/////////////////////////////////////////Euler 2eqs///////////////////////////////////////////////////

def euler2(num,eq1,eq2, yi, zi,h,x0):
     #################################
     error_y=0
     error_z=0

     #################################
     equation1=eq1
     equation2=eq2
     ###################################
     # Iterating till the point at which we need approximation
     yn = yi + h * func_xyz(eq1,x0,yi, zi)
     temp_f1=lambdify([x,y,z],equation1)
     y_prime1= Derivative(equation1,y)
     y_prime1=temp_f1(x0,yi,zi)*y_prime1.doit().subs({x:x0,y:yi,z:zi})
     temp_f2=lambdify([x,y,z],equation2)
     y_prime2=Derivative(equation1,z)
     y_prime2=temp_f2(x0,yi,zi)*y_prime2.doit().subs({x:x0,y:yi,z:zi})
     y_prime3=Derivative(equation1,x)
     y_prime3=y_prime3.doit().subs({x:x0,y:yi,z:zi})
     y_p=y_prime1+y_prime2+y_prime3
     error_y=pow(h,2)*y_p.doit()/2.0
     zn = zi + h * func_xyz(eq2,x0, yi, zi)
     z_prime1=Derivative(equation2,z)
     z_prime1=temp_f2(x0,yi,zi)*z_prime1.doit().subs({x:x0,y:yi,z:zi})
     z_prime2=Derivative(equation2,y)
     z_prime2=temp_f1(x0,yi,zi)*z_prime2.doit().subs({x:x0,y:yi,z:zi})
     z_prime3=Derivative(equation2,x)
     z_prime3=z_prime3.doit().subs({x:x0,y:yi,z:zi})
     z_p=z_prime1+z_prime2+z_prime3
     #print("Approximate solution at x = ", h, "-->", "Y=", "%.6f" % yn)

     #print("Approximate solution at x = ", h, "-->", "Z=", "%.6f" % zn)
     error_z = pow(h, 2) * z_p.doit() /2.0

     outy = yn
     outz = zn
     return (outy, outz,error_y,error_z,)
###############################################EULER3 eqs#########################################################
def euler3(num,eq1,eq2,eq3,ti,yi,zi,xi,h):
     error_t = 0
     error_y = 0
     error_z = 0
     #*********************************
     equation1 = eq1
     equation2 = eq2
     equation3 = eq3
     #********************************
     tn= ti + h * func_xyzt(eq1,xi,yi,zi,ti)
     temp_f1=lambdify([x,y,z,t],equation1)
     temp_f2 =lambdify([x,y,z,t],equation2)
     temp_f3=lambdify([x,y,z,t],equation3)
     t_prime=Derivative(equation1,t)
     t_p=t_prime.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f1(xi,yi,zi,ti)
     t_prime2=Derivative(equation1,y)
     t_p+=(t_prime2.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f2(xi,yi,zi,ti))
     t_prime3=Derivative(equation1,z)
     t_p+=(t_prime3.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f3(xi,yi,zi,ti))
     temp_f4=Derivative(equation1,x)
     t_p+=(temp_f4.doit().subs({x:xi,y:yi,z:zi,t:ti}))
     yn = yi + h * func_xyzt(eq2,xi,yi,zi,ti)
     t_prime=Derivative(equation2,y)
     y_p=t_prime.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f2(xi,yi,zi,ti)
     t_prime2 = Derivative(equation2,t)
     y_p+=(t_prime2.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f1(xi,yi,zi,ti))
     t_prime3=Derivative(equation2,z)
     y_p+=(t_prime3.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f3(xi,yi,zi,ti))
     temp_f4=Derivative(equation2,x)
     y_p+=temp_f4.doit().subs({x:xi,y:yi,z:zi,t:ti})
     zn = zi + h * func_xyzt(eq3,xi, yi, zi,ti)
     t_prime=Derivative(equation3,t)
     z_p=t_prime.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f1(xi,yi,zi,ti)
     t_prime2=Derivative(equation3,y)
     z_p+=(t_prime2.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f2(xi,yi,zi,ti))
     t_prime3=Derivative(equation3,z)
     z_p+=(t_prime3.doit().subs({x:xi,y:yi,z:zi,t:ti})*temp_f3(xi,yi,zi,ti))
     temp_f4=Derivative(equation3,x)
     z_p+=temp_f4.doit().subs({x:xi,y:yi,z:zi,t:ti})


     error_t=t_p.doit()*pow(h,2)/2.0

     error_y = y_p.doit() * pow(h, 2) / 2.0

     error_z = z_p.doit() * pow(h, 2) / 2.0
     outt = tn
     outy = yn
     outz = zn

     return (outt,outy, outz,error_t,error_y,error_z)

############################################################################
############################################### Main func of euler ##################################################################
def Solve_Euler(num_eqs,eq1,eq2,eq3,xnod,ynod,znod,tnod,X_at,h_Or_n,h,n):
      Error_num_steps=1
      #****************
      y_out=0
      x_out=0
      z_out=0
      t_out=0
      t_error=0
      y_error = 0
      z_error = 0
      List_x_values=[]
      List_y_values=[]
      List_z_values = []
      List_approx_y_error=[]
      List_approx_z_error = []
      List_approx_t_error = []
      # Initial Values
      if (num_eqs == 1):
        equation = str(eq1)
        x0 =float(xnod)
        #x0 = float("{:.1f}".format(x0))
        y0 =float(ynod)
        #y0 = float("{:.1f}".format(y0))
        # *******************************
        # Value of x at which we need approximation
        xt =float(X_at)
        #xt = float("{:.1f}".format(xt))  # round to one decimal
        # ***************************************
        choice = str(h_Or_n)
        if choice == "h":
            h =h
            n = 0
        elif choice == "n":
            n =float(n)
            h = float(xt - x0) / float(n)
        else:
            h=float(xt - x_out)
            # **********************************
        (y_out, x_out,List_x_values,List_y_values,List_approx_y_error,y_error) = euler(Error_num_steps,equation, x0, y0, h, xt)


      elif (num_eqs == 2):
        equation1 =eq1
        equation2 =eq2
        x0 = float(xnod)
        #x0 = float("{:.1f}".format(x0))
        y0 = float(ynod)
        #y0 = float("{:.1f}".format(y0))
        z0 = float(znod)
        #z0 = float("{:.1f}".format(z0))
        # *******************************
        # Value of x at which we need approximation
        xt = float(X_at)
        x_out=xt
        #xt = float("{:.1f}".format(xt))  # round to one decimal
        # ***************************************
        (y_out,z_out,y_error,z_error) = euler2(Error_num_steps,equation1, equation2, y0, z0, float(xt - x0),x0)

##########################################################################
      elif (num_eqs == 3):
        equation1 = eq1
        equation2 = eq2
        equation3 = eq3
        x0 = float(xnod)
        #x0 = float("{:.1f}".format(x0))
        t0 = float(tnod)
        #t0 = float("{:.1f}".format(t0))
        y0 = float(ynod)
        #y0 = float("{:.1f}".format(y0))
        z0 = float(znod)
        #z0 = float("{:.1f}".format(z0))
        # *******************************
        # Value of x at which we need approximation
        xp = float(X_at)
        x_out=xp
        #xp = float("{:.1f}".format(xp))  # round to one decimal

        # ***************************************
        (t_out, y_out, z_out,t_error,y_error,z_error ) = euler3(Error_num_steps,equation1, equation2, equation3, t0, y0, z0,float(xp-x0),x0)

      return(y_out,
      x_out,
      z_out,
      t_out,
      t_error,
      y_error,
      z_error,
      List_x_values,
      List_y_values,
      List_z_values,
      List_approx_y_error,
      List_approx_z_error,
      List_approx_t_error)
############################################################################################
#////////////////////////////////////////////////////////////////////////////////////////////
                           #HEUN's Method
#//////////////////////////////////////////////////////////////////////////////////////////
##############################helper functions for  Heun #################################################

x, y, z, w, u = sym.symbols('x,y,z,w,u')

    ########################for Heun 3 ODE ###################################
def Heun3(eq,exact_y,x0,y0,z0,w0,xf,h,m,n,e):
       #********
        List_num_iterations=[]
        List_y_values =[]
        List_relative_y_errors = []
        List_y_dash_values=[]
        List_y_d_dash_values=[]
        y_value=0
        y_dash=0
        y_d_dash=0
        true_error=0
       #*********
        f = simplify(eq)
        r0 = f.subs({x: x0, y: y0, z: z0, w: w0})
        y2 = y0 + h * z0
        z1 = z0 + h * w0
        w1 = w0 + h * r0
        y1 = y2
        r = f.subs({x: xf, y: y2, z: z1, w: w1})
        # solving for n iterations
        if (m == 'n'):
            for i in range(n):
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (w0 + w1) / 2.0
                w1 = w0 + h * (r0 + r) / 2.0
                r = f.subs({x: xf, y: y2, z: z1, w: w1})
                ea = fabs((y2 - y1) / y2) * 100
                List_num_iterations.append(i+1)
                List_y_values.append(y2)
                List_y_dash_values.append(z1)
                List_y_d_dash_values.append(w1)
                List_relative_y_errors.append(ea)
                #print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
        else:
            # solving until stopping error e%
            ea = 9000
            i = 1
            while ea > e:
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (w0 + w1) / 2.0
                w1 = w0 + h * (r0 + r) / 2.0
                r = f.subs({x: xf, y: y2, z: z1, w: w1})
                ea = fabs((y2 - y1) / y2) * 100
                #print("At i={} --> y={} ,  Ea%(y)={}%".format(i, y2, ea))  # printing y,Ea at every i
                List_num_iterations.append(i)
                List_y_values.append(y2)
                List_y_dash_values.append(z1)
                List_y_d_dash_values.append(w1)
                List_relative_y_errors.append(ea)
                y1 = y2
                i += 1
        #print("y({})={} , y'({})={} , y\"({})={}".format(xf, y2, xf, z1, xf, w1))
        y_value=y2
        y_dash=z1
        y_d_dash=w1
        yp=0
        if not exact_y=='':
         t = simplify(exact_y)
         yp = t.subs({x: xf})
         et = fabs((yp - y2) / yp) * 100
        #print("y({})={} ,Et%={}%".format(xf, yp, et))
         true_error =et
        return xf, List_num_iterations,List_y_values,List_relative_y_errors,List_y_dash_values,List_y_d_dash_values,y_value,y_dash,y_d_dash,true_error,yp
    ##############################for Heun 2 ODE###########################################
def Heun2(eq,exact_y,x0,y0,z0,xf,h,m,n,e):
        # ********
        List_num_iterations = []
        List_y_values = []
        List_relative_y_errors = []
        List_y_dash_values = []
        y_value = 0
        y_dash = 0
        true_error = 0
        # *********
        f = simplify(eq)
        r0 = f.subs({x: x0, y: y0, z: z0})
        y2 = y0 + h * z0
        z1 = z0 + h * r0
        y1 = y2
        r = f.subs({x: xf, y: y2, z: z1})
        # solving for n iterations
        if (m == 'n'):
            for i in range(n):
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (r0 + r) / 2.0
                r = f.subs({x: xf, y: y2, z: z1})
                ea = fabs((y2 - y1) / y2) * 100
                #print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
                List_num_iterations.append(i+1)
                List_y_values.append(y2)
                List_y_dash_values.append(z1)
                List_relative_y_errors.append(ea)
        else:
            # solving until stopping error e%
            ea = 9000
            i = 1
            while ea > e:
                y2 = y0 + h * (z0 + z1) / 2.0
                z1 = z0 + h * (r0 + r) / 2.0
                r = f.subs({x: xf, y: y2, z: z1})
                ea = fabs((y2 - y1) / y2) * 100
                #print("At i={} --> y={} ,  Ea%={}%".format(i, y2, ea))
                List_num_iterations.append(i)
                List_y_values.append(y2)
                List_y_dash_values.append(z1)
                List_relative_y_errors.append(ea)

                y1 = y2
                i += 1
        #print("y({})={} , y'({})={}".format(xf, y2, xf, z1))
        y_value =y2
        y_dash = z1
        yp=0
        if not exact_y == '':
         t = simplify(exact_y)
         yp = t.subs({x: xf})
         et = fabs((yp - y2) / yp) * 100
        #print("y({})={} ,Et%={}%".format(xf, yp, et))
         true_error =et
        return xf, List_num_iterations,List_y_values,List_relative_y_errors,List_y_dash_values,y_value,y_dash,true_error,yp
    #******************************for Heun 1 ODE---> 1eq************************************
def Heun1(eq1,exact_y, x0, y0, xf, h, m, n, e):
        # ********
        List_num_iterations = []
        List_y_values = []
        List_relative_y_errors = []
        y_value = 0
        true_error = 0
        # *********
        f = simplify(eq1)
        y2 = y0
        y1 = 0
        r0 = f.subs({x: x0, y: y0})
        r = r0
        if (m == 'n'):
            # 2.1.1.1-> asking for number of iterations
            for i in range(n):
                y2 = y0 + h * r
                r = (r0 + f.subs({x: xf, y: y2})) / 2.0
                ea = fabs((y2 - y1) / y2) * 100
                # 2.1.1.2--> every iteration-> output y & Ea at i
                #print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea))
                List_num_iterations.append(i+1)
                List_y_values.append(y2)
                List_relative_y_errors.append(ea)
                y1 = y2
        else:
            # 2.1.2.1--> enter stoping error
            # e = float(input("         Enter e : "))
            ea = 9000
            i = 1
            while ea > e:
                y2 = y0 + h * r
                r = (r0 + f.subs({x: xf, y: y2})) / 2.0
                ea = fabs((y2 - y1) / y2) * 100
                # 2.1.2.2--> every iteration-> output y & Ea at i
                #print("At i={} --> y={} ,  Ea%={}%".format(i, y2, ea))
                List_num_iterations.append(i)
                List_y_values.append(y2)
                List_relative_y_errors.append(ea)
                y1 = y2
                i += 1
            # 2.2--> output final answer of y
        #print("y({})={}".format(xf, y2))
        y_value=y2
        et=0
        yp=0
        if not exact_y == '':
         t = simplify(exact_y)
         yp = t.subs({x: xf})
         et = fabs((yp - y2) / yp) * 100
        #print("y({})={} ,Et%={}%".format(xf, yp, et))
         true_error=et
        return xf, List_num_iterations,List_y_values,List_relative_y_errors,y_value,true_error,yp
#********************************for Huen 1 ODE ---> 2eq***********************************************
def Heun1_2(eq1, eq2, x0, y0, z0, xf, h, m, n, e):
        # ********
        List_num_iterations = []
        List_y_values = []
        List_relative_y_errors = []
        List_relative_z_errors = []
        List_z_values = []
        y_value = 0
        z_value = 0
        true_error = 0
        # *********
        f1 = simplify(eq1)
        f2 = simplify(eq2)
        y2 = y0
        y1 = 0
        z2 = y0
        z1 = 0
        r01 = f1.subs({x:x0,y: y0, z: z0})
        r02 = f2.subs({x:x0,y: y0, z: z0})
        r1 = r01
        r2 = r02
        if (m == 'n'):
            for i in range(n):
                y2 = y0 + h * r1
                z2 = z0 + h * r2
                r1 = (r01 + f1.subs({x:xf,y: y2, z: z2})) / 2.0
                r2 = (r02 + f2.subs({x:xf,y: y2, z: z2})) / 2.0
                ea1 = fabs((y2 - y1) / y2) * 100
                ea2 = fabs((z2 - z1) / z2) * 100
                #print("At i={} --> y={} ,  Ea%={}%".format(i + 1, y2, ea1))
                #print("At i={} --> z={} ,  Ea%={}%".format(i + 1, z2, ea2))
                List_num_iterations.append(i+1)
                List_y_values.append(y2)
                List_relative_y_errors.append(ea1)
                List_relative_z_errors.append(ea2)
                List_z_values.append(z2)
                y1 = y2
                z1 = z2
        else:
            ea1 = 9000
            ea2 = 9000
            i = 1
            while ea1 > e and ea2 > e:
                y2 = y0 + h * r1
                z2 = z0 + h * r2
                r1 = (r01 + f1.subs({x:xf,y: y2, z: z2})) / 2.0
                r2 = (r02 + f2.subs({x:xf,y: y2, z: z2})) / 2.0
                ea1 = fabs((y2 - y1) / y2) * 100
                ea2 = fabs((z2 - z1) / z2) * 100
                #print("At i={} --> y={} ,  Ea%={}%".format(i, y2, ea1))
                #print("At i={} --> z={} ,  Ea%={}%".format(i, z2, ea2))
                List_num_iterations.append(i)
                List_y_values.append(y2)
                List_relative_y_errors.append(ea1)
                List_relative_z_errors.append(ea2)
                List_z_values.append(z2)
                y1 = y2
                z1 = z2
                i += 1
        #print("y={}".format(y2))
        y_value=y2
        z_value=z2
        #print("z={}".format(z2))
        return xf,List_num_iterations,List_y_values,List_z_values,List_relative_y_errors,List_relative_z_errors ,y_value,z_value
#*********************************************Main func of heun *****************************************
def Solve_Heun(ode_choice, num_eqs,ode1_eq1,ode1_eq2,ode2_eq,ode3_eq,exact_y,xnod,ynod,znod,y_dash_nod,y_doup_dash_nod,X_at,num_iter_Or_stoppingC,num_iterations,stoppingC):
    # ********
    xf=0
    List_num_iterations = []
    List_y_values = []
    List_z_values=[]
    List_relative_y_errors = []
    List_relative_z_errors=[]
    List_y_dash_values = []
    List_y_d_dash_values = []
    y_value = 0
    z_value = 0
    y_dash = 0
    y_d_dash = 0
    true_error = 0
    y_exact_value=0
    # *********
 #2--> asking for the degree of the ODE
    l=int(ode_choice)
    if(l==1):
    #2.1--> asking for number of equations
        q = int(num_eqs)
        if(q==1):
    #2.1.1--> asking for the equation, x0,y0,x1, stopping condition-->  5 inputs & 1 output
            f = ode1_eq1
            x0 = float(xnod)
            y0 = float(ynod)
            x1 = float(X_at)
            m = num_iter_Or_stoppingC
            n = 0
            e = 0
            h = x1 - x0
            y2 = 0
            if(m == 'n'):
    # 2.1.1.1-> asking for number of iterations
                n = int(num_iterations)
    #2.1.1.2--> every iteration-> output y & Ea at i
            else:
    #2.1.2.1--> enter stoping error
                e = float(stoppingC)

            (xf, List_num_iterations,List_y_values,List_relative_y_errors,y_value,true_error,y_exact_value) = Heun1(f,exact_y, x0, y0, x1, h, m, n, e)
        else:
            f1 = ode1_eq1
            f2 = ode1_eq2
            x0 = float(xnod)
            y0 = float(ynod)
            z0 = float(znod)
            x1 = float(X_at)
            m = num_iter_Or_stoppingC
            n = 0
            e = 0
            #************************************************
            h = x1 - x0
            if (m == 'n'):
                n = int(num_iterations)
            else:
                e = float(stoppingC)
            ( xf,List_num_iterations,List_y_values,List_z_values,List_relative_y_errors,
              List_relative_z_errors ,y_value,z_value) = Heun1_2(f1,f2,x0,y0,z0,x1,h,m,n,e)

    elif l == 2:
    #All the coming is the same as l=1 & q=1 but every time addinal input is required y'->l=2 , y" -> l=3 ,y"'->l=4
        f = ode2_eq
        x0 = float(xnod)
        y0 = float(ynod)
        z0 = float(y_dash_nod)
        x1 = float(X_at)
        m = num_iter_Or_stoppingC
        n=0
        e=0
        h = x1 - x0
        # solving for n iterations
        if (m == 'n'):
            n = int(num_iterations)
        else:
            # solving until stopping error e%
            e = float(stoppingC)

        (xf, List_num_iterations,List_y_values,List_relative_y_errors,List_y_dash_values,y_value,y_dash,true_error,y_exact_value)=Heun2(f,exact_y,x0,y0,z0,x1,h,m,n,e)

    elif l == 3:
        f = ode3_eq
        x0 = float(xnod)
        y0 = float(ynod)
        z0 = float(y_dash_nod)
        w0 = float(y_doup_dash_nod)
        x1 = float(X_at)
        m = num_iter_Or_stoppingC
        n = 0
        e = 0

        h = x1 - x0
        # solving for n iterations
        if (m == 'n'):
            n = int(num_iterations)
        else:
            # solving until stopping error e%
            e = float(stoppingC)

        (xf, List_num_iterations,
        List_y_values,
        List_relative_y_errors,
        List_y_dash_values,
        List_y_d_dash_values,
        y_value,
        y_dash,
        y_d_dash,
        true_error,y_exact_value) = Heun3(f,exact_y, x0, y0, z0, w0, x1, h, m, n, e)

    return (xf,
    List_num_iterations,
    List_y_values,
    List_z_values,
    List_relative_y_errors,
    List_relative_z_errors,
    List_y_dash_values,
    List_y_d_dash_values,
    y_value,
    z_value,
    y_dash,
    y_d_dash,
    true_error,y_exact_value)
#***************************************************************************************
#********************** for testing heun //passed*************************
# ode_choice=2
# num_eqs=1
# ode1_eq1=''
# ode1_eq2=''
# ode2_eq='(Pow(x,3)*ln(x)-2*y+2*x*z)/Pow(x,2)'
# ode3_eq=''
# exact_y='7*x/4+0.5*Pow(x,3)*ln(x)-0.75*Pow(x,3)'
# xnod=1
# ynod=1
# znod=0
# y_dash_nod=0
# y_doup_dash_nod=0
# X_at=1.2
# num_iter_Or_stoppingC='n'
# num_iterations=2
# stoppingC=0
# #*********************************
# (xf,
# List_num_iterations,
# List_y_values,
# List_z_values,
# List_relative_y_errors,
# List_relative_z_errors,
# List_y_dash_values,
# List_y_d_dash_values,
# y_value,
# z_value,
# y_dash,
# y_d_dash,
# true_error)=Solve_Heun(ode_choice,num_eqs,ode1_eq1,ode1_eq2,ode2_eq,ode3_eq,exact_y,xnod,ynod,znod,y_dash_nod,y_doup_dash_nod,X_at,num_iter_Or_stoppingC,num_iterations,stoppingC)
# #**************************************
# print(xf)
# print(List_num_iterations)
# print(List_y_values)
# print(List_z_values)
# print(List_relative_y_errors)
# print(List_relative_z_errors)
# print(List_y_dash_values)
# print(List_y_d_dash_values)
# print(y_value)
# print(z_value)
# print(y_dash)
# print(y_d_dash)
# print(true_error)
#********************** for testing Euler //passed*************************
# num_eqs=1
# eq1='1/(Pow(x,2)+y)'
# eq2=''
# eq3=''
# xnod=4.0
# ynod=4.0
# znod=''
# tnod=''
# X_at=4.4
# h_Or_n='h'
# h=0.1
# n=''
# (y_out,
#  x_out,
#  z_out,
#  t_out,
#  t_error,
#  y_error,
#  z_error,
#  List_x_values,
#  List_y_values,
#  List_z_values,
#  List_approx_y_error,
#  List_approx_z_error,
#  List_approx_t_error)=Solve_Euler(num_eqs,eq1,eq2,eq3,xnod,ynod,znod,tnod,X_at,h_Or_n,h,n)
# print(y_out)
# print(x_out)
# print(z_out)
# print(t_out)
# print(t_error)
# print(y_error)
# print(z_error)
# print(List_x_values)
# print(List_y_values)
# print(List_z_values)
# print(List_approx_y_error)
# print(List_approx_z_error)
# print(List_approx_t_error)
#
