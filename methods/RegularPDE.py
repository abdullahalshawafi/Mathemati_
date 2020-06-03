import numpy as np

#Mode 1: ( Regular Closed Region)

#L ->>> left boundry
#R ->>> right boundry
#U ->>> upper boundry
#D ->>> lower boundry
#H ->>> x axis step
#K ->>> y axis step
#X1,X2  ->>> x  period of the region   X2 > X1
#Y1,Y2  ->>> y  period of the region   Y2 > Y1



#The input equation parameters(make sure that all the equation is on one side and the other side is equal to zero)

#a  ->>> Uxx coefficient
#b  ->>> Uyy coefficient
#c  ->>> Ux coefficient
#d  ->>> Uy coefficient
#e  ->>> U coefficient
#f  ->>> Uxy coefficient
#EQN ->>> other functions like (2**X  OR   X*Y    OR    -2.1828*y(x*Y)  ............etc       )   but u must write it with respect to ( X,Y ) capital letters only 
#EQN ->>>(if there is no other functions in your equation ) input it like that         '0' 

###########################           Mode 1 TEST         #############################

#Closed_Region       (3,4,5,7,1/3,1/3,0,1,0,1,1,1,0,0,-2,0,'-2.71828**(X*Y)')

#Closed_Region       (3,4,5,7,1/3,1/3,0,1,0,1,1,1,0,0,0,0,'0')

#Closed_Region        (0,0,0,0,1/2,1/2,-1,1,-1,1,1,0,0,-2,0,0,'0')


def Closed_Region(L,R,U,D,H,K,X1,X2,Y1,Y2,a,b,c,d,e,f,EQN):

     Xsize = (int)(((X2-X1)/H)+1)
     Ysize = (int)(((Y2-Y1)/K)+1)
     GRID = np.full((Ysize, Xsize), 0.0)

     for x in range(Xsize):
       Y=0
       X=x*H
       GRID[0][x]=eval(D)

     for y in range(Ysize):
       Y=y*K
       X=0
       GRID[y][0]=eval(L)  
                       
     for y in range(Ysize):
       Y=y*K
       X=(Xsize-1)*H
       GRID[y][Xsize-1]=eval(R)

     for x in range(Xsize):
         X=x*H
         Y=(Ysize-1)*K
         GRID[Ysize-1][x]=eval(U)


     X=Y=0
     GRID[0][0]=(eval(D)+eval(L))/2

     Y=0
     X=(Xsize-1)*H
     GRID[0][Xsize-1]=(eval(D)+eval(R))/2


     Y=(Ysize-1)*K
     X=0
     GRID[Ysize-1][0]=(eval(U)+eval(L))/2

     Y=(Ysize-1)*K
     X=(Xsize-1)*H
     GRID[Ysize-1][Xsize-1]=(eval(U)+eval(R))/2

     nym_ofeqn=(Ysize-2)*(Xsize-2)
     outmatrix=np.zeros(nym_ofeqn)
     coefmatrix=np.zeros((nym_ofeqn,nym_ofeqn))
     coef_line=0

     #calculating the outmatrix
     for y in range(1,Ysize-1):
       for x in range(1,Xsize-1):

           #for the EQN 
           X=x*H
           Y=y*K

           temp=( (a/(H*H))-(c/(2*H)) )*GRID[y][x-1]+((a/(H*H))+(c/(2*H)))*GRID[y][x+1]+((b/(K*K))+(d/(2*K)))*GRID[y+1][x]+((b/(K*K))-(d/(2*K)))*GRID[y-1][x]+(((-2*a)/(H*H))+((-2*b)/(K*K))+e)*GRID[y][x]+((f/(H*K))*(GRID[y+1][x+1]-GRID[y-1][x+1]-GRID[y+1][x-1]+GRID[y-1][x-1]))+eval(EQN)
           outmatrix[coef_line]=temp*-1
           coef_line=coef_line+1

     #calculating the coefmatrix
     coef_line=0

     for y in range(1,Ysize-1):
       for x in range(1,Xsize-1):

           coefmatrix[coef_line][(Xsize-2)*(y-1)+x-1]       =   (((-2*a)/(H*H))+((-2*b)/(K*K))+e)   #CURRENT

           if (x-1) > 0:
               coefmatrix[coef_line][(Xsize-2)*(y-1)+x-2]   =   ((a/(H*H))-(c/(2*H)))               #LEFT

           if (x+1) < Xsize-1:
               coefmatrix[coef_line][(Xsize-2)*(y-1)+x]     =   ((a/(H*H))+(c/(2*H)))               #RIGHT

           if (y+1)< Ysize-1:
               coefmatrix[coef_line][(Xsize-2)*(y)+x-1]     =   ((b/(K*K))+(d/(2*K)))               #UP

           if (y-1)>0:
               coefmatrix[coef_line][(Xsize-2)*(y-2)+x-1]   =   ((b/(K*K))-(d/(2*K)))               #DOWN
          
           if(( (y+1) < (Ysize-1) ) and ( (x+1) < (Xsize-1) ) ) :                                   #RIGHT UP
                coefmatrix[coef_line][(Xsize-2)*(y)+x]      =   f/(H*K)                             
      
           if(( (y-1) > 0 ) and ( (x-1) > 0 )  ) :                                                  #LEFT DOWN   
                coefmatrix[coef_line][(Xsize-2)*(y-2)+x-2]  =   f/(H*K)

           if(( (y-1) > 0 ) and ( (x+1) < (Xsize-1) )  ) :                                          #RIGHT DOWN
                coefmatrix[coef_line][(Xsize-2)*(y-2)+x]    =   -f/(H*K)

           if(( (y+1) < (Ysize-1) ) and ( (x-1) > 0 )  ) :                                          #LEFT UP
                coefmatrix[coef_line][(Xsize-2)*(y)+x-2]    =   -f/(H*K)

           coef_line=coef_line+1


     coef_line=0 
     x_index=1
     y_inedx=0
     result=np.linalg.inv(coefmatrix).dot(outmatrix)
     for y in range(1,Ysize-1):
       y_inedx=y_inedx+1
       x_index=1
       for x in range(1,Xsize-1):
           #print('U' +str(x*10 +y)+'= '+str(result[coef_line]))
           GRID[x_index][y_inedx]=result[coef_line]
           x_index=x_index+1
           coef_line=coef_line+1
       

     return GRID
     
   

#Mode 2: ( Open Region from one side (Y side))

#L ->>> left boundry
#R ->>> right boundry
#D ->>> lower boundry
#H ->>> x axis step
#K ->>> y axis step
#X1,X2  ->>> x  period of the region   X2 > X1
#Y1  ->>> min y value

#The input equation parameters(make sure that all the equation is on one side and the other side is equal to zero)

#a  ->>> Uxx coefficient
#b  ->>> Uyy coefficient
#c  ->>> Ux coefficient
#d  ->>> Uy coefficient
#e  ->>> U coefficient
#f  ->>> Uxy coefficient
#EQN ->>> other functions like (2**X  OR   X*Y    OR    -2.1828*y(x*Y)  ............etc       )   but u must write it with respect to ( X,Y ) capital letters only 
#EQN ->>>(if there is no other functions in your equation ) input it like that         '0' 

#The additional equation (neumann) (solved with FD)

#For equation Uy = 5 for y=0 :

#FD_val  ->>> value for Uy i.e. 5
#YY  ->>> value for y at which the equation is valid i.e. 0
#rows  ->>> number of rows to compute PDE at

     


########################        Mode 2 TEST         #############################

# Open_Region        ('3','4*Y','7',1/3,1/5,0,1,0,-1,1,1,0,0,0,'0',5,0,1)

# Open_Region        (L,R,D,H,K,X1,X2,Y1,a,b,c,d,e,f,EQN,FD_val,YY,rows):


def Open_Region(L,R,D,H,K,X1,X2,Y1,a,b,c,d,e,f,EQN,FD_val,YY,rows):

     Xsize=(int)(((X2-X1)/H)+1)
     Ysize=rows+2
     GRID = np.full((Ysize, Xsize), 0.0)

     for x in range(Xsize):
       Y=0
       X=x*H
       GRID[0][x]=eval(D)


     for y in range(Ysize):
       Y=y*K
       X=0
       GRID[y][0]=eval(L)  
                       
     for y in range(Ysize):
       Y=y*K
       X=(Xsize-1)*H
       GRID[y][Xsize-1]=eval(R)

     X=Y=0
     GRID[0][0]=(eval(D)+eval(L))/2

     Y=0
     X=(Xsize-1)*H
     GRID[0][Xsize-1]=(eval(D)+eval(R))/2


     nym_ofeqn=(Ysize-2)*(Xsize-2)
     outmatrix=np.zeros(nym_ofeqn)
     coefmatrix=np.zeros((nym_ofeqn,nym_ofeqn))
     coef_line=0

     for x in range(1,Xsize-1):
             GRID[YY+1][x]=FD_val*K+GRID[YY][x]

  
     #calculating the outmatrix
     for y in range(1,Ysize-1):
       for x in range(1,Xsize-1):

           #for the EQN 
           X=x*H
           Y=y*K

           temp=((a/(H*H))-(c/(2*H)))*GRID[y][x-1]+((a/(H*H))+(c/(2*H)))*GRID[y][x+1]+((b/(K*K))+(d/(2*K)))*GRID[y+1][x]+((b/(K*K))-(d/(2*K)))*GRID[y-1][x]+(((-2*a)/(H*H))+((-2*b)/(K*K))+e)*GRID[y][x]+((f/(H*K))*(GRID[y+1][x+1]-GRID[y-1][x+1]-GRID[y+1][x-1]+GRID[y-1][x-1]))+eval(EQN)
           outmatrix[coef_line]=temp*-1
           coef_line=coef_line+1


     #calculating the coefmatrix
     coef_line=0

     for y in range(1,Ysize-1):
       for x in range(1,Xsize-1):
    
           coefmatrix[coef_line][(Xsize-2)*(y-1)+x-1]       =   ((b/(K*K))+(d/(2*K)))   #CURRENT
    
           if (x-1) > 0:
               coefmatrix[coef_line][(Xsize-2)*(y-1)+x-2]   =   -f/(H*K)              #LEFT
    
           if (x+1) < Xsize-1:
               coefmatrix[coef_line][(Xsize-2)*(y-1)+x]     =   f/(H*K)                #RIGHT
    
         #  if (y+1)< Ysize-1:
         #      coefmatrix[coef_line][(Xsize-2)*(y)+x-1]     =   ((b/(K*K))+(d/(2*K)))               #UP
    
           if (y-1)>0:
               coefmatrix[coef_line][(Xsize-2)*(y-2)+x-1]   =   (((-2*a)/(H*H))+((-2*b)/(K*K))+e)               #DOWN
          
          # if(( (y+1) < (Ysize-1) ) and ( (x+1) < (Xsize-1) ) ) :                                   #RIGHT UP
          #      coefmatrix[coef_line][(Xsize-2)*(y)+x]      =   f/(H*K)                             
      
           if(( (y-1) > 0 ) and ( (x-1) > 0 )  ) :                                                  #LEFT DOWN   
                coefmatrix[coef_line][(Xsize-2)*(y-2)+x-2]  =   ((a/(H*H))-(c/(2*H)))
    
           if(( (y-1) > 0 ) and ( (x+1) < (Xsize-1) )  ) :                                          #RIGHT DOWN
                coefmatrix[coef_line][(Xsize-2)*(y-2)+x]    =    ((a/(H*H))+(c/(2*H)))
    
         #  if(( (y+1) < (Ysize-1) ) and ( (x-1) > 0 )  ) :                                          #LEFT UP
         #       coefmatrix[coef_line][(Xsize-2)*(y)+x-2]    =   -f/(H*K)
    
           coef_line=coef_line+1



     coef_line=0 
     x_index=1
     y_inedx=0
     
     result=np.linalg.inv(coefmatrix).dot(outmatrix)
     for y in range(1,Ysize-1):
       y_inedx=y_inedx+1
       x_index=0
       for x in range(1,Xsize-1):
           #print('U' +str(x*10 +y+1)+'= '+str(result[coef_line]))
           #GRID[x_index][y_inedx]=result[coef_line]
           x_index=x_index+1
           coef_line=coef_line+1
     
     return GRID
  
 
