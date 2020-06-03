import numpy as np
import copy
def main():
    Size=int (input("Enter Matrix size : "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    print("Enter the initialization vector (separated by space): ")
    inp = list(map(float, input().split()))
    Matrix , Vector=ListToMatrix(Size ,entries , inp)
    print(Matrix)
    print(Vector)
    n=500
    re=0
    choice=int(input("Enter 1 to find Most Dom. Eigen Value , 2 to find Least Dom. , or 3 for the whole problem : "))
    if choice==1 :
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error %: "))
        itvector,itvalue,itrError ,Evalu , Evect =MostDominant (Matrix ,Vector ,n , re)
        TEvalue , Tnv = TrueError(Matrix,Evalu , 0)
        for i in range (0 ,len(itvalue)):
            print ("\u03BB = " ,itvalue[i])
            print ("Eigen vector : ")
            print (itvector[i])
            print ("Relative Error")
            print (itrError[i])
        print ("True Error = " ,TEvalue , " %")
    elif choice==2:
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error % : "))
        itvector,itvalue , itrError , Evalu ,Evect , test=LeastDominant (Matrix ,Vector ,n , re)
        TEvalue , Tnv = TrueError(Matrix,0 , Evalu)
        if not test :
            print ("\u03BB = " ,itvalue[0])
        for i in range (0 ,len(itvalue)):
            print ("\u03BB = " ,itvalue[i])
            print ("Eigen vector : ")
            print (itvector[i])
            print ("Relative Error")
            print (itrError[i])
        print ("True Error = " ,TEvalue , " %")
    elif choice ==3:
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error: "))
        Eval,Evec=Whole_Problem(Matrix,Vector,n,re ,Size)
        for i in range (0 ,len(Eval)):
            print ("\u03BB = " ,Eval[i])
            print ("Eigen vector : ")
            print (Evec[i])

def Whole_Problem(Matrix,Vector,n,re , Size):
     Valuez=[]
     Vectorz=[]
     a,b,c,x,y=MostDominant(Matrix,Vector,n,re)
     Valuez.append(x)
     Vectorz.append(y)
     w=Matrix
     temp=1;
     M=copy.deepcopy(Matrix)
     test=is_symmetric(M)
     i=0
     while test and i < len (Vector)-1 :
          M=deflate(M,Valuez[i],Vectorz[i])
          test=is_symmetric(M)
          if not test:
              break
          a,b,c,x,y=MostDominant(M,Vector,n,re)
          Valuez.append(x)
          Vectorz.append(y)
          i=i+1
          temp+=1
     while  temp<Size:
          Valuez.append("NULL")
          Vectorz.append(["NULL" ,"NULL" , "NULL"])
          print (temp)
          temp=temp+1
     return Valuez,Vectorz

def ListToMatrix(Size, Matrix, Guess):
    matrix = np.array(Matrix).reshape(Size, Size)
    vector = np.array(Guess).reshape(Size, 1)
    return matrix,vector

def MostDominant(Matrix, Guess,Iterations , re):  
    vector=Guess
    RE=100
    i=0
    pre=0
    itvectors =[]
    itvalues= []
    itrError=[]
    while RE>re and i<Iterations :
        Evector=Matrix.dot(vector)
        mx = Evector.max()
        mn = Evector.min()
        c=abs(mn)
        Evalue = mx
        if c>mx :
            Evalue = mn
        Evector=Evector / Evalue
        vector = Evector
        itvalues.append(Evalue)
        itvectors.append(Evector)
        i=i+1
        if i>0:
            RE=abs(((Evalue-pre)/Evalue )*100)
            itrError.append(RE)
        pre=Evalue
    return itvectors , itvalues , itrError , Evalue , Evector

def LeastDominant(Matrix,  Guess, Iterations , re) :
    vector=Guess
    test=Signular(Matrix)
    itvectors =[]
    itvalues= []
    itrError=[]
    if test:
        itvalues.append(0)
        return itvalues ,vector ,False
    matrix=np.linalg.inv(Matrix)
    RE=100
    i=0
    pre=0
    while RE>re and i<Iterations :
         Evector=matrix.dot(vector)
         mx = Evector.max()
         mn = Evector.min()
         c=abs(mn)
         Evalue = mx
         if c>mx :
             Evalue = mn
         Evector=Evector / Evalue
         vector = Evector
         i=i+1
         if i>0:
            RE=abs(((Evalue-pre)/Evalue )*100)
         pre=Evalue
         itvectors.append(Evector)
         itvalues.append (1/Evalue)
         itrError.append(RE)
    return itvectors , itvalues,itrError ,(1/Evalue) ,Evector, True
    
def nrm(x):
    return x/np.linalg.norm(x)

def deflate(A,curr_Evalue,x):
    if is_symmetric(A):
        return A-curr_Evalue*nrm(x).dot(np.transpose(nrm(x)))
    else:
        return False
    
def is_symmetric(A):
    return np.array_equal(A,np.transpose(A))

def TrueError (Matrix , Evalu , Evalumn):
    w, v = np.linalg.eig(Matrix )
    mx=w.max()
    mn=w.min()
    c=abs(mn)
    TEvalue = mx
    Tnv=mn
    if c>mx :
        TEvalue = mn
        Tnv=mx
    TEmn=((Tnv-Evalumn) /Tnv )*100
    TEmx=((TEvalue-Evalu) /TEvalue )*100

    return abs(TEmx) , abs(TEmn)

def Signular (Matrix):
    if(np.linalg.det(Matrix)==0):
        return True
    else:
        return False


def solve_Eigenvalue(size,list_of_entires,list_init_vector,Choice,iter_or_stoppingC,num_iteration,StoppingCriteria):

    List_Eig_values=[]
    List_Eig_vectors = []
    List_relative_error=[]
    Eig_value=0
    Eig_vector = 0
    True_error=0
    True_error_min = 0
    test=0 #for opition #2 --->least Dom.


    Size = int(size)
    entries = list(map(float,list_of_entires))
    inp = list(map(float,list_init_vector))
    Matrix, Vector = ListToMatrix(Size, entries, inp)
    n = 500
    re = 0
    #choice #1-->to find Most Dom.
    #choice #2 ----> to find Least Dom.
    #choice #3 ----> for the whole problem
    #// for iter_or_stoppingC ---> want to calculation with num_iteration or stopping_error
    choice = int(Choice)
    if choice == 1:
        ch = int(iter_or_stoppingC)
        if ch == 1:
            n = int(num_iteration)
        elif ch == 2:
            re = float(StoppingCriteria)
        List_Eig_vectors, List_Eig_values,  List_relative_error, Eig_value, Eig_vector = MostDominant(Matrix, Vector, n, re)
        True_error, True_error_min = TrueError(Matrix, Eig_value, 0)
    elif choice == 2:
        ch = int(iter_or_stoppingC)
        if ch == 1:
            n = int(num_iteration)
        elif ch == 2:
            re = float(StoppingCriteria)
        List_Eig_vectors, List_Eig_values, List_relative_error, Eig_value, Eig_vector, test = LeastDominant(Matrix, Vector, n, re)
        True_error, True_error_min = TrueError(Matrix, 0, Eig_value)
    elif choice == 3:
        ch = int(iter_or_stoppingC)
        if ch == 1:
            n = int(num_iteration)
        elif ch == 2:
            re = float(StoppingCriteria)
        List_Eig_values, List_Eig_vectors = Whole_Problem(Matrix, Vector, n, re, Size)

    return (List_Eig_values,
    List_Eig_vectors,
    List_relative_error,
    Eig_value,
    Eig_vector,
    True_error,
    test)
