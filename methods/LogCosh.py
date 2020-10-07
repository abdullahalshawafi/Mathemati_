import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Least Squares take on the matter
def LeastSquares(xdata,ydata,RP=4):
    X=np.c_[np.ones((len(xdata),1)),xdata]
    #Contriving the normal equation
    Theta=np.linalg.multi_dot([np.linalg.pinv(X),ydata])
    return np.round(Theta,RP)


def minLogCoshLoss(x,y,iterations=1000,lamda=0.01,tolerance=0,RP=4):
    xd=np.c_[np.ones((len(x),1)),x] #concatenate a coloumn vector of ones into your x
    theta=np.random.randn(2,1)
    for t in range(0,iterations):
        Grad=[]
        G=0
        for i in range(0,len(y)):
            Grad.append(-np.tanh(y[i]-np.dot(xd[i],theta))*xd[i].T)
            G=Grad[i]+G
        G=G.reshape(len(theta),1)   
        theta=theta-lamda*G
        if(abs(G[0][0]/(theta[0][0]-lamda*G[0][0]))<tolerance and abs(G[1][0]/(theta[1][0]-lamda*G[1][0]))<tolerance):
            theta=theta-lamda*G
            break
    return np.round(theta,RP),G

def RegressionErrors(theta,Theta,xdata,ydata): 
    #Regression Errors
    CoshErrors=[]
    SquareErrors=[]
    for i in range(0,len(xdata)):
        CoshErrors.append(np.log(np.cosh(ydata[i][0]-(theta[1][0]*xdata[i][0]+theta[0][0]))))
        SquareErrors.append((ydata[i][0]-(Theta[1][0]*xdata[i][0]+Theta[0][0]))**2)

    CshErrors=np.sum(CoshErrors)
    SqrErrors=np.sum(SquareErrors)
    
    return CshErrors,SqrErrors

#Testing

""" #Generating a random data that's suitable for a linear fit
x=2*np.random.rand(50,1) #This function returns Random values in a given shape. It Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
y=4+3*x+np.random.randn(50,1) #randn implies random data that follows the standard Gaussian Distribution (adding Gaussian Noise to y=4+3x)

theta,G=LogCoshLoss(x,y,10000,0.01,0.00001/100)
E1,E2=RegressionErrors(theta,theta,x,y)

print(E1,'\n',G)
print('y =',theta[1][0],"*x + ",theta[0][0])
plt.plot(x, y, "b.") #blue small dots=b.
X = np.linspace(0,2,100)
Yg=theta[1]*X+theta[0] #Gradient Descent Version
plt.plot(X, Yg, 'r-', label='Best Fit') #red soline line=r-, comment this to see the random data set only.
plt.show() """
