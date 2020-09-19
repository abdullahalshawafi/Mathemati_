import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def LeastAbsoluteDeviations(xdata,ydata,tolerance=0.1,iterations=400,RP=4): #RP is the rounding point and the tolerance is the stopping criteria (Relative true error)

   #Constructing the design matrix
   X=np.c_[np.ones((len(xdata),1)),xdata]
   theta=np.random.randn(2,1) #Initializing random theta, recall that numpy's arrays are multidimensional

     #Choreographing the iterative scheme
   for  t in range(iterations):
        #Forging the weight matrix
        W=[]
        for i in range(len(xdata)):
            W.append(1/abs(ydata[i]-np.dot(theta.T,X[i])))
        W=np.array(W)
        W= W * np.identity(len(W))
        #Calculating Theta's RHS
        A=np.linalg.inv(np.linalg.multi_dot([X.T,W,X]))
        B=np.linalg.multi_dot([X.T,W,y])
        #Tolerance Check
        if(abs(theta[0][0]-np.dot(A,B)[0][0])/abs(theta[0][0])<tolerance/100 and abs(theta[1][0]-np.dot(A,B)[1][0])/abs(theta[1][0])<tolerance/100): #In love with this
            break
        #RHS Calculation Done
        theta=np.dot(A ,B)
   return np.round(theta,RP);


#Least Squares take on the matter
def LeastSquares(xdata,ydata,RP=4):
    X=np.c_[np.ones((len(xdata),1)),xdata]
    #Contriving the normal equation
    Theta=np.linalg.multi_dot([np.linalg.pinv(X),ydata])
    return np.round(Theta,RP)
    
#Graphing both plots
def GraphTheory(xdata,ydata,theta,Theta): #theta is for absolutes and Theta is for squares
    X = np.linspace(min(xdata),max(xdata),100)
    #Least Absolute Deviations:
    Y=theta[1][0]*X+theta[0][0]
    #Least Squares:
    Ys=Theta[1][0]*X+Theta[0][0]
    plt.plot(X, Ys, 'r-', label='Least Squares')
    plt.plot(X, Y, 'g-', label='Least Absolutes')
    plt.plot(x, y, "b.") #blue small dots=b.
    plt.xlabel("$x_1$", fontsize=18) #$LATEX$
    plt.ylabel("$y$", rotation=0, fontsize=18)  #rotation=0 for a vertical y
    plt.show()


#Angle between both Straight Lines:
def Angulus(theta, Theta):
    AngleDifference = np.arctan(abs((Theta[1][0]-theta[1][0])/(1+Theta[1][0]*theta[1][0]))) #The angle difference between the two lines
    return AngleDifference*180/np.pi  #In degrees

def CorrelationCoefficients(theta,Theta,xdata,ydata): 
    #Regression Errors
    AbsoluteErrors=[]
    SquareErrors=[]
    for i in range(0,len(xdata)):
        AbsoluteErrors.append(abs(ydata[i][0]-(theta[1][0]*xdata[i][0]+theta[0][0])))
        SquareErrors.append((ydata[i][0]-(Theta[1][0]*xdata[i][0]+Theta[0][0]))**2)

    AbsErrors=np.sum(AbsoluteErrors)
    SqrErrors=np.sum(SquareErrors)
    #print(AbsoluteErrors,SquareErrors)
        
    #True Errors (Regression Errors with respect to a horizontal line)
    AbsoluteTrues=[]
    SquareTrues=[]
    Yavg=np.average(ydata)
    for i in range(0,len(xdata)):
        AbsoluteTrues.append(abs(ydata[i][0]-Yavg))
        SquareTrues.append((ydata[i][0]-Yavg)**2)
    AbsTrues=np.sum(AbsoluteTrues)
    SqrTrues=np.sum(SquareTrues)
    #print(AbsoluteTrues,SquareTrues)
    #The correlation coefficient
    Qabs=abs((AbsTrues-AbsErrors)/AbsTrues)
    Qsq=abs((SqrTrues-SqrErrors)/SqrTrues)
    return np.sqrt(Qabs)*100,np.sqrt(Qsq)*100 #Absolute and squared correlation coefficients

#Generating a random data that's suitable for a linear fit

#x=4*np.random.rand(15,1) #This function returns Random values in a given shape. It Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
#y=5+-3*x+np.random.randn(15,1) #randn implies random data that follows the standard Gaussian Distribution (adding Gaussian Noise to y=4+3x)
def Numpify(xdata,ydata):
    x=np.array(xdata)
    x=x.reshape(len(x),1)
    y=np.array(ydata)
    y=y.reshape(len(y),1)
    return x,y
x=[1,2,3,4,5,6,7,8,9]
y=[11,3,6,8,6,5,3,8,5]
x,y=Numpify(x,y)
th=LeastAbsoluteDeviations(x,y,0.1,400)
print("y = ",th[1][0],"*x","+",th[0][0])
Th=LeastSquares(x,y)
print("y = ",Th[1][0],"*x","+",Th[0][0])
print(CorrelationCoefficients(th,Th,x,y))
GraphTheory(x,y,th,Th)

