######## Definition of function solving ODE using Predictor Corrector using
######## Adam's method with backward difference#######
######## This problem solves the equations till the fourth order(accuracy) and solves only 1st degree ODEs
from math import e #### Added this to be able to solve functions containing e ############
def ode_adams_backward_difference():
    equation = input("Enter the RHS of the equation here: ") #This equation may contain only x,y,e,+,-,*,/,**(power).
########### Checking that the equation is a valid one ############
###Assign arbitary values for x & y to test the validity of the equation####
    x = 2.3
    y = 1.2
    while 1:
        try:
            eval(equation)
            break
        except:
            equation = input("Invalid Equation!!! Please enter the RHS of the equation here(using these operators + - * / **): ")
############# Check which is the terminating condition #####################
    choice = int(input("Please select whether you want to stop by default(1) or to stop after a certain number of iterations(2) or until a fixed number of digits becomes constant(3) : "))
    ######Default values for number of digits and itertions
    no_of_digi = 4  ##We can change the default to whatever value
    no_of_iter = 2 ###Just a place holder, not used unless choice ==2
    while 1:
        if (choice == 1):
            break
        elif(choice == 2):
            no_of_iter = int(input("Please enter the number of iterations to stop at:"))
            break
        elif(choice == 3):
            no_of_digi = int(input("Please enter the number of fixed digits to stop at:"))
            break
        else:
            choice = int(input("Please select (1or2) whether you want to stop after a certain number of iterations(1) or until a fixed number of digits becomes constant(2): "))
#############
    N = int(input("N numbers"))
    n = N
    i = 0
    FUN = []

###################################
    def f(x, y, i):
    #########
        try: #### Added as a second line of defense to avoid errors since eval() function
             #### is very dangerous ####
            ev = eval(equation)
            FUN.append(float(ev))
        except:
            print("invalid equation")
        return
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
    X = []
    Y = []

    while i < N:
        x = float(input("X"))
        X.append(x)
        y = float(input("Y"))
        Y.append(y)
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
    xrequired = float(input("X at which y is to be calculated: "))

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
    for a in tempArr:
        print(a)
    while(xrequired> X[len(X) - 1]):
##################Predictor step###################
        Pre_result = predictor()
        f(X[len(X) - 1] + h,Pre_result,i)
        tempArr = []
        Table(N + 1)
        tempArr.pop()
        for a in tempArr:
            print(a)
###############Corrector Step#####################
        corr_result = corrector()
        print("#1 :  " + format(corr_result,'.' + str(no_of_digi) + 'f'))
        FUN.pop()
        f(X[len(X) - 1] + h, corr_result, i)
        tempArr = []
        Table(N + 1)
        tempArr.pop()
        for a in tempArr:
            print(a)
        corr_result2 = corrector()
        print("#2 :  " + format(corr_result2,'.' + str(no_of_digi) + 'f'))
## el loop de fe 7alet en el user mada5alsh no.terations
        counter = 3
        Continue = True
        if ((choice == 2 and no_of_iter < 3) or ((format(corr_result,'.' + str(no_of_digi) + 'f') == format(corr_result2,'.' + str(no_of_digi) + 'f'))and (choice==1 or choice ==3))):
            Continue = False
        while(Continue):
            corr_result = corr_result2
            FUN.pop()
            f(X[len(X) - 1] + h,corr_result,i)
            tempArr = []
            Table(N + 1)
            tempArr.pop()### ana kol marra bamsa7 a5er list 3l4an e7na mesh 3ayzeen nesta5dem l values l
                     ### gedeeda w ngeeb beeha nabla gdeeda
            corr_result2 = corrector()
            print("#" + str(counter) + " :  " + format(corr_result2, '.' + str(no_of_digi) + 'f'))
            counter+=1
            if (choice == 3 or choice==1):
                Continue = format(corr_result,'.' + str(no_of_digi) + 'f') != format(corr_result2,'.' + str(no_of_digi) + 'f')
            elif(choice == 2):
                Continue = counter <= no_of_iter 
        X.append(X[len(X) - 1] + h)
        Y.append(corr_result2)
        f(X[len(X) - 1] + h,corr_result2,i)
        if(len(FUN)>5):
            FUN.pop(0)
#######################################
    return
ode_adams_backward_difference()