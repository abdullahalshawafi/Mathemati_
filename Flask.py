from flask import Flask, render_template, url_for, request, redirect
from methods.PolynomialInterpolation import Newton, LaGrange
from methods.Bezier import bezier_curve_bin
from methods.SplineInterpolation import linear_spline, quad_spline,cubic_spline, get_interval_list
from methods.Regression import Nonlinear_Regression, TrueError, Curve_Family_Detective, Linearized_Regression, Surface_Fit_Beta
from methods.Differentiation import  TableDeriv, FuncDeriv
from methods.NewtonCotes import Trapezoidal_Integ, Trapezoidal_error, Trapezoidal_Double_Integ, single_mixe_rule, double_mixed_rule, triple_mixed_rule
from methods.Romberg import RombergRule
from methods.Gauss_Quadrature import myfun, Exact
from methods.ODE_Kutta import rungeKutta
from methods.ODE_Adams import  ode_adams_backward_difference
from methods.RegularPDE import Open_Region, Closed_Region
from methods.PDE_Solve import Grid, PDE_Solver, boundry , point
from methods.LinearSystems import solve_linear_systems

from methods.ODE_Adams import  ode_adams_backward_difference
from methods.ODE_milne import milne
import numpy as np
from methods.NewtonRaphson import Newton_Raphson
from methods.FixedPoint import FixedPointIteration
from methods.Eigenvalue import solve_Eigenvalue

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'edcb30ed4a6a5b467a2ed529ed889dbf'

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')

@app.route("/Credits")
def Credits():
    return render_template('Credits.html', title='Credits', css="Credits.css", wing="Neon Green Header.svg", logo="Logo.svg")

@app.route("/Contact")
def Contact():
    return render_template('Contact.html', title='Contact', css="Contact.css", wing="Neon Green Header.svg", logo="Logo.svg")

@app.route("/PolynomialInterpolation", methods=['GET', 'POST'])
def PolynomialInterpolation():
    PolynomialFunction = ""
    if request.method == 'POST':
        Method = ''
        Degree = -1

        NumPoints = 0
        X_Points = []
        Y_Points = []

        if 'Method' in request.form:
            Method = request.form['Method']


        if Method=="Newton" and (request.form['Degree']) :
            Degree = int(request.form['Degree'])

        while (request.form["X_" + str(NumPoints)]) and (request.form["Y_" + str(NumPoints)]) :

            Xtemp =float((request.form["X_" + str(NumPoints)]))
            if NumPoints>0 :
                if Xtemp != X_Points[NumPoints-1]:
                    X_Points.append(float((request.form["X_" + str(NumPoints)])))
                    Y_Points.append(float((request.form["Y_" + str(NumPoints)])))
            else:
                X_Points.append(float((request.form["X_" + str(NumPoints)])))
                Y_Points.append(float((request.form["Y_" + str(NumPoints)])))

            NumPoints += 1


        NumPoints=len(X_Points)
        if Method and NumPoints > 0 and (Degree>-1 or Method=='Lagrange') and (NumPoints)>= (Degree+1):

            X_val = 0
            if Method == "Newton":
                X_diff_val = 0
                X_val = 0
                #if request.form["Xderivative"]:
                 #   X_diff_val = float(request.form["Xderivative"])
                #if request.form["Xvalue"]:
                 #   X_val = float(request.form["Xvalue"])
                DT, Y_val, PolynomialFunction, Y_diff_val, PolynomialDerivativeFunction, ResidualError = Newton(X_Points, Y_Points, NumPoints, X_val, Degree)
                ParametricX ,ParametricY = bezier_curve_bin(NumPoints,X_Points,Y_Points)
                return render_template('PolynomialInterpolation.html', title='Polynomial Interpolation', css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg", Method = Method, PolynomialFunction = PolynomialFunction , PolynomialDerivativeFunction= PolynomialDerivativeFunction, ResidualError = ResidualError, ParametricX=ParametricX,ParametricY=ParametricY)

            elif Method == "Lagrange":
                #if request.form["Xvalue"]:

                 #   X_val = float(request.form["Xvalue"])
                Y_val, PolynomialFunction = LaGrange(X_Points, Y_Points, NumPoints, X_val)
                ParametricX, ParametricY = bezier_curve_bin(NumPoints, X_Points, Y_Points)
                return render_template('PolynomialInterpolation.html', title='Polynomial Interpolation', css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg", Method = Method, PolynomialFunction = PolynomialFunction, ParametricX=ParametricX,ParametricY=ParametricY)
        return redirect(url_for('PolynomialInterpolation'))
    else:
        return render_template('PolynomialInterpolation.html', title='Polynomial Interpolation', css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg", PolynomialFunction = PolynomialFunction)

@app.route("/SplineInterpolation", methods=['GET', 'POST'])
def SplineInterpolation():
    if request.method == 'POST':
        Numbers =[]
        NumPoints = 0

        while (request.form['x_coordinates'+str(NumPoints)]) and (request.form['y_coordinates'+str(NumPoints)]) :
           Numbers.append([float((request.form['x_coordinates'+str(NumPoints)])),float((request.form['y_coordinates'+str(NumPoints)]))])
           NumPoints +=1

        print(NumPoints,Numbers)

        LinearSpline = linear_spline(NumPoints,Numbers)
        IntervalList = get_interval_list(NumPoints,Numbers)
        QuadraticSpline = quad_spline(NumPoints,Numbers)
        CubicSpline = cubic_spline(NumPoints,Numbers)
        print(LinearSpline)
        print(QuadraticSpline)
        print(CubicSpline)
        print(IntervalList)
        return render_template('SplineInterpolation.html', title='Spline Interpolation', css="SplineInterpolation.css",wing="CF Header.png", logo="Logo.svg",NumPoints = NumPoints-1, IntervalList=IntervalList,LinearSpline=LinearSpline, QuadraticSpline=QuadraticSpline, CubicSpline=CubicSpline)

    else:
        return render_template('SplineInterpolation.html', title='Spline Interpolation', css="SplineInterpolation.css", wing="CF Header.png", logo="Logo.svg" , eq="")

@app.route("/LeastSquareReg", methods=['GET', 'POST'])
def LeastSquareReg():
    if request.method == 'POST':
        Method = ''
        print("Method=", Method)
        if 'Method' in request.form:
            Method  = request.form['Method']
            print("Method=", Method)
        if Method == 'Nonlinear':
            Equation = request.form['Nonlinear_Equation']
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
                i += 1
            if len(xdata)>=3:
                result, Error = Nonlinear_Regression(xdata, ydata, Equation, 4);
                TrueErr = TrueError(ydata, 4);
                r=round((abs(Error-TrueErr)/TrueErr)**0.5,4);
            else:
                result="The data set is too small"
                Error='...'
                TrueErr='...';
                r='...'

            if result and TrueErr:
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results=result, Error=Error, TrueErr=TrueErr, r=r)
        elif Method == 'Linearized':
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
                i += 1
            j = 0
            Fdata = [request.form['Abdullah_Knows_It_All']]
            while request.form['term' + str(j)]:
                Fdata.append(request.form['term' + str(j)])
                j += 1

            LHS, RHS, Constants, Sr = Linearized_Regression(xdata, ydata, Fdata, 4)

            if  ydata and xdata and LHS !="" :
                TrueErr = TrueError(ydata, 4)
                r=round((abs(Sr-TrueErr)/TrueErr)**0.5,4)
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results=RHS, Error=Sr, TrueErr=TrueErr, r=r)
            elif not ydata or not xdata:
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results='Missing Points.', Error='...', TrueErr='...', r='...')
            elif xdata and ydata:
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results='Singular Matrix', Error='...', TrueErr='...', r='...')

        elif Method == 'Best-Fitting-Family-of-Curves':
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
                i += 1
            result, Family, Error, STnd = Curve_Family_Detective(xdata, ydata, 4);
            TrueErr = TrueError(ydata, 4);
            r=round((abs(Error-TrueErr)/TrueErr)**0.5,4);
            if result !="" and Error !="" :
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results=result, Error=Error, TrueErr=TrueErr, r=r, family=Family + ' curves')
            elif not xdata or not ydata:
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results='Missing Points', Error='...', TrueErr='...', r='...', family= ' ...')
            elif xdata and ydata:
                return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results='Singular Matrix', Error='...', TrueErr='...', r='...', family= ' ...')

        return redirect(url_for('LeastSquareReg'))
    else:
        return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/SurfaceFitting", methods=['GET', 'POST'])
def SurfaceFitting():
    if request.method == 'POST':
        Sr = 0
        LHS = 0
        i = 0
        xdata = []
        ydata = []
        zdata = []
        while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!='' and request.form['z_coordinates' + str(i)]!=''):
            xdata.append(float(request.form['x_coordinates' + str(i)]))
            ydata.append(float(request.form['y_coordinates' + str(i)]))
            zdata.append(float(request.form['z_coordinates' + str(i)]))
            i += 1
        j = 0
        Fdata = [request.form['Abdullah_Knows_It_All']]
        while request.form['term' + str(j)]:
            Fdata.append(request.form['term' + str(j)])
            j += 1

        if xdata and Fdata:
            LHS, RHS, Constants, Sr = Surface_Fit_Beta(xdata, ydata, zdata, Fdata, 4)

        if LHS and not Sr == '':
            print(LHS, Sr)
            return render_template('SurfaceFitting.html', title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png", logo="Logo.svg", results=RHS, Error=Sr)
        elif not xdata:
            return redirect(url_for('SurfaceFitting'))
        else:
            return render_template('SurfaceFitting.html', title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png", logo="Logo.svg", results='Singular Matrix', Error='...')
    else:
        return render_template('SurfaceFitting.html', title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/Differentiation", methods=['GET', 'POST'])
def Differentiation():
    if request.method == 'POST':
       # print(request.form)
        Method = ''
        Method = request.form['Method']
        Calculation_Point = 0
        Calculation_Point = float(request.form['Calculation Point'])
        if Method == 'Table' :
            x = []
            y = []
            i = 0
            while (request.form['x' + str(i)]!='' and request.form['y' + str(i)]!=''):
                x.append(float(request.form['x' + str(i)]))
                y.append(float(request.form['y' + str(i)]))
                i += 1

            results = TableDeriv(Calculation_Point, x, y)
        else:
            Function = ''
            Function = request.form['Function']
            results = []
            h = 0
            order = 0
            h = float(request.form['step'])
            order = float(request.form['order'])
            results = FuncDeriv(Function, h, order, Calculation_Point)

        return render_template('Differentiation.html', title='Differentiation', css="Differentiation.css", wing="SE - Copy.png", logo="Logo Crimson.svg" , results = results , Method = Method)

    else:
        return render_template('Differentiation.html', title='Differentiation', css="Differentiation.css", wing="SE - Copy.png", logo="Logo Crimson.svg" )

@app.route("/Integration", methods=['GET', 'POST'])
def Integration():
    if request.method == 'POST':
        Dim=''
        if 'Dim' in request.form:
            NumOfVar=request.form['Dim']
            if NumOfVar == '1':
                function=request.form['func']
                function=function.replace("^","**")
                function=function.replace("PI","pi")
                x1=float(request.form['x1'])
                x2=float(request.form['x2'])
                N=int(request.form['n1'])
                if N > 6:
                    Result="N > 6"
                    error=""
                else:
                    Result,error=myfun(function,x1,x2,1,1,N)
                exact=Exact(function,x1,x2,1,1,1,1,1)
                ResultTrap=Trapezoidal_Integ(function,x1,x2,N)
                ResultMin,ErrorMin=single_mixe_rule(function,x1,x2,N)
                OrderOfError=int(request.form['OrderOfError'])
                if(OrderOfError%2==0):
                    ResultRom=RombergRule(function, int(NumOfVar),x1,x2,1,1,1,1,OrderOfError)
                    print(ResultRom)
                    ResultRom=ResultRom[0]
                else:
                    ResultRom="Order of Error must be even"

                TrapError=Trapezoidal_error(function,x1,x2,N)
                return render_template('Integration.html', title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",Dim = NumOfVar,function=function,x1=x1,x2=x2,n1=N,Result=Result,exact=exact,error=error,ResultTrap=ResultTrap,TrapError=TrapError,ResultMin=ResultMin,ErrorMin=ErrorMin,ResultRom=ResultRom,OrderOfError=OrderOfError)
            elif NumOfVar == '2':
                function=request.form['func']
                x1=float(request.form['x1'])
                x2=float(request.form['x2'])
                N=int(request.form['n1'])
                y1=float(request.form['y1'])
                y2=float(request.form['y2'])
                N2=int(request.form['n2'])
                if N > 6:
                    Result="N > 6"
                    error=""
                else:
                    Result,error=myfun(function,x1,x2,y1,y2,N)
                ResultMin=double_mixed_rule (function,x1,x2,N,y1,y2,N2)
                exact=Exact(function,x1,x2,y1,y2,1,1,2)
                ResultTrap=Trapezoidal_Double_Integ(function,x1,x2,N,y1,y2,N2)
                OrderOfError=int(request.form['OrderOfError'])
                if(OrderOfError%2==0):
                    ResultRom=RombergRule(function, int(NumOfVar),x1,x2,y1,y2,1,1,OrderOfError)
                    print(ResultRom)
                    ResultRom=ResultRom[0]
                else:
                    ResultRom="Order of Error must be even"

                return render_template('Integration.html', title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",Dim = NumOfVar,function=function,x1=x1,x2=x2,y1=y1,y2=y2,n2=N2,n1=N,Result=Result,exact=exact,error=error,ResultTrap=ResultTrap,ResultMin=ResultMin,ResultRom=ResultRom,OrderOfError=OrderOfError)
            else:
                function=request.form['func']
                x1=float(request.form['x1'])
                x2=float(request.form['x2'])
                N=int(request.form['n1'])
                y1=float(request.form['y1'])
                y2=float(request.form['y2'])
                N2=int(request.form['n2'])
                z1=float(request.form['z1'])
                z2=float(request.form['z2'])
                N3=int(request.form['n3'])
                Result="too complex"
                exact=Exact(function,x1,x2,y1,y2,z1,z2,3)
                ResultTrap=Trapezoidal_Triple_Integ(function,x1,x2,N,y1,y2,N2,z1,z2,N3)
                ResultMin=triple_mixed_rule (function,x1,x2,N,y1,y2,N2,z1,z2,N3)
                OrderOfError=int(request.form['OrderOfError'])
                if(OrderOfError%2==0):
                    ResultRom=RombergRule(function, int(NumOfVar),x1,x2,y1,y2,z1,z2,OrderOfError)
                    print(ResultRom)
                    ResultRom=ResultRom[0]
                else:
                    ResultRom="Order of Error must be even"

                return render_template('Integration.html', title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",Dim = NumOfVar,function=function,x1=x1,x2=x2,n1=N,Result=Result,exact=exact,ResultTrap=ResultTrap,y1=y1,y2=y2,n2=N2,z1=z1,z2=z2,n3=N3,ResultMin=ResultMin,ResultRom=ResultRom,OrderOfError=OrderOfError)

    else:
        return render_template('Integration.html', title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg")

@app.route("/ODERK", methods=['GET', 'POST'])
def ODERK():
    if request.method == 'POST':
        equation = ''
        x0 = ''
        fx0 = ''
        h = ''
        xn = ''
        equation = request.form['equation']
        if equation:
            equation = request.form['equation']
        x0 = request.form['x0']
        if x0:
            x0 = float(request.form['x0'])
        fx0 = request.form['fx0']
        if fx0:
            fx0 = float(request.form['fx0'])
        h = request.form['h']
        if h:
            h = float(request.form['h'])
        xn = request.form['xn']
        if xn:
            xn = float(request.form['xn'])

        result = rungeKutta(x0, fx0, xn, h, equation)

        return render_template('ODERK.html', title='ODE Runge-Kutta', css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg", results=result, length=len(result))

    else:
        return render_template('ODERK.html', title='ODE Runge-Kutta', css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg")

@app.route("/ODEPC", methods=['GET', 'POST'])
def ODEPC():
    if request.method == 'POST':
        #Variables decleration 
        Is_OK=True
   

        try:
            x = []
            y = []
            Number_Of_Corrections=''
            Stopping_Criteria=''
            Method=''
            x_requested=''
            Equation=''
            #results=[]
            Number_Of_Points=0

            Method = request.form['Method']
            Equation = request.form['Equation']

            for i in range(4):
                x_index = 'x'+str(i)
                y_index ='y'+str(i)

                x_i=''
                y_i=''

                x_i = request.form[x_index]
                y_i = request.form[y_index]
            

                if x_i and y_i:
                    x.append(float(x_i))
                    y.append(float(y_i))
            
            
            Number_Of_Points = len(x) #Getting the number of points from the length of the list
            Number_Of_Corrections=int(request.form['Num_Of_Corrections']) 
            Stopping_Criteria=int(request.form['Stopping_Criteria'])
            x_requested=float(request.form['xn'])
        
        except: 
            Is_OK=False



        if Method=="AdamBackward": 
            if Is_OK==True:

                if len(x)!=0 and Equation and Number_Of_Corrections and Stopping_Criteria and x_requested:
                  
                    results=ode_adams_backward_difference(Equation,Number_Of_Corrections,Stopping_Criteria,Number_Of_Points,x,y,x_requested)
                    return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",results=results,Method=Method,OK=Is_OK)
                else:    
                    return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=False)

            else :
  
                return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)

        elif Method=="MilneMethod":
            if Is_OK==True:
                if len(x)!=0 and Equation and Number_Of_Corrections and Stopping_Criteria and x_requested:
                    y_requested=float(request.form['yn'])
                    yp, YC, relative_error=milne(Equation,5,x,y,x_requested,Number_Of_Corrections,Stopping_Criteria,y_requested)
                    results=np.array([yp,YC,relative_error])
                    return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",yp=yp,YC=YC,Error=relative_error,Method=Method,OK=Is_OK)
            else :
                return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)
        else :
            return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)


    else:
        return render_template('ODEPC.html', title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg")

@app.route("/PDE", methods=['GET', 'POST'])
def PDE():
    if request.method == 'POST':
        Choice="Regular"
        Choice=request.form['Method']
        U=''
        if Choice == "Irregular":
            #Taking the equation parameters
            h=k=0
            dxx=dyy=dx=dy=u_coeff=function=''
            dxx=request.form['dxx']
            dyy=request.form['dyy']
            dx=request.form['dx']
            dy=request.form['dy']
            u_coeff=request.form['U_Coeff']
            function=request.form['Function']
            h=float(request.form['h_step'])
            k=float(request.form['k_step'])
            boundaries=[]
            for i in range(12):
             #Strings for table records :

                f_str='function'+str(i)
                x_i_str='xi'+str(i)
                x_f_str='xf'+str(i)
                y_i_str='yi'+str(i)
                y_f_str='yf'+str(i)
                u_str='u'+str(i)
                #Parameters
                f=request.form[f_str]
                x_i=request.form[x_i_str]
                x_f=request.form[x_f_str]
                y_i=request.form[y_i_str]
                y_f=request.form[y_f_str]
                u=request.form[u_str]

                #Check that the table record is not empty

                if not f=="" and not x_i=="" and not x_f=="" and not y_i=="" and not y_f=="" and not u=="":
                    x_i=float(request.form[x_i_str])
                    x_f=float(request.form[x_f_str])
                    y_i=float(request.form[y_i_str])
                    y_f=float(request.form[y_f_str])
                    bound=boundry(y_i,y_f,x_i,x_f,f,u)
                    boundaries.append(bound)
            if dxx and dyy and dx and dy and u_coeff and function :
                grid=Grid(boundaries,h,k)
                points=grid.get_points(grid.get_boundry_rows_points(),grid.get_boundry_cols_points())
                pde=PDE_Solver(points,grid)
                pde.Get_Parameters(dxx,dyy,dx,dy,u_coeff,function)
                x_point=float(request.form['x_cordinates'])
                y_point=float(request.form['y_cordinates'])
                _point=point(x_point,y_point,False)
                grid.Plot_Region()
                U_Value=pde.Solve_At_Point(_point)
                U=U_Value
            else :
                U="There is empty inputs"
            return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg",U=U,Choice=Choice)

        else :
            h=k=0
            dxx=dyy=dx=dy=dxy=u_coeff=0
            function=''
            dxx=float(request.form['dxx'])
            dyy=float(request.form['dyy'])
            dx=float(request.form['dx'])
            dy=float(request.form['dy'])
            dxy=float(request.form['dxy'])
            u_coeff=float(request.form['U_Coeff'])
            function=request.form['Function']
            h=float(request.form['h_step'])
            k=float(request.form['k_step'])
            xi_list=[]
            xf_list=[]
            yi_list=[]
            yf_list=[]
            value_list=[]
            function_list=[]
            boundry_counter=0
            U=''
            yy=0
            Rows=0
            Value=0
            for i in range(4) :
                f_str='function'+str(i)
                x_i_str='xi'+str(i)
                x_f_str='xf'+str(i)
                y_i_str='yi'+str(i)
                y_f_str='yf'+str(i)
                u_str='u'+str(i)
                #Parameters
                f=request.form[f_str]
                x_i=request.form[x_i_str]
                x_f=request.form[x_f_str]
                y_i=request.form[y_i_str]
                y_f=request.form[y_f_str]
                u=request.form[u_str]
                if not f=="" and not x_i=="" and not x_f=="" and not y_i=="" and not y_f=="" and not u=="":
                    x_i=float(request.form[x_i_str])
                    x_f=float(request.form[x_f_str])
                    y_i=float(request.form[y_i_str])
                    y_f=float(request.form[y_f_str])
                    xi_list.append(x_i)
                    xf_list.append(x_f)
                    yi_list.append(y_i)
                    yf_list.append(y_f)
                    function_list.append(f)
                    value_list.append(u)
                    boundry_counter=boundry_counter+1

                elif f=="" and x_i=="" and x_f=="" and not y_i=="" and not y_f=="" and not u=="": #Open Boundary Condition
                    yy=int(y_i)
                    Rows=int(y_f)
                    Value=int(u)

                #Getting the boundaries and their values from the previous loop then find The x_range and y_range
            x1=min(xi_list)
            x2=max(xf_list)
            y1=min(yi_list)
            y2=max(yf_list)


                #If There is 4 Boundries --> Closed Region
            if boundry_counter==4:
                UList=Closed_Region(value_list[0],value_list[1],value_list[2],value_list[3],h,k,x1,x2,y1,y2,dxx,dyy,dx,dy,u_coeff,dxy,function)
                x_point=float(request.form['x_cordinates'])
                y_point=float(request.form['y_cordinates'])
                x_index=(x_point-x1)/h
                y_index=(y_point-y1)/k
                U=UList[x_index][y_index]
                return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg",U=U)

            elif boundry_counter==3: #Indication to open boundries --->
                x_point=float(request.form['x_cordinates'])
                y_point=float(request.form['y_cordinates'])
                x_index=(x_point-x1)/h
                y_index=(y_point-y1)/k
                Number_Of_Rows=y_index+1

                UList=Open_Region(value_list[0],value_list[1],value_list[2],h,k,x1,x2,y1,dxx,dyy,dx,dy,u_coeff,dxy,function,Value,yy,Number_Of_Rows)
                U=UList[x_index][y_index]
                return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg",U=U)



        return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg",U=U)
    else:
        return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg")

@app.route("/LinearSystem", methods=['GET', 'POST'])
def LinearSystem():
    Length = 0
    temp_to_test = 0
    inputs = []
    result = []
    n = 0
    choice = 0
    iterations = 0
    StoppingCriteria = 0.0
    w = 1

    if request.method == 'POST':

        temp_to_test = request.form['Stopping Criteria']
        if not temp_to_test == '':
            StoppingCriteria = float(request.form['Stopping Criteria'])
            choice = 2

        temp_to_test = request.form['Number of iterations']
        if not temp_to_test == '':
            iterations = int(request.form['Number of iterations'])
            choice=1

        temp_to_test = request.form['w']
        if not temp_to_test == '':
            w = float(request.form['w'])

        if 'Dim' in request.form:
            n = int(request.form['Dim']) # size = n*(n+1), inputs[size-1]
            if n >1 :
                for i in range (n):
                    for j in range (n+1):
                        if j != n:
                            temp= 'x'+str(i)+str(j)
                        elif j==n:
                            temp = 'c' + str(i)
                        temp_to_test = request.form[temp]
                        if not temp_to_test == '':
                              inputs.append(request.form[temp])
##########################################################################
        if (n*(n+1)==len(inputs)) and (StoppingCriteria or iterations) and w and choice:
            result = solve_linear_systems(n,inputs,w,choice,iterations,StoppingCriteria)
            Length = len(result[0])
            if Length:
                 return render_template('LinearSystem.html', title='Linear Systems', css="LinearSystem.css", wing="SE - copy2.png", logo="Logo Greeny.svg" , Eqs_No=n, results=result)
        return redirect(url_for('LinearSystem'))

    else:
        return render_template('LinearSystem.html', title='Linear Systems', css="LinearSystem.css", wing="SE - copy2.png", logo="Logo Greeny.svg")

@app.route("/NonlinearSystem", methods=['GET', 'POST'])
def NonlinearSystem():
    if request.method == 'POST':
        Method = ''
        Eqs_No = iterations = f_xy = g_xy =X0 = Y0 = 0
        StoppingCriteria = 0.0
        Length = 0
        result = []

        if 'Method' in request.form:
            Method  = request.form['Method']
        if 'Dim' in request.form:
            Eqs_No = int(request.form['Dim'])
            if Eqs_No == 2:
                f_xy = request.form['Feq']
                g_xy = request.form['Geq']
                X0 = request.form['X0']
                if not X0 == '':
                    X0 = float(request.form['X0'])
                Y0 = request.form['Y0']
                if not Y0 == '':
                    Y0 = float(request.form['Y0'])
            elif Eqs_No == 3:
                f_xy = request.form['Feq']
                g_xy = request.form['Geq']
                h_xy = request.form['Heq']
                X0 = request.form['X0']
                if not X0 == '':
                    X0 = float(request.form['X0'])
                Y0 = request.form['Y0']
                if not Y0 == '':
                    Y0 = float(request.form['Y0'])
                Z0 = request.form['Z0']
                if not Z0 == '':
                    Z0 = float(request.form['Z0'])

        StoppingCriteria = request.form['StoppingCriteria']
        if not StoppingCriteria == '':
            StoppingCriteria = float(request.form['StoppingCriteria'])
        iterations = request.form['Iterations']
        if not iterations == '':
            iterations = int(request.form['Iterations'])

        if Method and Eqs_No and not StoppingCriteria == '' and iterations and f_xy and g_xy and X0 and Y0:
            if Method == "NewtonRaphson":
                if Eqs_No == 2:
                    result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, 0, X0, Y0, 0, StoppingCriteria)
                    Length = len(result[1])
                    print(result, Length)
                elif Eqs_No == 3 and Z0 and h_xy:
                    result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, h_xy, X0, Y0, Z0, StoppingCriteria)
                    Length = len(result[1])
            elif Method == "FixedPoint":
                if Eqs_No == 2:
                    result = FixedPointIteration(str(Eqs_No), str(iterations), str(StoppingCriteria), f_xy, g_xy, X0, Y0)
                    Length = len(result[1])
                elif Eqs_No == 3 and h_xy and Z0:
                    result = FixedPointIteration(str(Eqs_No), str(iterations), str(StoppingCriteria), f_xy, g_xy, X0, Y0, h_xy, Z0)
                    Length = len(result[1])
            if Length:
                return render_template('NonlinearSystem.html', title='Nonlinear Systems', css="NonlinearSystems.css", wing="SE - copy2.png", logo="Logo Greeny.svg", Length=Length, Method=Method, iterations=iterations, Eqs_No=Eqs_No, results=result)
        return redirect(url_for('NonlinearSystem'))
    else:
        return render_template('NonlinearSystem.html', title='Nonlinear Systems', css="NonlinearSystems.css", wing="SE - copy2.png", logo="Logo Greeny.svg")

@app.route("/EigenvalueProblem", methods=['GET', 'POST'])
def EigenvalueProblem():
    Length = 0
    temp_to_test = 0

    size = 0
    list_of_entires = []
    list_init_vector = []

    iter_or_stoppingC = 0
    num_iteration = 0
    StoppingCriteria = 0

    Method = ''  # Choice

    result = []

    if request.method == 'POST':

        if 'Method' in request.form:
            temp_to_test = request.form['Method']
            if temp_to_test == 'Power':
                Method = 1
            elif temp_to_test == 'Inv.Power':
                Method = 2
            elif temp_to_test == 'Power-with-defelation':
                Method = 3

        temp_to_test = request.form['Stopping Criteria']
        if not temp_to_test == '':
            StoppingCriteria = float(request.form['Stopping Criteria'])
            iter_or_stoppingC = 2

        temp_to_test = request.form['Number of iterations']
        if not temp_to_test == '':
            num_iteration = int(request.form['Number of iterations'])
            iter_or_stoppingC = 1

        if 'Dim' in request.form:
            size = int(request.form['Dim'])
            if size > 1:
                for i in range(size):
                    for j in range(size + 1):
                        if j != size:
                            temp = 'x' + str(i) + str(j)
                            temp_to_test = request.form[temp]
                            if not temp_to_test == '':
                                list_of_entires.append(request.form[temp])
                        elif j == size:
                            temp = 'v' + str(i)
                            temp_to_test = request.form[temp]
                            if not temp_to_test == '':
                                list_init_vector.append(request.form[temp])

        if size and (size * size == len(list_of_entires)) and (1 * size == len(list_init_vector)) and iter_or_stoppingC and (StoppingCriteria or num_iteration) and Method:
            result = solve_Eigenvalue(size, list_of_entires, list_init_vector, Method, iter_or_stoppingC, num_iteration,
                                      StoppingCriteria)

            # result[0] List_Eig_values-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[1] List_Eig_vectors-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[2] List_relative_error-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[3] Eig_value ->if method == 1 or 2 : carries the value to be displayed
            # result[4] Eig_vector ->if method == 1 or 2 : carries the value to be displayed
            # result[5] True_error ->if method == 1 or 2 : carries the value to be displayed
            # result[6] test -> if false then there was an error in the calculations of the power method
            Length = len(result[0])
            if Length:
                return render_template('EigenvalueProblem.html', title='Eigenvalue Problem',
                                       css="EigenvalueProblem.css", wing="SE - copy2.png", logo="Logo Greeny.svg",
                                       Length=size, Method=Method, iterations=Length, results=result)
        return redirect(url_for('EigenvalueProblem'))
    else:
        return render_template('EigenvalueProblem.html', title='Eigenvalue Problem', css="EigenvalueProblem.css",
                               wing="SE - copy2.png", logo="Logo Greeny.svg")


if __name__ == '__main__':
    app.run(debug=True)
