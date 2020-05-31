import numpy as np
from scipy import integrate
from sympy import cos, sin, tan,acos, asin, atan, cosh, sinh, tanh, acosh, asinh, atanh, cot, acot, coth, acoth,\
    sec, asec, sech, asech, csc, acsc, csch, acsch, sqrt, pi
#from numpy import sin
#from numpy import cos
#from numpy import tan
#from numpy import sinh
#from numpy import cosh
#from numpy import tanh
from numpy import exp
from numpy import log                   #ln
from numpy import log10
from numpy import log2
#from numpy import arcsin
#from numpy import arctan
#from numpy import arccos
#from numpy import arcsinh
#from numpy import arccosh
#from numpy import arctanh
#from numpy import pi
#def sec(x):
#    return 1/cos(X)
#def csc(x):
#    return 1/sin(x)
#def cot(x):
#    return 1/tan(x)
#def sech(x):
#   return 1/cosh(X)
#def csch(x):
#    return 1/sinh(X)
#def coth(x):
#    return 1/tanh(x)
#the outputs are at the end in the output section

#intial values section don't touch
#---------------------
numberOfVariables=1
#---------------------
#end of intial values section

#the input section
#------------------------------------------------------------------------------------------------------------------------
#number of variables are automatically known
#one varible(f(x) from x=ax to x=bx) and two varile(f(x,y) from x=ax to x=bx and from y=ay to y=by) with n point of gauss quadrature
#to input infinity the input must be (ax=np.inf) for positive infinity and (ax=-np.inf) for negative infinity and for pi (np.pi)
#max n is 6
#important (note that even in one varibles integration leave (ay) and (by) with intial valuses)
# input one or two varible function must be string and every function has (np.) before the function except for Power function use (x**2) insted of (np.pow(x,2)) as (pow(x,2)) is not exist in numpy library and normal varibles are written as normal without (np.)examples{x*np.sin(x)-x*x, 1/x**2, np.cosh(x)*y*np.sin(y)}d
def Exact(f,ax,bx,ay,by,az,bz,numberOfVariables):
    f.replace("exp", "np.exp")
    f.replace("log", "np.log")
    if(numberOfVariables==1):
        fe = lambda x: eval(f)
        exact=integrate.quad(fe, ax, bx)
        exact=exact[0]
        return exact
    if(numberOfVariables==2):
        fe = lambda y, x: eval(f)
        exact=integrate.dblquad(fe, ax, bx, lambda x: ay, lambda x: by)
        exact=exact[0]
        return exact
    if(numberOfVariables==3):
        fe = lambda z, y, x: eval(f)
        exact=integrate.tplquad(fe, ax, bx, lambda x: ay, lambda x: by, lambda x,y:az, lambda x,y:bz)
        exact=exact[0]
        return exact

def myfun(F,x1,x2,y1,y2,N):
    f=F
    f.replace("exp", "np.exp")
    f.replace("log", "np.log")
    ax=x1
    bx=x2
    numberOfVariables=1
    if(f.find("y") != -1):
        numberOfVariables=2
    ay=1
    by=2
    if(numberOfVariables==2):
        ay=y1
        by=y2
    n=N
    #------------------------------------------------------------------------------------------------------------------------
    #end of the input section

    #the implementation section (don't touch)
    #---------------------------------------------------------------------------------------------------------------------------------------------
    f=f.replace("^","**")
    f=f.replace("PI","pi")
    if(ax==-np.inf):
        ax=-bx
        bx=np.inf
        f=f.replace("x","(-x)")
    if(ay==-np.inf):
        ay=-by
        by=np.inf
        f=f.replace("y","(-y)")
    if(numberOfVariables==1):
        def f1(x):
            return eval(f)
    else:
        def f2(x,y):
            return eval(f)

    x=[[[],[]],[[],[],[]],[[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[],[]]]
    c=[[[],[]],[[],[],[]],[[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[],[]]]
    #ci -> c[n-2][i+1]
    c[0][0]=1
    c[0][1]=1
    c[1][0]=0.8888888888888888
    c[1][1]=0.5555555555555556
    c[1][2]=0.5555555555555556
    c[2][0]=0.6521451548625461
    c[2][1]=0.6521451548625461
    c[2][2]=0.3478548451374538
    c[2][3]=0.3478548451374538
    c[3][0]=0.5688888888888889
    c[3][1]=0.4786286704993665
    c[3][2]=0.4786286704993665
    c[3][3]=0.2369268850561891
    c[3][4]=0.2369268850561891
    c[4][0]=0.3607615730481386
    c[4][1]=0.3607615730481386
    c[4][2]=0.4679139345726910
    c[4][3]=0.4679139345726910
    c[4][4]=0.1713244923791704
    c[4][5]=0.1713244923791704

    #xi -> x[n-2][i+1]
    x[0][0]=-0.5773502691896257
    x[0][1]=0.5773502691896257
    x[1][0]=0
    x[1][1]=-0.7745966692414834
    x[1][2]=0.7745966692414834
    x[2][0]=-0.3399810435848563
    x[2][1]=0.3399810435848563
    x[2][2]=-0.8611363115940526
    x[2][3]=0.8611363115940526
    x[3][0]=0
    x[3][1]=-0.5384693101056831
    x[3][2]=0.5384693101056831
    x[3][3]=-0.9061798459386640
    x[3][4]=0.9061798459386640
    x[4][0]=0.6612093864662645
    x[4][1]=-0.6612093864662645
    x[4][2]=-0.2386191860831969
    x[4][3]=0.2386191860831969
    x[4][4]=-0.9324695142031521
    x[4][5]=0.9324695142031521
    def integration(ax,bx,ay,by):
        if(not(ax==np.inf or ax==-np.inf or bx==np.inf or bx==-np.inf or (ay==np.inf or ay==-np.inf or by==np.inf or by==-np.inf) and numberOfVariables==2)):

            #if there is no infinity for 1 variable
            if(numberOfVariables==1):
                I=0
                T1X=(bx-ax)/2
                T2X=(bx+ax)/2
                for i in range(n):
                    I+=c[n-2][i]*f1(T1X*x[n-2][i]+T2X)
                I*=T1X
                return I
            #

            #if there is no infinity for 2 variable
            else:
                I=0
                T1X=(bx-ax)/2
                T2X=(bx+ax)/2
                T1Y=(by-ay)/2
                T2Y=(by+ay)/2
                for k in range(n):
                    for i in range(n):
                        I+=c[n-2][k]*c[n-2][i]*f2(T1X*x[n-2][i]+T2X,T1Y*x[n-2][k]+T2Y)
                I*=T1X*T1Y
                return I
            #(ay==0 and(ax==np.inf or bx==np.inf))or(by==0 and(ax==np.inf or bx==np.inf))
        else:
            if(numberOfVariables==1):
            #if any infinity appears for 1 variable
                I=0
                T1X=(1/bx-1/ax)/2
                T2X=(1/bx+1/ax)/2
                for i in range(n):
                    I+=c[n-2][i]*f1(1/(T1X*x[n-2][i]+T2X))*-T1X/((T1X*x[n-2][i]+T2X)*(T1X*x[n-2][i]+T2X))
                return I
            #

            #if any infinity appears for 2 variable
            else:
                if((ax==0 and(ay==np.inf or by==np.inf))or(bx==0 and(ay==np.inf or by==np.inf))):
                    I=0
                    T1X=(bx-ax)/2
                    T2X=(bx+ax)/2
                    T1Y=(1/by-1/ay)/2
                    T2Y=(1/by+1/ay)/2
                    for k in range(n):
                        for i in range(n):
                            I+=c[n-2][k]*c[n-2][i]*f2(T1X*x[n-2][i]+T2X,1/(T1Y*x[n-2][k]+T2Y))*-T1Y/((T1Y*x[n-2][k]+T2Y)*(T1Y*x[n-2][k]+T2Y))
                    I*=T1X
                    return I
                elif((ay==0 and(ax==np.inf or bx==np.inf))or(by==0 and(ax==np.inf or bx==np.inf))):
                    I=0
                    T1X=(1/bx-1/ax)/2
                    T2X=(1/bx+1/ax)/2
                    T1Y=(by-ay)/2
                    T2Y=(by+ay)/2
                    for k in range(n):
                        for i in range(n):
                            I+=c[n-2][k]*c[n-2][i]*f2(1/(T1X*x[n-2][k]+T2X),T1Y*x[n-2][i]+T2Y)*-T1X/((T1X*x[n-2][k]+T2X)*(T1X*x[n-2][k]+T2X))
                    I*=T1Y
                    return I
                else:
                    I=0
                    T1X=(1/bx-1/ax)/2
                    T2X=(1/bx+1/ax)/2
                    T1Y=(1/by-1/ay)/2
                    T2Y=(1/by+1/ay)/2
                    for k in range(n):
                        for i in range(n):
                            I+=c[n-2][k]*c[n-2][i]*f2(1/(T1X*x[n-2][i]+T2X),1/(T1Y*x[n-2][k]+T2Y))*T1X/((T1X*x[n-2][i]+T2X)*(T1X*x[n-2][i]+T2X))*T1Y/((T1Y*x[n-2][k]+T2Y)*(T1Y*x[n-2][k]+T2Y))
                    return I
            #
    if(numberOfVariables==1):
        fe = lambda x: eval(f)
        exact=integrate.quad(fe, ax, bx)
        exact=exact[0]
    if(numberOfVariables==2):
        fe = lambda y, x: eval(f)
        exact=integrate.dblquad(fe, ax, bx, lambda x: ay, lambda x: by)
        exact=exact[0]
    Result=integration(ax,1,ay,1)
    Result+=integration(1,bx,ay,1)
    Result+=integration(ax,1,1,by)
    Result+=integration(1,bx,1,by)
    if(numberOfVariables==1):
        Result/=2
    RelativeTrueError=(np.abs(exact-Result)/abs(exact))*100
    #-----------------------------------------------------------------------------------------------------------------------------------
    #end of the implementation section
    return Result,RelativeTrueError
    #output section
    #print("Approximated Value =",Result)#Gauss quadrature approximation value
    #print("Exact Value =",exact)#Exact value
    #print("Relative Percentage True Error =",100*RelativeTrueError)#Relative Percentage True Error
    #end of the output section
