import sympy as sp
import numpy as np

vars=sp.symbols('x:z , a:w') #list (tuple) of variables
truevars=()
def TrapezoidalIntegration(g,a,b,n,i):     #g is function,a is lower bound, b is upper bound,n is number of segment
    h=(b-a)/n                       #i is the current evaluating integral operator counting from the right to left
    answer=0.0
    for iterator in np.arange(a,b,h):
        if iterator==a :
            answer+=g.subs(vars[i],iterator)
        else:
            answer+=2*g.subs(vars[i],iterator)
    answer+=g.subs(vars[i],b)
    answer*=h/2
    return answer

def Multi_Trapezoidal(nIntegralOp,Fn,lowerb,upperb,numSubInt):
    Functions=[] #list of functions
    Functions.append(sp.sympify(Fn))

    #ordinal functios is taken from stack overflow, https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    #ordinal() converts 1 to 1st ,2 to 2nd and so on
    #Evaluation block
    for i in range(nIntegralOp):
        Functions.append(sp.sympify(TrapezoidalIntegration(Functions[i],lowerb[i],upperb[i],numSubInt[i],i)))
        print(str(ordinal(i+1))+" application of trapezoidal rule: "+str(Functions[i+1]))
    return Functions[nIntegralOp]

def TrapezoidRule(Fn):

    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

    #The number of integral operators
    numI=int(input("Enter the number of integral operators: "))

    #data members
    lowerbounds=[] #list of lower bounds
    upperbounds=[] #list of upper bounds
    numSubIntervals=[] # list of num_of_intervals, one for each variable

    ### Block for taking the integration-limits info from the user
    for i in range(numI):
        l=input("please enter the "+ str(ordinal(i+1))+ " lower bound: ")
        lowerbounds.append(float(l))
        u=input("please enter the "+ str(ordinal(i+1))+ " upper bound: ")
        upperbounds.append(float(u))
        n=input("please enter the "+ str(ordinal(i+1))+ " number of subintervals: ")
        numSubIntervals.append(int(n))
    Multi_Trapezoidal(numI,Fn,lowerbounds,upperbounds,numSubIntervals)



def RombergInt(nIntOp,Func,O_error,lowerb,upperb):
    Fn=sp.sympify(Func)
    #initalize a matrix to have the extrapolation values
    Romberg=np.zeros((O_error//2,O_error//2))

    #get trapezoidal at each h in first column
    numSubInt=[]
    for j in range (O_error//2):
        numSubInt.append([])
        for i in range(nIntOp):
            numSubInt[j].append(2**j)

    numSubInt.append(numSubInt)
    for j in range (O_error//2):
        Romberg[j,0]=Multi_Trapezoidal(nIntOp,Fn,lowerb,upperb,numSubInt[j])

    for k in range(1,O_error//2):
        for j in range(k,O_error//2):
            Romberg[j,k]=(4**(k)*Romberg[j,k-1]-Romberg[j-1,k-1])/(4**(k)-1)

    print(Romberg)
    return Romberg[O_error//2-1,O_error//2-1]

def RombergRule(Fn,numI,ax,bx,ay,by,az,bz,Order_of_Error):
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    #The number of integral operators
    #numI=int(input("Enter the number of integral operators: "))

    #data members
    lowerbounds=[] #list of lower bounds
    upperbounds=[] #list of upper bounds
    #numSubIntervals=[] # list of num_of_intervals, one for each variable
    if(numI==1):
        lowerbounds=[ax]
        upperbounds=[bx]
    elif(numI==2):
        Fn += "+0*x"
        lowerbounds=[ax,ay]
        upperbounds=[bx,by]
    elif(numI==3):
        Fn += "+0*x+0*y+0*z"
        lowerbounds=[ax,ay,az]
        upperbounds=[bx,by,bz]

    ### Block for taking the integration-limits info from the user
    #for i in range(numI):
    #    l=input("Enter the "+ str(ordinal(i+1))+ " lower bound: ")
    #    lowerbounds.append(float(l))
    #    u=input("Enter the "+ str(ordinal(i+1))+ " upper bound: ")
    #    upperbounds.append(float(u))
    #Order_of_Error=int(input("Enter the order of error (an even number): "))
    return RombergInt(numI,Fn,Order_of_Error,lowerbounds,upperbounds)
