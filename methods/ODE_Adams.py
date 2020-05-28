######## Definition of function solving ODE using Predictor Corrector using
######## Adam's method with backward difference#######
######## This problem solves the equations till the fourth order
from math import e #### Added this to be able to solve functions containing e ############
from math import sin , cos ,tan , sinh , cosh , tanh , asin , acos , atan , asinh , acosh , atanh
"""
equation1 = input("Enter the RHS of the equation here: ")
x = 2.3
y = 1.2
while 1:
    try:
        eval(equation1)
        break
    except:
        equation1 = input( "Invalid Equation!!! Please enter the RHS of the equation here(using these operators + - * / **): ")



N1 = int(input("N numbers"))
X1=[]
Y1=[]
i=0
while i < N1:
    x = float(input("X"))
    X1.append(x)
    y = float(input("Y"))
    Y1.append(y)
    i=i+1
    pass

xrequired1 = float(input("X at which y is to be calculated: "))
no_of_iter1 = int(input("Please enter the number of iterations to stop at (at least 2) :"))
no_of_digi1=int(input("Please enter the number of digits to compare at:"))
"""
def ode_adams_backward_difference(equation,no_of_digi,no_of_iter,N,X,Y,xrequired):

########### Checking that the equation is a valid one ############
###Assign arbitary values for x & y to test the validity of the equation####


############# Check which is the terminating condition #####################
    ######Default values for number of digits and itertions




#############

    n = N
    i = 0
    FUN = []

###################################
    def f(x, y, i):
        ev = eval(equation)
        FUN.append(float(ev))
        
    
###################################
    Pre_coeff = [1,0.5,5 / 12,3 / 8,251 / 720]
    Corr_coeff = [1,-0.5,-1 / 12,-1 / 24,-19 / 720]

    def predictor():
        h_r = 0
        for c in range(0,n):
            h_r+=tempArr[c][len(tempArr[c]) - 1] * Pre_coeff[c]
        result = Y[n - 1] + h * h_r
        return result
    def corrector():
        h_r = 0
        for c in range(0, n):
            h_r += tempArr[c][len(tempArr[c]) - 1] * Corr_coeff[c]
        result = Y[n - 1] + h * h_r
        return result

###################################


    while i < N:

        f(X[i], Y[i], i)
        i = i + 1
        pass
    if(n>5):
        for c in range(0, n-5):
            FUN.pop(0)
            X.pop(0)
            Y.pop(0)
        n=5
        N=5
####################################
    i = 0
    h = abs(X[0] - X[1])
    tempArr = []
    results=[]

######BEFORE Correction#######
    def Table(No):
        i = 0
        tempArr.append(FUN)
        for j in range(0,n):
            arr0 = []
            if(No == 1):
                break

            while i < No - 1:
                if i + 1 < No:
                    arr0.append(float(tempArr[j][i + 1] - tempArr[j][i]))
                    pass
                i = i + 1
                pass
            tempArr.append(arr0.copy())
            i = 0
            No-=1

#####first call to calculate predictor ######
    Table(N)
    results.append(tempArr) #1
    while(xrequired>X[len(X) - 1]):
##################Predictor step###################
        Pre_result = predictor()
        f(X[len(X) - 1] + h,Pre_result,i)
        tempArr = []
        Table(N + 1)
        tempArr.pop()
        results.append(format(Pre_result,'.' + str(no_of_digi) + 'f')) #2
        results.append(tempArr) #3

###############Corrector Step#####################
        corr_result = corrector()
        results.append(format(corr_result,'.' + str(no_of_digi) + 'f')) #4
        FUN.pop()
        f(X[len(X) - 1] + h, corr_result, i)
        tempArr = []
        Table(N + 1)
        tempArr.pop()
        results.append(tempArr)
        corr_result2 = corrector()
        results.append(format(corr_result2,'.' + str(no_of_digi) + 'f')) #5
## el loop de fe 7alet en el user mada5alsh no.terations
        counter = 3

        while(format(corr_result,'.' + str(no_of_digi) + 'f') != format(corr_result2,'.' + str(no_of_digi) + 'f') and (counter <= no_of_iter)):
            corr_result = corr_result2
            FUN.pop()
            f(X[len(X) - 1] + h,corr_result,i)
            tempArr = []
            Table(N + 1)
            tempArr.pop()### ana kol marra bamsa7 a5er list 3l4an e7na mesh 3ayzeen nesta5dem l values l
                     ### gedeeda w ngeeb beeha nabla gdeeda
            corr_result2 = corrector()
            results.append(format(corr_result2, '.' + str(no_of_digi) + 'f')) #
            counter+=1


        X.append(X[len(X) - 1] + h)
        Y.append(corr_result2)
        f(X[len(X) - 1] + h,corr_result2,i)
        if(len(FUN)>5):
            FUN.pop(0)



        results.append("X="+ str(format((X[len(X) - 1]), '.' + '3' + 'f'))+" is done")
#######################################
    return results
"""

r=[]
r=ode_adams_backward_difference(equation1,no_of_digi1,no_of_iter1,N1,X1,Y1,xrequired1)
for a in r:
    if type(a)==list:
        for g in a:
            print(g)
    else:
        print(a)
"""

