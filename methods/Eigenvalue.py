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
    choice=int(input("Enter 1 to find Most Dom. Eigen Value , 2 to find Least Dom. , 3 to find Deflated matrix , or 4 for the whole problem : "))
    if choice==1 :
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error %: "))
        Evalu,vector=MostDominant (Matrix ,Vector ,n , re)
        TEvalue , Tnv = TrueError(Matrix,Evalu , 0)
        print ("\u03BB = " ,Evalu)
        print ("True Error = " ,TEvalue , " %")
        print ("Eigen vector : ")
        print (vector)
    elif choice==2:
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error % : "))
        Evalu,vector , test=LeastDominant (Matrix ,Vector ,n , re)
        TEvalue , Tnv = TrueError(Matrix,0 , Evalu)
        print ("\u03BB = " ,Evalu)
        if test :
            print ("True Error = " ,Tnv , " %")
            print ("Eigen vector : ")
            print (vector)
    elif choice ==3:
        Eval=int (input("Enter Eigen value: "))
        matrix=deflate(Matrix ,Eval,Vector )
        print ("The deflated matrix :")
        print(matrix)
    elif choice ==4:
        ch=int (input("Enter 1 if you need to Enter num. of iterations or 2 for stopping relative error: "))
        if ch==1 :
             n=int (input("Enter number of iterations: "))
        elif ch==2:
            re=float (input("Enter stopping relative error: "))
        Eval,Evec=Whole_Problem(Matrix,Vector,n,re)
        print ("\u03BB = " ,Eval)
        print ("Eigen vectors = ")
        print('\n'.join(map(str, Evec)))
       
        

def Whole_Problem(Matrix,Vector,n,re):
     Valuez=[]
     Vectorz=[]
     x,y=MostDominant(Matrix,Vector,n,re)
     Valuez.append(x)
     Vectorz.append(y)
     w=Matrix
     M=copy.deepcopy(Matrix)
     #for i in range(0,len(Vector)-1):
     test=is_symmetric(M)
     i=0
     while ( test) and i < len (Vector)-1 :
          M=deflate(M,Valuez[i],Vectorz[i])
          x,y=MostDominant(M,Vector,n,re)
          Valuez.append(x)
          Vectorz.append(y)
          i=i+1
          test=is_symmetric(M)
    # x,y=LeastDominant(w,  Vector, n , re)
    # Valuez.append(x)
     #Vectorz.append(y)
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
        i=i+1
        if i>0:
            RE=abs(((Evalue-pre)/Evalue )*100)
        pre=Evalue
    return Evalue , Evector

def LeastDominant(Matrix,  Guess, Iterations , re) :
    vector=Guess
    test=Signular(Matrix)
    if test:
        return 0 ,vector ,False
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
    return (1/Evalue) , Evector , True
    
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
main()




