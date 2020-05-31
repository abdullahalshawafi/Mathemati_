#!/usr/bin/env python
# coding: utf-8

# In[261]:


import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy import lambdify
from sympy import symbols, solve
import math
from decimal import *
from fractions import Fraction
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
x = symbols('x')
y = symbols('y')


# to prevent floats errors
getcontext().prec = 8
acc = 10

utility = lambda x: round(x, acc)


# In[262]:


# helper function works as np.linespace but with acc contol

def getrange(start, end, step):

    arr = []

    x = Fraction(start)
    y = Fraction(end)
    while round(float(x), acc) <= round(float(y), acc):
        arr.append(x)
        x+= Fraction(step)

    return arr


# In[263]:






# In[264]:


# define point

"""
parametres:
x: x value for the point in the grid
y: y value for the point in the grid
is_bound: is this point on a boundry or not

other attributes:
(i_index, j_index): index of the point to be used in solve matirx
(up, down, left, right): points that around this point
irreg: is this point has alpha or beta != 1 or not
(alpha, beta): if point in !irreg should = 1
value: U value at this point should be a string if it's unknown

"""

class point():

    count = 0

    def __init__(self, x, y, is_bound):
        self.x = round(float(x), acc)
        self.y = round(float(y), acc)

        self.index = -1
        self.i_index = 0
        self.j_index = 0

        self.is_bound = is_bound

        self.irreg = False
        self.alpha = 1
        self.beta = 1

        self.right = []
        self.left = []
        self.up = []
        self.down = []

        self.value = 'x' + str(point.count)
        point.count+=1


    def __gt__(self, other):
        if(self.x >= other.x  and self.y >= other.y):
            return True
        else:
            return False

    def __eq__(self, other):
        if(abs(self.x - other.x) <= 0.0000001 and abs(self.y - other.y) <= 0.0000001):
            return True
        else:
            return False


# In[265]:


#define boundry

"""
parametres:

---------------------range and domain parameters---------------------
ly: start of y values
my: end of y values
lx: start of x values
mx: end of x values

---------------------boundry parameters---------------------
equation: the equation of the boundry in form f(x, y) = 0
value = U value at this boundry
"""

class boundry():


    def __init__(self, ly, my, lx, mx, equation, value):

        if len(solve(equation, y, check = False)) == 0:
            self.equation = lambdify(x, solve(equation, check = False))
        else:
            self.equation = lambdify(x, solve(equation, y, check = False))

        if len(solve(equation, x, check = False)) == 0:
            self.inv = lambdify(y, solve(equation , check = False))
        else:
            self.inv = lambdify(y, solve(equation, x, check = False))

        self.ly = ly
        self.my = my
        self.lx = lx
        self.mx = mx
        self.eq=equation
        self.value = lambdify([x,y], value)



# In[266]:


class Grid():

    #def __init__(self, start_x, end_x, start_y, end_y, h, k, boundries):
    def __init__(self, boundary, h, k):
        self.boundries = boundary
        self.start_x = self.get_start_x()
        self.end_x = self.get_end_x()

        self.start_y = self.get_start_y()
        self.end_y = self.get_end_y()

        self.h = h
        self.k = k

        #self.boundries = boundries


    def get_start_x(self):
        x_i=self.boundries[0].lx
        for bound in self.boundries:
            if bound.lx<x_i:
                x_i=bound.lx
        return x_i

    def get_end_x(self):
        x_f=self.boundries[0].mx
        for bound in self.boundries:
            if bound.mx>x_f:
                x_f=bound.mx
        return x_f

    def get_start_y(self):
        y_i=self.boundries[0].ly
        for bound in self.boundries:
            if bound.ly<y_i:
                y_i=bound.ly
        return y_i

    def get_end_y(self):
        y_f=self.boundries[0].my
        for bound in self.boundries:
            if bound.my>y_f:
                y_f=bound.my
        return y_f

    def Plot_Region(self):
        plt.style.use('dark_background')
        plt.figure(figsize=(18,9),dpi =200)
        for bound in self.boundries:
            x_data = np.linspace(bound.lx, bound.mx, 10000)
            y_data = list(map(bound.equation, x_data))
            plt.plot(x_data,y_data, label=bound.eq)

        plt.xticks(np.arange(self.start_x, self.end_x + self.h, self.h))
        plt.yticks(np.arange(self.start_y, self.end_y + self.k, self.k))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.savefig('Boundeies')


    def get_boundry_rows_points(self):
        boundry_rows_points = []

        # loop on the rows in the grid an get all boundry points
        for i in getrange(self.start_y, self.end_y, self.k):
            row = []
            for s in self.boundries:
                if i >= round(s.ly, acc) and i <= round(s.my, acc):
                    if s.ly == s.my:
                        for j in np.arange(s.lx, s.mx + self.k, self.k):
                            p = point(utility(j), s.inv(j)[0], True)
                            p.value = s.value(utility(j), s.inv(j)[0])
                            row.append(p)
                    else:
                        for sol in s.inv(float(i)):
                            if sol >= s.lx and sol <= s.mx:
                                p = point(round(sol, acc), utility(float(i)), True)
                                p.value = s.value(round(sol, acc), utility(float(i)))
                                row.append(p)
            if len(row) != 0:
                boundry_rows_points.append(row)

        # this copy will be used in avarege

        temp_rows = boundry_rows_points.copy()

        # get the unique boundry points in every row
        for r in range(len(boundry_rows_points)):
            boundry_rows_points[r], counts = np.unique(boundry_rows_points[r], return_counts=True)

        # get avarege for intersection points
        for r in range(len(boundry_rows_points)):
            for p in range(len(boundry_rows_points[r])):
                ls = [i for i,x in enumerate(temp_rows[r]) if x == boundry_rows_points[r][p]]

                if (len(ls) > 1):
                    sum_v = 0
                    for i in ls:
                        sum_v += temp_rows[r][i].value

                    boundry_rows_points[r][p].value = sum_v / len(ls)

        return boundry_rows_points

    def get_boundry_cols_points(self):
        boundry_cols_points = []
        h=self.h
        k=self.k
        bounds=self.boundries
        # loop on the coluomns in the grid an get all boundry points
        for i in getrange(self.start_x, self.end_x, h):
            row = []
            for s in bounds:
                if i >= s.lx and i <= s.mx:
                    if s.lx == s.mx:

                        for j in np.arange(s.ly, s.my + self.k, self.k):
                            p = point(round(s.equation(j)[0], acc), utility(j), True)
                            p.value = s.value(utility(j), round(s.equation(j)[0], acc))
                            row.append(p)
                    else:
                        for sol in s.equation(float(i)):
                            if sol >= s.ly and sol <= s.my:
                                p = point(utility(float(i)), round(sol, acc), True)
                                p.value = s.value(utility(float(i)), round(sol, acc))
                                row.append(p)
            if len(row) != 0:

                boundry_cols_points.append(row)

        # this copy will be used in avarege
        temp_cols = boundry_cols_points.copy()

        # get the unique boundry points in every coluomns
        for r in range(len(boundry_cols_points)):
            boundry_cols_points[r], counts = np.unique(boundry_cols_points[r], return_counts=True)

        # get avarege for intersection points
        for r in range(len(boundry_cols_points)):
            for p in range(len(boundry_cols_points[r])):
                ls = [i for i,x in enumerate(temp_cols[r]) if x == boundry_cols_points[r][p]]
                if (len(ls) > 1):
                    sum_v = 0
                    for i in ls:
                        sum_v += temp_cols[r][i].value

                    boundry_cols_points[r][p].value = sum_v / len(ls)

        return boundry_cols_points

    def get_points(self, boundry_rows_points, boundry_cols_points):

        #loop on the grid and get all points between boundry points
        #also set (up, down, left, right) with (irreg, alpha, beta)
        #and the index (i_index, j_index) and index
        h=self.h
        k=self.k
        points = []
        r = 1
        count = 0
        for j in getrange(self.start_y + self.k, self.end_y - self.k, self.k):
            c = 1
            for i in getrange(self.start_x + self.h, self.end_x - self.h, self.h):

                i_bound = 0
                while i_bound < len(boundry_rows_points[r]):
                    j_bound = 0
                    while j_bound < len(boundry_cols_points[c]):

                         if  (len(boundry_rows_points[r]) > 1 and len(boundry_cols_points[c]) > 1 and
                            i_bound + 1 < len(boundry_rows_points[r]) and
                            j_bound + 1 < len(boundry_cols_points[c]) and
                            i > boundry_rows_points[r][i_bound].x and
                            i < boundry_rows_points[r][i_bound + 1].x and
                            j < boundry_cols_points[c][j_bound + 1].y and
                            j > boundry_cols_points[c][j_bound].y):

                            p = point(i, j, False)
                            p.i_index = r - 1
                            p.j_index = c -1

                            #right
                            if i + h >= boundry_rows_points[r][i_bound + 1].x:
                                boundry_rows_points[r][i_bound + 1].alpha = round((boundry_rows_points[r][i_bound + 1].x - i) / self.h, acc)
                                if boundry_rows_points[r][i_bound + 1].alpha != 1:
                                    boundry_rows_points[r][i_bound + 1].irreg = True
                                p.right.append((boundry_rows_points[r][i_bound + 1]))
                            else:
                                p.right.append((point(round(i + h, acc), j, False)))

                            #up
                            if j + k >= boundry_cols_points[c][j_bound + 1].y:
                                boundry_cols_points[c][j_bound + 1].beta = round((boundry_cols_points[c][j_bound + 1].y - j) / self.k, acc)
                                if boundry_cols_points[c][j_bound + 1].beta != 1:
                                    boundry_cols_points[c][j_bound + 1].irreg = True
                                p.up.append((boundry_cols_points[c][j_bound + 1]))
                            else:
                                p.up.append((point(i, j + k, False)))

                            #left
                            if i - h <= boundry_rows_points[r][i_bound].x:
                                boundry_rows_points[r][i_bound].alpha = round((i - boundry_rows_points[r][i_bound].x) / self.h, acc)
                                if boundry_rows_points[r][i_bound].alpha != 1:
                                    boundry_rows_points[r][i_bound].irreg = True
                                p.left.append((boundry_rows_points[r][i_bound]))
                            else:
                                p.left.append((point(i - h, j, False)))

                            #down
                            if j - k <= boundry_cols_points[c][j_bound].y:
                                boundry_cols_points[c][j_bound].beta = round((j - boundry_cols_points[c][j_bound].y) / self.k, acc)
                                if boundry_cols_points[c][j_bound].beta != 1.0:
                                    boundry_cols_points[c][j_bound].irreg = True
                                p.down.append((boundry_cols_points[c][j_bound]))
                            else:
                                p.down.append((point(i, j - k, False)))

                            p.index = count
                            count+=1
                            points.append(p)

                         j_bound+=1
                    i_bound+=1
                c+=1
            r+=1

        for p in range(len(points)):
            if points[p].up[0] in points:
                x = points.index(points[p].up[0])
                points[p].up[0] = points[x]

            if points[p].down[0] in points:
                x = points.index(points[p].down[0])
                points[p].down[0] = points[x]


            if points[p].right[0] in points:
                x = points.index(points[p].right[0])
                points[p].right[0] = points[x]



            if points[p].left[0] in points:
                x = points.index(points[p].left[0])
                points[p].left[0] = points[x]

        return points






# In[267]:


class PDE_Solver :
    def __init__(self,point,grid):
        self.list_points=point
        self.CoeffMatrix=[]
        self.OutputMatrix=[]
        self.grid=grid
        self.dxx=0
        self.dx=0
        self.dyy=0
        self.dy=0
        self.u_coeff=0
        self.function=0
        self.Number_Of_Points=len(self.list_points)
        self.h=self.grid.h
        self.k=self.grid.k

    def Get_Parameters(self,dxx,dyy,dx,dy,u,function):
        self.dxx=lambdify([x,y], dxx)
        self.dx=lambdify([x,y], dx)
        self.dyy=lambdify([x,y], dyy)
        self.dy=lambdify([x,y], dy)
        self.u_coeff=lambdify([x,y], u)
        self.function=lambdify([x,y], function)

    def Solution(self):

        for p in self.list_points:
            Up_Beta=p.up[0].beta
            Down_Beta=p.down[0].beta
            Right_Alpha=p.right[0].alpha
            Left_Alpha=p.left[0].alpha
            Row_Matrix=np.zeros(self.Number_Of_Points)
            x=p.x
            y=p.y

            u_term1=2*self.dxx(x,y)/(Right_Alpha*Left_Alpha*self.h**2)
            u_term2=2*self.dyy(x,y)/(Up_Beta*Down_Beta*self.k**2)
            u_term3=self.dx(x,y)*(Right_Alpha-Left_Alpha)/(self.h*Left_Alpha*Right_Alpha)
            u_term4=self.dy(x,y)*(Up_Beta-Down_Beta)/(self.k*Up_Beta*Down_Beta)
            u_term5=-1* self.u_coeff(x,y)
            u=u_term1+u_term2+u_term3+u_term4+u_term5
            u=-1*u
            Row_Matrix[p.index]=u
            UpperCoeff=0
            LowerCoeff=0
            RightCoeff=0
            LeftCoeff=0
            Output=0

            #Solving the up point :

            if p.up[0].is_bound==True :
                Term1=2*self.dyy(x,y)/(Up_Beta*(Up_Beta+Down_Beta)*self.k**2)
                Term2=self.dy(x,y)*Down_Beta/(self.k*Up_Beta*(Up_Beta+Down_Beta))
                Term = Term1+Term2
                Term=Term*p.up[0].value
                Output=Output+Term
                UpperCoeff=0
            else :
                up_term1=2*self.dyy(x,y)/(Up_Beta*(Up_Beta+Down_Beta)*self.k**2)
                up_term2=self.dy(x,y)*Down_Beta/(self.k*Up_Beta*(Up_Beta+Down_Beta))
                UpperCoeff=up_term1+up_term2
                Row_Matrix[p.up[0].index]=UpperCoeff

            #Solving the down point
            if p.down[0].is_bound==True: #Boundary
                Term1=2*self.dyy(x,y)/(Down_Beta*(Up_Beta+Down_Beta)*self.k**2)
                Term2=self.dy(x,y)*Up_Beta/(self.k*Down_Beta*(Up_Beta+Down_Beta))
                Term=Term1-Term2
                Term=Term*p.down[0].value
                Output=Output+Term
                LowerCoeff=0
            else :
                low_term1=2*self.dyy(x,y)/(Down_Beta*(Up_Beta+Down_Beta)*self.k**2)
                low_term2=self.dy(x,y)*Up_Beta/(self.k*Down_Beta*(Up_Beta+Down_Beta))
                LowerCoeff=low_term1+low_term2
                Row_Matrix[p.down[0].index]=LowerCoeff

            #Solving Right :
            if p.right[0].is_bound==True: #Boundary
                Term1=2*self.dxx(x,y)/(Right_Alpha*(Right_Alpha+Left_Alpha)*self.h**2)
                Term2=self.dx(x,y)*Right_Alpha/(self.h*Right_Alpha*(Right_Alpha+Left_Alpha))
                Term=Term1+Term2
                Term=Term*p.right[0].value
                Output=Output+Term
                RightCoeff=0
            #Not Boundary :
            else :
                right_term1=2*self.dxx(x,y)/(Right_Alpha*(Right_Alpha+Left_Alpha)*self.h**2)
                right_term2=self.dx(x,y)*Left_Alpha/(self.h*Right_Alpha*(Right_Alpha+Left_Alpha))
                RightCoeff=right_term1+right_term2
                Row_Matrix[p.right[0].index]=RightCoeff

            #Solving Left
            if p.left[0].is_bound==True: #Boundary
                Term1=2*self.dxx(x,y)/(Left_Alpha*(Left_Alpha+Right_Alpha)*self.h**2)
                Term2=self.dx(x,y)*Right_Alpha/(self.h*Left_Alpha*(Right_Alpha+Left_Alpha))
                Term=Term1-Term2
                Term=Term*p.left[0].value
                Output=Output+Term
                LeftCoeff=0
            #Not Boundary :
            else :
                left_term1=2*self.dxx(x,y)/(Left_Alpha*(Right_Alpha+Left_Alpha)*self.h**2)
                left_term2=self.dx(x,y)*Right_Alpha/(self.h*Left_Alpha*(Right_Alpha+Left_Alpha))
                LeftCoeff=left_term1+left_term2
                Row_Matrix[p.left[0].index]=LeftCoeff

            Output=Output-self.function(x,y)
            self.OutputMatrix.append(Output)
            self.CoeffMatrix.append(Row_Matrix)





    def Solve(self):
        self.Solution()
        b=np.array(self.OutputMatrix)
        A=np.array(self.CoeffMatrix)
        if self.Number_Of_Points==1:
            return b[0]/A[0]
        else :
            A_Inverse=np.linalg.inv(A)
            x=A_Inverse.dot(b)
            return -1*x
    def Solve_At_Point(self,point):
        x=point.x
        y=point.y
        Point=point
        for p in self.list_points:
            if p.x==x and p.y==y:
                Point=p
                Sol_Vector=self.Solve()
                return Sol_Vector[Point.index]
        raise ValueError('Invaid Point')
