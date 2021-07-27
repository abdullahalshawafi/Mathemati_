from flask import Flask, render_template, url_for, request, redirect, jsonify
from methods.PolynomialInterpolation import Newton, LaGrange
from methods.Bezier import bezier_curve_bin
from methods.SplineInterpolation import linear_spline, quad_spline,cubic_spline, get_interval_list
from methods.Regression import Nonlinear_Regression, TrueError, Curve_Family_Detective, Linearized_Regression, Surface_Fit_Beta, PointsFor3DSF, zEvalList, SurfaceInt
from methods.Differentiation import  TableDeriv, FuncDeriv
from methods.NewtonCotes import Trapezoidal_Integ, Trapezoidal_error, Trapezoidal_Double_Integ, single_mixe_rule, double_mixed_rule, triple_mixed_rule, Trapezoidal_Triple_Integ
from methods.Romberg import RombergRule
from methods.Gauss_Quadrature import myfun, Exact
from methods.ODE_Kutta import rungeKutta,TrueDifferentials,TrueErrorr
from methods.ODE_Adams import ode_adams_backward_difference
from methods.ODE_milne import milne
from methods.RegularPDE import Open_Region, Closed_Region
from methods.PDE_Solve import Grid, PDE_Solver, boundry , point
from methods.LinearSystems import solve_linear_systems
from methods.NewtonRaphson import Newton_Raphson
from methods.FixedPoint import FixedPointIteration
from methods.Eigenvalue import solve_Eigenvalue
from methods.ODE_EulerAndHeun  import func_xyzt,Solve_Euler ,Solve_Heun
from methods.BilinearInterpolation import Surface_Interpolation
from methods.LeastAbsoluteErrors import LeastAbsoluteDeviations, LeastSquares,CorrelationCoefficients, Numpify, Angulus, ZeroDerivativeCheck
from methods.LogCosh import minLogCoshLoss, RegressionErrors
import numpy as np

app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'edcb30ed4a6a5b467a2ed529ed889dbf'

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')

@app.route("/home-dynamic")
def homeDynamic():
    return render_template('home-dynamic.html')

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
        error = ''
        Degree = -1

        NumPoints = 0
        X_Points = []
        Y_Points = []

        if 'Method' in request.form:
            Method = request.form['Method']


        if Method=="Newton" and (request.form['Degree']) :
            try:
                Degree = int(request.form['Degree'])
            except:
                pass

        for i in range(20):
            if request.form["X_" + str(i)] and request.form["Y_" + str(i)]:
                try:
                    x_temp = float(request.form["X_" + str(i)])

                    if not(x_temp in X_Points):
                        X_Points.append(float(request.form["X_" + str(i)]))
                        Y_Points.append(float(request.form["Y_" + str(i)]))

                except:
                    pass


        NumPoints = len(X_Points)
        PolynomialDerivativeFunction = ''
        ResidualError = ''
        PolynomialFunction = ''
        ParametricX = ''
        ParametricY = ''
        X_val = 0

        if not(Method):
            error = 'Chose a Method'
            PolynomialFunction = 'Chose a Method'

        elif Degree < 0 and Method =='Newton':
            error = 'Invalid Degree'
            PolynomialFunction = 'Invalid Degree'

        elif Method=='Lagrange' and NumPoints > 0 :
            Y_val, PolynomialFunction = LaGrange(X_Points, Y_Points, NumPoints, X_val)
            ParametricX, ParametricY = bezier_curve_bin(NumPoints, X_Points, Y_Points)

        elif Method=='Newton' and NumPoints > Degree:
            X_diff_val = 0
            DT, Y_val, PolynomialFunction, Y_diff_val, PolynomialDerivativeFunction, ResidualError = Newton(X_Points, Y_Points, NumPoints, X_val, Degree)
            ParametricX ,ParametricY = bezier_curve_bin(NumPoints,X_Points,Y_Points)

        else:
            error = 'Missing Points'

        return render_template('PolynomialInterpolation.html', url="vdBtRSCF_kA", title='Polynomial Interpolation',
                                css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg", Method = Method,
                                PolynomialFunction = PolynomialFunction , PolynomialDerivativeFunction= PolynomialDerivativeFunction,
                                 ResidualError = ResidualError, ParametricX=ParametricX,ParametricY=ParametricY, error = error)

    else:

        return render_template('PolynomialInterpolation.html', url="vdBtRSCF_kA", title='Polynomial Interpolation', css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg", PolynomialFunction = PolynomialFunction)

@app.route("/SplineInterpolation", methods=['GET', 'POST'])
def SplineInterpolation():
    if request.method == 'POST':
        Numbers =[]
        NumPoints = 0

        while (request.form['x_coordinates'+str(NumPoints)]) and (request.form['y_coordinates'+str(NumPoints)]):
            try:
                Numbers.append([float((request.form['x_coordinates'+str(NumPoints)])),float((request.form['y_coordinates'+str(NumPoints)]))])
                NumPoints +=1
            except:
                pass

        if NumPoints > 1:
            LinearSpline = linear_spline(NumPoints,Numbers)
            IntervalList = get_interval_list(NumPoints,Numbers)
            QuadraticSpline = quad_spline(NumPoints,Numbers)
            CubicSpline = cubic_spline(NumPoints,Numbers)
            return render_template('SplineInterpolation.html', title='Spline Interpolation', css="SplineInterpolation.css",
                                    wing="CF Header.png", logo="Logo.svg",NumPoints = NumPoints-1,
                                    IntervalList = IntervalList, LinearSpline = LinearSpline,
                                    QuadraticSpline = QuadraticSpline, CubicSpline = CubicSpline)
        else:
            return render_template('SplineInterpolation.html', title='Spline Interpolation',
                                   css="SplineInterpolation.css", wing="CF Header.png", logo="Logo.svg",
                                    eq="",error = 'Missing Points')
    else:
        return render_template('SplineInterpolation.html', title='Spline Interpolation', css="SplineInterpolation.css", wing="CF Header.png", logo="Logo.svg" , eq="")

@app.route("/BilinearInterpolation", methods=['GET', 'POST'])
def BilinearInterpolation():
    if request.method == 'POST':
        points = []
        Z = []
        plane=''
        _Z=''
        x_val1=request.form['xinput']
        y_val1=request.form['yinput']
        x_val=0
        y_val=0
        if x_val1 and y_val1:
            try:
                x_val=float(x_val1)
                y_val=float(y_val1)
            except:
                pass

        for i in range(25):
            x = request.form['x' + str(i)]
            y = request.form['y' + str(i)]
            z = request.form['z' + str(i)]

            if x and y and z:
                try:

                    points.append([float(x), float(y)])
                    Z.append(float(z))
                except:
                    pass



        try:
            np_points=np.array(points)
            np_Z=np.array(Z)
            surface = Surface_Interpolation(np_points,np_Z )
            plane=surface.GetPlane_of_P(x_val,y_val)


            Surf, GriX, GriY, GriZ = surface.BiLinearInt()
            GriZ = GriZ.transpose()
            x1 = list(GriX)
            y1 = list(GriY)
            z1 = []


            _Z=-1*plane[3]-x_val*plane[0]-y_val*plane[1]
            plane = list(plane)
            plane.append(0)
            plane.append(0)

            if plane[2]:

                _Z = np.round(_Z/plane[2],5)
                plane[4] = np.round(-1*plane[0]/plane[2],5)
                plane[5] = np.round(-1*plane[1]/plane[2],5)

            plane = np.round(plane, 5)

            for i in range(np.shape(GriZ)[0]):
                z1.append(list(GriZ[i]))
        except:
            return render_template('BI.html', title='Bilinear Interpolation', css="BI.css", wing="CF Header.png", logo="Logo.svg" , eq="",plane=[1,1,1,1],_Z="")

        return render_template('BI.html', title='Bilinear Interpolation', css="BI.css", wing="CF Header.png", logo="Logo.svg", eq="",x1 = x1, y1 = y1, z1 = z1,function=surface.GetPlane_of_P,plane=plane,Z=_Z)

    else:
        return render_template('BI.html', title='Bilinear Interpolation', css="BI.css", wing="CF Header.png", logo="Logo.svg" , eq="",plane=[1,1,1,1],_Z="",z="")

@app.route("/LeastSquareReg", methods=['GET', 'POST'])
def LeastSquareReg():
    if request.method == 'POST':
        Method = ''
        error = ''
        if 'Method' in request.form:
            Method  = request.form['Method']
        if Method == 'Nonlinear':
            Equation = request.form['Nonlinear_Equation']
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                try:
                    xdata.append(float(request.form['x_coordinates' + str(i)]))
                    ydata.append(float(request.form['y_coordinates' + str(i)]))
                except:
                    pass
                i += 1
            if len(xdata)>=3:
                try:
                    result, Error = Nonlinear_Regression(xdata, ydata, Equation, 12)
                    TrueErr = TrueError(ydata, 12)
                    r = round((abs(Error-TrueErr)/TrueErr)**0.5,12)
                except:
                    error = "Invalid Inputs"
                    result = "Invalid Inputs"
                    Error = '...'
                    TrueErr = '...'
                    r = '...'

            elif len(xdata) == 0:
                error = 'Missing Points'
                result = "Missing Points"
                Error = '...'
                TrueErr = '...'
                r = '...'

            else:
                error = "The data set is too small"
                result = "The data set is too small"
                Error = '...'
                TrueErr = '...'
                r = '...'

            return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method, results=result, Error=Error, TrueErr=TrueErr, r=r, error = error)

        elif Method == 'Linearized':
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                try:
                    xdata.append(float(request.form['x_coordinates' + str(i)]))
                    ydata.append(float(request.form['y_coordinates' + str(i)]))
                except:
                    pass
                i += 1

            j = 0
            Fdata = [request.form['Abdullah_Knows_It_All']]
            while request.form['term' + str(j)]:
                Fdata.append(request.form['term' + str(j)])
                j += 1

            try:
                LHS, RHS, Constants, Sr = Linearized_Regression(xdata, ydata, Fdata, 12)
            except:
                error = "Invalid Inputs"
                result = "Invalid Inputs"
                Error = '...'
                TrueErr = '...'
                r = '...'
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results=result, Error=Error, TrueErr=TrueErr, r=r, error = error)

            if  ydata and xdata and LHS !="" :
                TrueErr = TrueError(ydata, 4)
                r = round((abs(Sr-TrueErr)/TrueErr)**0.5,12)
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results=RHS, Error=Sr, TrueErr=TrueErr, r=r)
            elif not ydata or not xdata:
                error = 'Missing Points'
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results='Missing Points', Error='...', TrueErr='...', r='...', error = error)
            elif xdata and ydata:
                error = 'Singular/Out of Domain Matrix'
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results='Singular/Out of Domain Matrix', Error='...', TrueErr='...', r='...', error=error)

        elif Method == 'Best-Fitting-Family-of-Curves':
            i = 0
            xdata = []
            ydata = []
            while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
                try:
                    xdata.append(float(request.form['x_coordinates' + str(i)]))
                    ydata.append(float(request.form['y_coordinates' + str(i)]))
                except:
                    pass
                i += 1
            try:
                result, Family, Error, STnd = Curve_Family_Detective(xdata, ydata, 12)
                TrueErr = TrueError(ydata, 12)
                r = round((abs(Error-TrueErr)/TrueErr)**0.5,12)
            except:
                error = "Missing Points"
                result = "Missing Points"
                Error = '...'
                TrueErr = '...'
                r = '...'
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results=result, Error=Error, TrueErr=TrueErr, r=r, error = error)

            if result !="" and Error !="" :
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results=result, Error=Error, TrueErr=TrueErr, r=r, family=Family + ' curves')
            elif not xdata or not ydata:
                error = 'Missing Points'
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results='Missing Points', Error='...', TrueErr='...', r='...', family= ' ...',error = error)
            elif xdata and ydata:
                return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                        css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg", Method=Method,
                                        results='Singular Matrix/ Out of Domain Matrix', Error='...', TrueErr='...',
                                        r='...', family= ' ...', error = error)

        else:
            error = 'Chose a Method'
            return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                    css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg",
                                    Method=Method, error = error)
    else:
        error = 'Singular/Out of Domain Matrix'
        return render_template('LeastSquareReg.html', url="gr-a8q7EDbY", title='Least Square Reg.',
                                css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/SurfaceFitting", methods=['GET', 'POST'])
def SurfaceFitting():
    if request.method == 'POST':
        Sr = 0
        LHS = 0
        i = 0
        xdata = []
        ydata = []
        zdata = []
        RHS = 0

        while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!='' and request.form['z_coordinates' + str(i)]!=''):
            try:
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
                zdata.append(float(request.form['z_coordinates' + str(i)]))
            except:
                pass
            i += 1

        j = 0
        Fdata = [request.form['Abdullah_Knows_It_All']]
        while request.form['term' + str(j)]:
            Fdata.append(request.form['term' + str(j)])
            j += 1

        if xdata and Fdata:
            try:
                LHS, RHS, Constants, Sr = Surface_Fit_Beta(xdata, ydata, zdata, Fdata, 10)
            except:
                return render_template('SurfaceFitting.html', url="mRjVy0MSUI0",
                                        title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png",
                                        logo="Logo.svg", error = 'Invalid Input', results='Invalid Input', Error='...')

        if RHS:
            GriX, GriY, GriZ = PointsFor3DSF(xdata,ydata,RHS)
            GriZ = GriZ.transpose()
            x1 = list(GriX)
            y1 = list(GriY)
            z1 = []

            for i in range(np.shape(GriZ)[0]):
                z1.append(list(GriZ[i]))




        if LHS and RHS and not Sr == '':
            return render_template('SurfaceFitting.html', url="mRjVy0MSUI0",
                                    title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png",
                                    logo="Logo.svg", results=RHS, Error=Sr, x1 = x1, y1 = y1, z1 = z1)
        elif not xdata:
            return render_template('SurfaceFitting.html', url="mRjVy0MSUI0",
                                    title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png",
                                    logo="Logo.svg", error = 'Missing Points', results='Missing Points', Error='...')
        else:
            return render_template('SurfaceFitting.html', url="mRjVy0MSUI0",
                                    title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png",
                                    logo="Logo.svg", results='Singular Matrix/Out of Domain', Error='...', error = 'Singular Matrix/Out of Domain')
    else:
        return render_template('SurfaceFitting.html', url="mRjVy0MSUI0", title='Surface Fitting',
                                css="SurfaceFitting.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/Differentiation", methods=['GET', 'POST'])
def Differentiation():
    if request.method == 'POST':
        results=''
        error=''
        try:
            Method = ''
            Method = request.form['Method']
            Calculation_Point = 0
            Calculation_Point = float(request.form['Calculation Point'])
        except:
            error="Invalid Calculation Point"
        if Method == 'Table' :
            x = []
            y = []
            i = 0
            while (request.form['x' + str(i)]!='' and request.form['y' + str(i)]!=''):
                try:
                    x.append(float(request.form['x' + str(i)]))
                    y.append(float(request.form['y' + str(i)]))
                    i += 1
                except:
                    pass
            try:
                results = TableDeriv(Calculation_Point, x, y)
            except:
                error="Invalid Input"
        else:
            try:
                Function = ''
                Function = request.form['Function']
                results = []
                h = 0
                order = 0
                h = float(request.form['step'])
                order = float(request.form['order'])
                results = FuncDeriv(Function, h, order, Calculation_Point)
                import sympy
                from sympy import symbols
                x = symbols('x');
                F=sympy.sympify(Function )  
                y=sympy.lambdify([x],F)
                Tango=str(results[0])+"*x"+"+"+str(y(Calculation_Point)-results[0]*Calculation_Point)
            except:
                error="Invalid Input"

        return render_template('Differentiation.html', url='KPnkAIZqWFQ', title='Differentiation', css="Differentiation.css", wing="SE - Copy.png", logo="Logo Crimson.svg" ,error=error, results = results , Method = Method,Tango=Tango)

            #return render_template('Differentiation.html', url='KPnkAIZqWFQ', title='Differentiation', css="Differentiation.css", wing="SE - Copy.png", logo="Logo Crimson.svg" )

    else:
        return render_template('Differentiation.html', url='KPnkAIZqWFQ', title='Differentiation', css="Differentiation.css", wing="SE - Copy.png", logo="Logo Crimson.svg" )

@app.route("/Integration", methods=['GET', 'POST'])
def Integration():
    if request.method == 'POST':
        Dim=''
        function=''
        x1=''
        x2=''
        y1=''
        y2=''
        N2=''
        N=''
        Result=''
        ResultTrap=''
        error=''
        _error=''
        TrapError=''
        exact=''
        ResultMin=''
        ErrorMin=''
        ResultRom=''
        OrderOfError=''

        if 'Dim' in request.form:
            NumOfVar=request.form['Dim']
            if NumOfVar == '1':
                function=request.form['func']
                function=function.replace("^","**")
                function=function.replace("PI","pi")
                try:
                    x1=float(request.form['x1'])
                    x2=float(request.form['x2'])
                except:
                    if _error=='':
                        _error="Invalid x1 , or x2"
                try:
                    N=int(request.form['n1'])
                except:
                    if _error=='':
                        _error="Invalid N"
                try:
                    OrderOfError=int(request.form['OrderOfError'])
                except:
                    ResultRom="Order of Error is invalid"

                try:
                    if function != '' and x1 != '' and x2 != '' and N != '' and N > 6:
                        Result,error=myfun(function,x1,x2,1,1,6)
                except:
                    pass
                else:
                    try:
                        Result,error=myfun(function,x1,x2,1,1,N)
                    except:
                        if _error=='':
                            _error="Invalid Inputs"
                try:
                    if function != '' and x1 != '' and x2 != '':
                        exact=Exact(function,x1,x2,1,1,1,1,1)
                        if OrderOfError != '':
                            if OrderOfError%2==0:
                                ResultRom=RombergRule(function, int(NumOfVar),x1,x2,1,1,1,1,OrderOfError)
                            else:
                                ResultRom="Order of Error must be even"
                    if function != '' and x1 != '' and x2 != '' and N != '':
                        ResultTrap=Trapezoidal_Integ(function,x1,x2,N)
                        ResultMin,ErrorMin=single_mixe_rule(function,x1,x2,N)
                        TrapError=Trapezoidal_error(function,x1,x2,N)
                except:
                    if _error=='':
                        _error="Invalid Inputs"

                return render_template('Integration.html', url="EgQa0aKmUyk" , title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",Dim = NumOfVar,function=function,x1=x1,x2=x2,n1=N,Result=Result,exact=exact,_error=_error,error=error,ResultTrap=ResultTrap,TrapError=TrapError,ResultMin=ResultMin,ErrorMin=ErrorMin,ResultRom=ResultRom,OrderOfError=OrderOfError)



            elif NumOfVar == '2':
                try:
                    function=request.form['func']
                except:
                    if _error=='':
                        _error="Invalid Function"
                try:
                    x1=float(request.form['x1'])
                except:
                    if _error=='':
                        _error="Invalid x1"
                try:
                    x2=float(request.form['x2'])
                except:
                    if _error=='':
                        _error="Invalid x2"
                try:
                    N=int(request.form['n1'])
                except:
                    if _error=='':
                        _error="Invalid N"
                try:
                    y1=float(request.form['y1'])
                except:
                    if _error=='':
                        _error="Invalid y1"
                try:
                    y2=float(request.form['y2'])
                except:
                    if _error=='':
                        _error="Invalid y2"
                try:
                    N2=int(request.form['n2'])
                except:
                    if _error=='':
                        _error="Invalid N2"
                try:
                    OrderOfError=int(request.form['OrderOfError'])
                except:
                     ResultRom="Order of Error is invalid"

                try:
                    if N > 6:
                        Result,error=myfun(function,x1,x2,y1,y2,6)
                except:
                    pass
                else:
                    try:
                        Result,error=myfun(function,x1,x2,y1,y2,N)
                    except:
                        if _error=='':
                            _error="Invalid Input"
                try:
                    if function != '' and x1 != '' and x2 != '':
                        exact=Exact(function,x1,x2,y1,y2,1,1,2)
                        if OrderOfError != '':
                            if OrderOfError%2==0:
                                ResultRom=RombergRule(function, int(NumOfVar),x1,x2,y1,y2,1,1,OrderOfError)
                            else:
                                ResultRom="Order of Error must be even"
                    if function != '' and x1 != '' and x2 != '' and N != '':
                        ResultMin=double_mixed_rule (function,x1,x2,N,y1,y2,N2)
                        ResultTrap=Trapezoidal_Double_Integ(function,x1,x2,N,y1,y2,N2)
                except:
                    if _error=='':
                        _error="Invalid Input"

                return render_template('Integration.html', url="EgQa0aKmUyk" , title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",Dim = NumOfVar,function=function,x1=x1,x2=x2,y1=y1,y2=y2,n2=N2,n1=N,Result=Result,exact=exact,error=error,ResultTrap=ResultTrap,ResultMin=ResultMin,ResultRom=ResultRom,OrderOfError=OrderOfError,_error=_error)

            else:
                z1=''
                z2=''
                N3=''
                try:
                    function=request.form['func']
                except:
                    if _error=='':
                        _error="Invalid function"
                try:
                    x1=float(request.form['x1'])
                except:
                    if _error=='':
                        _error="Invalid x1"
                try:
                    x2=float(request.form['x2'])
                except:
                    if _error=='':
                        _error="Invalid x2"
                try:
                    N=int(request.form['n1'])
                except:
                    if _error=='':
                        _error="Invalid N1"
                try:
                    y1=float(request.form['y1'])
                except:
                    if _error=='':
                        _error="Invalid y1"
                try:
                    y2=float(request.form['y2'])
                except:
                    if _error=='':
                        _error="Invalid y2"
                try:
                    N2=int(request.form['n2'])
                except:
                    if _error=='':
                        _error="Invalid N2"
                try:
                    z1=float(request.form['z1'])
                except:
                    if _error=='':
                        _error="Invalid z1"
                try:
                    z2=float(request.form['z2'])
                except:
                    if _error=='':
                        _error="Invalid z2"
                try:
                    N3=int(request.form['n3'])
                except:
                    if _error=='':
                        _error="Invalid N3"
                try:
                    OrderOfError=int(request.form['OrderOfError'])
                except:
                     ResultRom="Order of Error is invalid"
                Result="too complex"
                try:
                    if function != '' and x1 != '' and x2 != '':
                        exact=Exact(function,x1,x2,y1,y2,z1,z2,3)
                        if OrderOfError != '':
                            if OrderOfError%2==0:
                                ResultRom=RombergRule(function, int(NumOfVar),x1,x2,y1,y2,z1,z2,OrderOfError)
                            else:
                                ResultRom="Order of Error must be even"
                    if function != '' and x1 != '' and x2 != '' and N != '':
                        ResultTrap=Trapezoidal_Triple_Integ(function,x1,x2,N,y1,y2,N2,z1,z2,N3)
                        ResultMin=triple_mixed_rule (function,x1,x2,N,y1,y2,N2,z1,z2,N3)
                except:
                    if _error=='':
                        _error="Invalid Inputs"

                return render_template('Integration.html', url="EgQa0aKmUyk" , title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",_error=_error,Dim = NumOfVar,function=function,x1=x1,x2=x2,n1=N,Result=Result,exact=exact,ResultTrap=ResultTrap,y1=y1,y2=y2,n2=N2,z1=z1,z2=z2,n3=N3,ResultMin=ResultMin,ResultRom=ResultRom,OrderOfError=OrderOfError)

        else:
            _error="Choose a Method"

            return render_template('Integration.html', url="EgQa0aKmUyk" , title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg",_error=_error)
    else:
        return render_template('Integration.html' , url="EgQa0aKmUyk" , title='Integration', css="Integration.css", wing="SE - Copy.png", logo="Logo Crimson.svg")

@app.route("/ODERK", methods=['GET', 'POST'])
def ODERK():
    if request.method == 'POST':
        error = ''
        x0 = ''
        fx0 = ''
        h = ''
        xn = ''
        result = ''

        equation = request.form['equation']
        if not(equation):
            return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                    css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                    error = 'Enter Equation')

        try:
            x0 = float(request.form['x0'])
        except:
            return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                    css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                    error = 'Enter X0')
        try:
            fx0 = float(request.form['fx0'])
        except:
            return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                    css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                    error = 'Enter fX0')
        try:
            h = float(request.form['h'])
        except:
            return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                    css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                    error = 'Enter h')
        try:
            xn = float(request.form['xn'])
        except:
            return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                    css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                    error = 'Enter Xn')
        try:
            result = rungeKutta(x0, fx0, xn, h, equation)
        except:
            error = 'Can not Solve at This Point'

        TrueResult = TrueDifferentials(equation,x0,fx0,xn)
        Truerror=TrueErrorr(TrueResult,result[-1])
        return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg",
                                results=result, length=len(result), Truerror=Truerror, error = error)

    else:
        return render_template('ODERK.html', url="gC-XbgLj63I", title='ODE Runge-Kutta',
                                css="ODERK.css", wing="DE - Copy.png", logo="Logo.svg")

@app.route("/ODEEH", methods=['GET', 'POST'])
def ODEEH():
    #*********
    Method =0
    O_Dim = 0
    Eqs_No = 0
    temp_to_test=0
    h_or_n=''
    iter_or_stoppingC=''
    StoppingCriteria = 0.0
    num_iteration=0
    List_initial_values=['']*7 # [0]->x0 ,[1]-> y0 ,[2]->z0 ,[3]->t0 ,[4]->y'0 ,[5]->y"0 ,[6]->x_at
    List_eqs = ['']*5 #[0]-> y',[1]->y",[2]->y"',[3]->z',[4]->t'
    y_exact=''
    Length = 0
    result = []
    #*****************************
    if request.method == 'POST':
        if 'Method' in request.form:
            temp_to_test  = request.form['Method']
            if temp_to_test=='Euler':
                Method=1
            if temp_to_test=='Heun':
                Method=2
        if 'ODim' in request.form:
            O_Dim = int(request.form['ODim'])
        if 'Dim' in request.form:
            Eqs_No = int(request.form['Dim'])

        if not request.form['Stopping Criteria']=='':
          try:
                 checker = float(request.form['Stopping Criteria'])

          except ValueError :
              if Method==2:
               return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                     wing="DE - Copy.png",
                                     logo="Logo.svg", error="Ops!.. Enter valid data for Stopping Criteria ")
              else:
               return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                             wing="DE - Copy.png",
                                             logo="Logo.svg", error="Ops!.. Enter valid data for Step Size(h) ")
          else:
            temp_to_test = request.form['Stopping Criteria']
            if Method == 2:
             StoppingCriteria = float(temp_to_test)
             num_iteration=''
             iter_or_stoppingC ='s'
            else:
             StoppingCriteria = float(temp_to_test)
             num_iteration = ''
             h_or_n = 'h'
        elif not request.form['Number of iterations']=='':
          try:
                 checker = float(request.form['Number of iterations'])

          except ValueError :
                 if Method==2:
                  return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                        wing="DE - Copy.png",
                                        logo="Logo.svg", error="Ops!..Enter valid data for Number of iterations ")
                 else:
                  return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen',
                                                css="ODEEH.css",
                                                wing="DE - Copy.png",
                                                logo="Logo.svg",
                                                error="Ops!..Enter valid data for Number of Steps (n)")
          else:
             temp_to_test = request.form['Number of iterations']

             if Method == 2:
              num_iteration=int(temp_to_test)
              StoppingCriteria=''
              iter_or_stoppingC = 'n'
             else:
              num_iteration = int(temp_to_test)
              StoppingCriteria = ''
              h_or_n = 'n'
        else:
         StoppingCriteria = ''
         num_iteration = ''
         if Method==2:
          return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                wing="DE - Copy.png",
                                logo="Logo.svg", error="You forgot entering data for Stoping Criteria OR Number of iterations -- only one of them is needed--")
         else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                    wing="DE - Copy.png",
                                    logo="Logo.svg",
                                    error="You forgot entering data for Step Size(h) OR Number of Steps(n) -- only one of them is needed--")
 #******************************

        if not request.form['Atx'] =='':
            try:
                checker = float(request.form['Atx'])
            except ValueError:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                       wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!.. Enter valid data for x to evaluate at:")
            else:
             temp_to_test = float(request.form['Atx'])
             if not temp_to_test == '':
              List_initial_values[6] = temp_to_test  # x to evaluate at =
        else:
            return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering X to evaluate at :")
        if Method==2 :
         temp_to_test = (request.form['yex'])
         if not temp_to_test == '':
             try:
                 func_xyzt(request.form['yex'],1,1,1,1)
             except NameError:
                 return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                        wing="DE - Copy.png",
                                        logo="Logo.svg", error="Ops!.. Enter valid equation for Y exact (x) ")
             else:
              y_exact = temp_to_test  # func to calc exact value of y:
    #***********
        if not request.form['x'] == '':
         try:
            checker = float(request.form['x'])
         except ValueError:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                       wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!.. Enter valid data for Xo ")
         else:
          temp_to_test = float(request.form['x'])
          List_initial_values[0] = float(temp_to_test)
        else:
            return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering Xo value:")
        if (Method==1 and (Eqs_No==1 or Eqs_No==2 or Eqs_No==3 )) or (Method==2 and O_Dim==1 and (Eqs_No==1 or Eqs_No==2)) or (Method==2 and (O_Dim==2 or O_Dim==3)):
            temp_to_test = (request.form['y'])
            if not temp_to_test == '':
                try:
                 checker = float(request.form['y'])
                except ValueError:
                  return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!.. Enter valid data for Yo")
                else:
                 List_initial_values[1] = float(temp_to_test)
            else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering Yo value:")
        if (Method==1 and (Eqs_No==2 or Eqs_No==3))or (Method==2 and O_Dim==1 and Eqs_No==2):
            temp_to_test = (request.form['z'])
            if not temp_to_test == '':
                try:
                    checker = float(request.form['z'])
                except ValueError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!.. Enter valid data for Zo")
                else:
                 List_initial_values[2] = float(temp_to_test)
            else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering Zo value:")
        if (Method==1 and Eqs_No==3):
            temp_to_test = (request.form['t'])
            if not temp_to_test == '':
                try:
                    checker = float(request.form['t'])
                except ValueError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!.. Enter valid data for to")
                else:
                 List_initial_values[3] = float(temp_to_test)
            else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering to value:")
        if (Method==2 and (O_Dim==3 or O_Dim==2)):
            temp_to_test = (request.form['ydash'])
            if not temp_to_test == '':
                try:
                    checker = float(request.form['ydash'])
                except ValueError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!.. Enter valid data for Y’o ")
                else:
                 List_initial_values[4] = float(temp_to_test)
            else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering Y’o value:")
        if (Method==2 and  O_Dim==3):
            temp_to_test = (request.form['yddash'])
            if not temp_to_test == '':
                try:
                    checker = float(request.form['yddash'])
                except ValueError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!.. Enter valid data for Y’’o ")
                else:
                 List_initial_values[5] = float(temp_to_test)
            else:
             return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",error="Ops!..You forgot entering Y’’o value:")
         #*********************************************
        if (Method == 1 and (Eqs_No == 2 or Eqs_No==1 or Eqs_No==3)) or (Method ==2 and O_Dim==1 and(Eqs_No == 1 or Eqs_No==2 )):
         if not request.form['Y1']== '':
          try:
              func_xyzt(str(request.form['Y1']),1,1,1,1)
          except NameError:
              return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                     wing="DE - Copy.png",
                                     logo="Logo.svg", error="Ops!.. Enter valid equation for Y’( )")
          else:
           List_eqs[0] = str(request.form['Y1'])
         else:
          return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png",
                               logo="Logo.svg", error="Ops!..You forgot entering Y’( ):")
        if (Method == 2 and (O_Dim == 2 )):
            temp_to_test = (request.form['Y2'])
            if not temp_to_test == '':
                try:
                    func_xyzt(str(request.form['Y2']), 1, 1, 1, 1)
                except NameError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!..Enter valid equation for Y’’( )")
                else:
                 List_eqs[1] = request.form['Y2']
            else:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!..You forgot entering Y’’( ):")
        if (Method == 2 and ( O_Dim == 3)):
            temp_to_test = (request.form['Y3'])
            if not temp_to_test == '':
                try:
                    func_xyzt(str(request.form['Y3']), 1, 1, 1, 1)
                except NameError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!..Enter valid equation for Y’’’( )")
                else:
                 List_eqs[2] = request.form['Y3']
            else:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!..You forgot entering Y’’’( )")
        if (Method == 2 and (O_Dim ==1) and Eqs_No==2) or (Method == 1 and ( Eqs_No==2 or Eqs_No==3)):
            temp_to_test = ( request.form['Z1'])
            if not temp_to_test == '':
                try:
                    func_xyzt(str(request.form['Z1']), 1, 1, 1, 1)
                except NameError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!..Enter valid equation for Z’( ) " )
                else:
                 List_eqs[3] = request.form['Z1']
            else:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!..You forgot entering Z’( )")
        if(Method == 1 and Eqs_No == 3):
            temp_to_test = (request.form['T1'])
            if not temp_to_test == '':
                try:
                    func_xyzt(str(request.form['T1']), 1, 1, 1, 1)
                except NameError:
                    return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css",
                                           wing="DE - Copy.png",
                                           logo="Logo.svg", error="Ops!..Enter valid equation for t’( ) " )
                else:
                 List_eqs[4] = request.form['T1']
            else:
                return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png",
                                       logo="Logo.svg", error="Ops!..You forgot entering t’( )")
        if Method == 1:
            result=Solve_Euler(Eqs_No,List_eqs[0],List_eqs[3],List_eqs[4],List_initial_values[0],List_initial_values[1],List_initial_values[2],List_initial_values[3],List_initial_values[6],h_or_n,StoppingCriteria,num_iteration)
            Length = len(result[8])
        else:
            result=Solve_Heun(O_Dim,Eqs_No,List_eqs[0],List_eqs[3],List_eqs[1], List_eqs[2],y_exact,List_initial_values[0],List_initial_values[1],List_initial_values[2],List_initial_values[4],List_initial_values[5],List_initial_values[6],iter_or_stoppingC,num_iteration,StoppingCriteria)
            Length=len(result[1])
        if result:
              return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen',
                                       css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg",
                                        Method=Method, iterations=Length,num_eqs=Eqs_No, results=result,ODE_dim=O_Dim,Atx=List_initial_values[6],Y_eq=List_eqs[0],Ydash_eq=List_eqs[1],Yddash_eq=List_eqs[2],Z_eq=List_eqs[3],T_eq=List_eqs[4],StoppingCriteria=StoppingCriteria,num_iteration=num_iteration,x=List_initial_values[0],y=List_initial_values[1],z=List_initial_values[2],t=List_initial_values[3],ydash=List_initial_values[4],yddash=List_initial_values[5],y_exact=y_exact)

        return redirect(url_for('ODEEH'))

    else:
      return render_template('ODEEH.html', url="pntenkMEUyk", title='ODE Euler&Huen', css="ODEEH.css", wing="DE - Copy.png", logo="Logo.svg")

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
            yp=''
            #results=[]
            Number_Of_Points=0

            Method = request.form['Method']
            Equation = request.form['Equation']

            for i in range(8):
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
                    try :
                        results=ode_adams_backward_difference(Equation,Number_Of_Corrections,Stopping_Criteria,Number_Of_Points,x,y,x_requested)
                        return render_template('ODEPC.html', url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",results=results,Method=Method,OK=Is_OK)
                    except:
                        return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=False)
                else:
                    return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=False)

            else :

                return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)

        elif Method=="MilneMethod":
            if Is_OK==True:
                if len(x)!=0 and Equation :

                    try :

                        relative_error,yp, YC=milne(Equation,5,x,y,x_requested,Stopping_Criteria,Number_Of_Corrections)

                        return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",yp=yp,YC=YC,Error=relative_error,Method=Method,OK=Is_OK)
                    except:
                        return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=False)
                else :
                    return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=False)

            else :
                return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)
        else :
            return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg",Method=Method,OK=Is_OK)


    else:
        return render_template('ODEPC.html',  url="icvMDjMea3w" , title='ODE Predictor/Corrector', css="ODEPC.css", wing="DE - Copy.png", logo="Logo.svg")

@app.route('/_background_process_PDE', methods=['POST', 'GET'])
def background_process():
    try:
        Choice = request.form['Method']
    except:
        return jsonify(error = 'Choose a Method', U = '')

    if Choice == "Irregular":
            #Taking the equation parameters
        #h = k = 0
        #dxx = dyy = dx = dy = u_coeff = function = ''
        try:
            h = float((eval(request.form['h_step'])))
            k = float(eval(request.form['k_step']))
        except:
            return jsonify(error = 'Enter h and k', U = '')

        dxx = request.form['dxx']
        dyy = request.form['dyy']
        dx = request.form['dx']
        dy = request.form['dy']
        u_coeff = request.form['U_Coeff']
        function = request.form['Function']

        if not(dxx and dyy and dx and dy and u_coeff and function):
            return jsonify(error = 'Enter Equation', U = '')

        boundaries=[]
        for i in range(12):
         #Strings for table records :

            f_str = 'function'+str(i)
            x_i_str = 'xi' + str(i)
            x_f_str = 'xf' + str(i)
            y_i_str = 'yi' + str(i)
            y_f_str = 'yf' + str(i)
            u_str = 'u' + str(i)
            #Parameters
            f = request.form[f_str]
            x_i = request.form[x_i_str]
            x_f = request.form[x_f_str]
            y_i = request.form[y_i_str]
            y_f = request.form[y_f_str]
            u = request.form[u_str]

            #Check that the table record is not empty

            if not f=="" and not x_i=="" and not x_f=="" and not y_i=="" and not y_f=="" and not u=="":
                x_i = float(request.form[x_i_str])
                x_f = float(request.form[x_f_str])
                y_i = float(request.form[y_i_str])
                y_f = float(request.form[y_f_str])
                bound = boundry(y_i, y_f, x_i, x_f, f,u)
                boundaries.append(bound)
        try:
            grid = Grid(boundaries,h,k)
            grid.Plot_Region()
        except:
            return jsonify(error = 'Invalid Boundaries', U = '')

        try:
            points = grid.get_points(grid.get_boundry_rows_points(),grid.get_boundry_cols_points())
        except:
            return jsonify(error = 'Invalid Boundaries', U = '')

        pde = PDE_Solver(points,grid)
        pde.Get_Parameters(dxx, dyy, dx, dy, u_coeff, function)

        try:
            x_point = float(eval(request.form['x_cordinates']))
            y_point = float(eval(request.form['y_cordinates']))
        except:
            return jsonify(error = 'Enter x any y Values', U = '')

        _point = point(x_point,y_point,False)

        try:
            U_Value = pde.Solve_At_Point(_point)
        except ValueError:
            return jsonify(error = 'Invalid Point', U = '')
        except:
            return jsonify(error = 'Could not Solve at This Point', U = '')

        return jsonify(U = U_Value)
    else :
        try:
            h = float(eval(request.form['h_step']))
            k = float(eval(request.form['k_step']))
        except:
            return jsonify(error = 'Enter h and k', U = '')

        try:
            dxx = float(request.form['dxx'])
            dyy = float(request.form['dyy'])
            dx = float(request.form['dx'])
            dy = float(request.form['dy'])
            dxy = float(request.form['dxy'])
            u_coeff = float(request.form['U_Coeff'])
            function = request.form['Function']
        except:
            return jsonify(error = 'Enter Equation', U = '')

        xi_list = []
        xf_list = []
        yi_list = []
        yf_list = []
        value_list = []
        function_list = []
        boundry_counter = 0
        U = ''
        yy = 0
        Rows = 0
        Value = 0

        try:
            for i in range(4) :
                #f_str = 'function' + str(i)
                x_i_str = 'xi' + str(i)
                x_f_str = 'xf' + str(i)
                y_i_str = 'yi' + str(i)
                y_f_str ='yf' + str(i)
                u_str ='u' + str(i)
                #Parameters
                #f = request.form[f_str]
                x_i = request.form[x_i_str]
                x_f = request.form[x_f_str]
                y_i = request.form[y_i_str]
                y_f = request.form[y_f_str]
                u = request.form[u_str]
                if not x_i=="" and not x_f=="" and not y_i=="" and not y_f=="" and not u=="":
                    x_i = float(request.form[x_i_str])
                    x_f = float(request.form[x_f_str])
                    y_i = float(request.form[y_i_str])
                    y_f = float(request.form[y_f_str])
                    xi_list.append(x_i)
                    xf_list.append(x_f)
                    yi_list.append(y_i)
                    yf_list.append(y_f)

                    value_list.append(u)
                    boundry_counter = boundry_counter + 1

                #Open Boundary Condition
                elif x_i=="" and x_f=="" and not y_i=="" and not y_f=="" and not u=="":
                    yy = int(y_i)
                    Rows = int(y_f)
                    Value = int(u)
        except:
            return jsonify(error = 'Invalid Boundaries', U = '')

        if boundry_counter != 4 and boundry_counter != 3:
            return jsonify(error = 'Invalid Number of Boundaries', U = '')

        #Getting the boundaries and their values from the previous loop then find The x_range and y_range
        x1=min(xi_list)
        x2=max(xf_list)
        y1=min(yi_list)
        y2=max(yf_list)

        if boundry_counter==4:
            try:
                # L R U D

                UList = Closed_Region(value_list[1], value_list[2], value_list[0], value_list[3], h, k,
                                      x1, x2, y1, y2, dxx, dyy, dx, dy, u_coeff, dxy, function)

            except:
                return jsonify(error = 'Could not Solve')
            try:
                x_point = float(eval(request.form['x_cordinates']))
                y_point = float(eval(request.form['y_cordinates']))
            except:
                return jsonify(error = 'Enter x any y Values', U = '')


            x_index = (x_point-x1)/h
            y_index = (y_point-y1)/k

            try:
                U = UList[int(x_index)][int(y_index)]

            except:
                return jsonify(error = 'Invalid Point', U = '')

            return jsonify(U = U)

        #Indication to open boundries --->
        elif boundry_counter==3:
            try:
                x_point = float(request.form['x_cordinates'])
                y_point = float(request.form['y_cordinates'])
            except:
                return jsonify(error = 'Invalid Point', U = '')

            x_index = (x_point-x1) / h
            y_index = (y_point-y1) / k
            Number_Of_Rows = y_index + 1

            try:
                # yy --> y_i
                # Rows -->y_f
                # value --> function
                UList = Open_Region(value_list[0], value_list[1], value_list[2], h, k, x1, x2,
                                    y1, dxx, dyy, dx, dy, u_coeff, dxy, function, Value, yy, int(Number_Of_Rows))

            except:
                return jsonify(error = 'Could not Solve', U = '')

            try:
                U = UList[int(x_index)][int(y_index)]
            except:
                return jsonify(error = 'Could not Solve at This Point', U = '')

            return jsonify(U = U)
        else:
            return jsonify(error = 'Invalid Number of Boundaries', U = '')

@app.route("/PDE", methods=['GET'])
def PDE():
    return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - Copy.png", logo="Logo.svg")

@app.route("/LinearSystem", methods=['GET', 'POST'])
def LinearSystem():

    if request.method == 'POST':
        anyErrorsInPosting = 0
        errorMSG=''
        Length = 0
        temp_to_test = 0
        inputs = []
        result = []
        n = 0
        choice = 0
        iterations = 0
        StoppingCriteria = 0.0
        w = 1
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
            for x in inputs:
                try:
                    float(x)
                except :
                    anyErrorsInPosting=1
                    errorMSG="please enter numbers only"
                    break
##########################################################################
        if (n*(n+1)==len(inputs)) and (StoppingCriteria or iterations) and w and choice and (not anyErrorsInPosting):
            result = solve_linear_systems(n,inputs,w,choice,iterations,StoppingCriteria)
            Length = len(result[0])
            errorOccInCalc=result[1]
            if Length:
                return render_template('LinearSystem.html', url="h_UP4CVuQeE", title='Linear Systems', css="LinearSystem.css",
                                       wing="SE - Copy2.png", logo="Logo Greeny.svg", Eqs_No=n, results=result,
                                       inputs=inputs, choice=choice, iterations=iterations,
                                       StoppingCriteria=StoppingCriteria, w=w,anyErrorsInPosting=0,errorMSG=errorMSG)
            else:
                anyErrorsInPosting = 1
                errorMSG = "Can't be solved using this method !"
        else:
            anyErrorsInPosting = 1  # as it will enter 'else' only if an error has occurred
            errorMSG = "please fill all the inputs !"

        if anyErrorsInPosting:
            return render_template('LinearSystem.html', url="h_UP4CVuQeE", title='Linear Systems', css="LinearSystem.css",
                                   wing="SE - Copy2.png", logo="Logo Greeny.svg", inputs=inputs, choice=choice, iterations=iterations,
                                       StoppingCriteria=StoppingCriteria, w=w,anyErrorsInPosting=anyErrorsInPosting,errorMSG=errorMSG)
        return redirect(url_for('LinearSystem'))
    else:
        return render_template('LinearSystem.html', url="h_UP4CVuQeE", title='Linear Systems', css="LinearSystem.css", wing="SE - Copy2.png", logo="Logo Greeny.svg")

@app.route("/NonlinearSystem", methods=['GET', 'POST'])
def NonlinearSystem():
    if request.method == 'POST':
        Method = ''
        errorMSG = ''
        Eqs_No = iterations = f_xy = g_xy =X0 = Y0 = 0
        StoppingCriteria = 0.0
        Length = 0
        result = []

        if 'Method' in request.form:
            Method  = request.form['Method']
        try:
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

        except:
            anyErrorsInPosting = 1
            errorMSG = errorMSG + " Invalid inputs"


        if Method and Eqs_No and not StoppingCriteria == '' and iterations and f_xy and g_xy and X0 and Y0:
            if Method == "NewtonRaphson":
                if Eqs_No == 2:
                    try:
                        result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, 0, X0, Y0, 0, StoppingCriteria)
                        Length = len(result[1])
                    except:
                        anyErrorsInPosting = 1
                        errorMSG = "can't be solved using this method !"
                elif Eqs_No == 3 and Z0 and h_xy:
                    try:
                        result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, h_xy, X0, Y0, Z0, StoppingCriteria)
                        Length = len(result[1])
                    except:
                        anyErrorsInPosting = 1
                        errorMSG = "can't be solved using this method !"
            elif Method == "FixedPoint":
                if Eqs_No == 2:
                    try:
                        result = FixedPointIteration(str(Eqs_No), str(iterations), str(StoppingCriteria), f_xy, g_xy, X0, Y0)
                        Length = len(result[1])
                    except:
                        anyErrorsInPosting = 1
                        errorMSG = "can't be solved using this method !"
                elif Eqs_No == 3 and h_xy and Z0:
                    try:
                        result = FixedPointIteration(str(Eqs_No), str(iterations), str(StoppingCriteria), f_xy, g_xy, X0, Y0, h_xy, Z0)
                        Length = len(result[1])
                    except:
                        anyErrorsInPosting = 1
                        errorMSG = "can't be solved using this method !"
            if Length:
                return render_template('NonlinearSystem.html', url="4pb2Khe2fSM", title='Nonlinear Systems', css="NonlinearSystems.css", wing="SE - Copy2.png", logo="Logo Greeny.svg", Length=Length, Method=Method, iterations=iterations, Eqs_No=Eqs_No, results=result)
            else:
                anyErrorsInPosting = 1
                errorMSG = "can't be solved using this method !"
        else:
            anyErrorsInPosting = 1  # as it will enter 'else' only if an error has occurred
            if errorMSG == '':
                errorMSG = " please fill all the inputs !"
            if not Method:
                errorMSG = errorMSG + " ,please Select a method!"
            if not Eqs_No:
                errorMSG = errorMSG + " ,please Enter number of Equations!"
            if not errorMSG == " please fill all the inputs !":
                errorMSG = errorMSG + " ,please fill all the inputs correctly!"

        if anyErrorsInPosting:
            return render_template('NonlinearSystem.html', url="4pb2Khe2fSM", title='Nonlinear Systems',
                                   css="NonlinearSystems.css",
                                   wing="SE - Copy2.png", logo="Logo Greeny.svg", Method=Method,
                                   iterations=iterations, Eqs_No=Eqs_No, results=result,
                                   StoppingCriteria=StoppingCriteria, anyErrorsInPosting=anyErrorsInPosting,
                                   errorMSG=errorMSG)

        return redirect(url_for('NonlinearSystem'))
    else:
        return render_template('NonlinearSystem.html', url="4pb2Khe2fSM", title='Nonlinear Systems', css="NonlinearSystems.css", wing="SE - Copy2.png", logo="Logo Greeny.svg")


@app.route("/EigenvalueProblem", methods=['GET', 'POST'])
def EigenvalueProblem():
    anyErrorsInPosting = 0
    errorMSG = ''
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
        for x in list_of_entires:
            try:
                float(x)
            except :
                anyErrorsInPosting = 1
                errorMSG = "Please, enter numbers only"
                break
        for x in list_init_vector:
            try:
                float(x)
            except ValueError:
                anyErrorsInPosting = 1
                errorMSG = "Please, enter numbers only"
                break

        if not anyErrorsInPosting and size and (size * size == len(list_of_entires)) and (1 * size == len(list_init_vector)) and iter_or_stoppingC and (StoppingCriteria or num_iteration) and Method:
            result = solve_Eigenvalue(size, list_of_entires, list_init_vector, Method, iter_or_stoppingC, num_iteration, StoppingCriteria)
            # result[0] List_Eig_values-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[1] List_Eig_vectors-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[2] List_relative_error-> if method == 1 or 2: carries the iterations, if method==3: carries the value to be displayed
            # result[3] Eig_value ->if method == 1 or 2 : carries the value to be displayed
            # result[4] Eig_vector ->if method == 1 or 2 : carries the value to be displayed
            # result[5] True_error ->if method == 1 or 2 : carries the value to be displayed
            # result[6] test -> if false then there was an error in the calculations of the power method
            Length = len(result[0])
            if Length :
                return render_template('EigenvalueProblem.html', url="BYwlztZrgqM", title='Eigenvalue Problem',
                                       css="EigenvalueProblem.css", wing="SE - Copy2.png", logo="Logo Greeny.svg",
                                       Length=size, Method=Method, iterations=Length, results=result,
                                       iter_or_stoppingC=iter_or_stoppingC, num_iteration=num_iteration,
                                       StoppingCriteria=StoppingCriteria, list_init_vector=list_init_vector,
                                       list_of_entires=list_of_entires,anyErrorsInPosting=0,errorMSG=errorMSG)
            else:
                anyErrorsInPosting = 1
                errorMSG = "can't be solved using this method !"
        else:
            anyErrorsInPosting = 1  # as it will enter 'else' only if an error has occurred
            errorMSG = "Please fill all the inputs !"

        if anyErrorsInPosting:
            return render_template('EigenvalueProblem.html', url="BYwlztZrgqM", title='Eigenvalue Problem',
                                   css="EigenvalueProblem.css", wing="SE - Copy2.png", logo="Logo Greeny.svg",
                                   Length=size, Method=Method, iterations=Length, results=result,
                                   iter_or_stoppingC=iter_or_stoppingC, num_iteration=num_iteration,
                                   StoppingCriteria=StoppingCriteria, list_init_vector=list_init_vector,
                                   list_of_entires=list_of_entires, anyErrorsInPosting=anyErrorsInPosting,errorMSG=errorMSG)
        return redirect(url_for('EigenvalueProblem'))
    else:
        return render_template('EigenvalueProblem.html', url="BYwlztZrgqM", title='Eigenvalue Problem', css="EigenvalueProblem.css",
                               wing="SE - Copy2.png", logo="Logo Greeny.svg")

@app.route("/LeastAbsoluteErrors", methods=['GET', 'POST'])
def LeastAbsoluteErrors():
    if request.method == 'POST':
        xdata=[]
        ydata=[]
        i=0
        Iterations=1000
        Tolerance=1/1000

        if (request.form['iterations'] != ''):
            I=request.form['iterations']
    
            if( len(I.split(' '))==1):
                if(float(eval(I.split(' ')[0]))>=1 ):
                    Iterations = I.split(' ')[0]
                elif(float(eval(I.split(' ')[0]))<1 and float(eval(I.split(' ')[0]))>=0 ):
                    Tolerance= eval(I.split(' ')[0])
                    if(float(eval(I.split(' ')[0]))==0):
                        Tolerance=1/1000000

            else:
                Iterations = request.form['iterations'].split(' ')[0]
                Tolerance = eval(request.form['iterations'].split(' ')[2])
            Iterations=int(np.ceil(int(Iterations)))
            Tolerance=float(Tolerance)


        while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
            try:
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
            except:
                pass
            i += 1

        x,y=Numpify(xdata,ydata)
        Th=LeastSquares(x,y,4)
        XD,YD,W,th=LeastAbsoluteDeviations(x,y,Tolerance,Iterations,4)
        Ya=str(round(th[1][0],4))+"*x"+"+"+str(round(th[0][0],4))
        Ys=str(Th[1][0])+"*x"+"+"+str(Th[0][0])
        Angle=str(round(Angulus(th,Th),3))+"°"
        Gradi=ZeroDerivativeCheck(XD,YD,W,th)
        Gradi="("+str(Gradi[0][0])+" , "+str(Gradi[0][1])+")"
        Qa,Qs=CorrelationCoefficients(th,Th,x,y)
        if (i == 0):
            return render_template('LeastAbsoluteErrors.html', url="", error="Missing inputs!",
                                    title='Least Absolute Deviations', css="LeastAbsoluteErrors.css", wing="CF Header.png", logo="Logo.svg")

        return render_template('LeastAbsoluteErrors.html', url="",
                                        title='Least Absolute Deviations', css="LeastAbsoluteErrors.css", wing="CF Header.png", logo="Logo.svg", Ya=Ya, Ys=Ys
                                      ,Qs=Qs,Qa=Qa,Angle=Angle,Gradi=Gradi  )
    else:
        return render_template('LeastAbsoluteErrors.html', url="",
                                        title='Least Absolute Deviations', css="LeastAbsoluteErrors.css", wing="CF Header.png", logo="Logo.svg")


@app.route("/LogCoshLoss", methods=['GET', 'POST'])
def LogCoshLoss():
    if request.method == 'POST':
        xdata=[]
        ydata=[]
        i=0
        Iterations=1000
        Tolerance=0
        Learning_Rate=0.01
        if request.form['iterations']:
            Iterations=eval(request.form['iterations'])
        if request.form['Lamda']:
            Learning_Rate=eval(request.form['Lamda'])



        while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!=''):
            try:
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
            except:
                pass
            i += 1

        x,y=Numpify(xdata,ydata)
        Th=LeastSquares(x,y,4)
        th, Gradi=minLogCoshLoss(x,y,Iterations,Learning_Rate,Tolerance,4)
        Gradi="("+str(Gradi[0][0])+" , "+str(Gradi[1][0])+")"
        Ya=str(round(th[1][0],4))+"*x"+"+"+str(round(th[0][0],4))
        Ys=str(Th[1][0])+"*x"+"+"+str(Th[0][0])
        Angle=str(round(Angulus(th,Th),3))+"°"
        Qa,Qs=RegressionErrors(th,Th,x,y)
        if (i == 0):
            return render_template('LogCoshLoss.html', url="", error="Missing inputs!",
                                    title='Log-Cosh Loss', css="LogCoshLoss.css", wing="CF Header.png", logo="Logo.svg")

        return render_template('LogCoshLoss.html', url="",
                                        title='Log-Cosh Loss', css="LogCoshLoss.css", wing="CF Header.png", logo="Logo.svg", Ya=Ya, Ys=Ys
                                      ,Qs=Qs,Qa=Qa,Angle=Angle,Gradi=Gradi  )
    else:
        return render_template('LogCoshLoss.html', url="",
                                        title='Log-Cosh Loss', css="LogCoshLoss.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/SurfaceInterpolation", methods=['GET', 'POST'])
def SurfaceInterpolation():
    if request.method == 'POST':
        LHS = 0
        i = 0
        xdata = []
        ydata = []
        zdata = []
        RHS = 0

        while (request.form['x_coordinates' + str(i)]!='' and request.form['y_coordinates' + str(i)]!='' and request.form['z_coordinates' + str(i)]!=''):
            try:
                xdata.append(float(request.form['x_coordinates' + str(i)]))
                ydata.append(float(request.form['y_coordinates' + str(i)]))
                zdata.append(float(request.form['z_coordinates' + str(i)]))
            except:
                pass
            i += 1

        if xdata:
            try:
                LHS, RHS, Constants, Sr = SurfaceInt(xdata, ydata, zdata, 10)
            except:
                return render_template('SurfaceInt.html', url="mRjVy0MSUI0",
                                        title='Surface Interpolation', css="SurfaceInt.css", wing="CF Header.png",
                                        logo="Logo.svg", error = 'Invalid Input', results='Invalid Input', Error='...')

        if RHS:
            GriX, GriY, GriZ = PointsFor3DSF(xdata,ydata,RHS)
            GriZ = GriZ.transpose()
            x1 = list(GriX)
            y1 = list(GriY)
            z1 = []

            for i in range(np.shape(GriZ)[0]):
                z1.append(list(GriZ[i]))




        if LHS and RHS and not Sr == '':
            return render_template('SurfaceInt.html', url="mRjVy0MSUI0",
                                        title='Surface Interpolation', css="SurfaceInt.css",wing="CF Header.png",
                                    logo="Logo.svg", results=RHS, x1 = x1, y1 = y1, z1 = z1)
        elif not xdata:
            return render_template('SurfaceInt.html', url="mRjVy0MSUI0",
                                        title='Surface Interpolation', css="SurfaceInt.css", wing="CF Header.png",
                                    logo="Logo.svg", error = 'Missing Points', results='Missing Points')
        else:
            return render_template('SurfaceInt.html', url="mRjVy0MSUI0",
                                        title='Surface Interpolation', css="SurfaceInt.css", wing="CF Header.png",
                                    logo="Logo.svg", results='Singular Matrix/Out of Domain', error = 'Singular Matrix')
    else:
        return render_template('SurfaceInt.html', url="mRjVy0MSUI0",
                                        title='Surface Interpolation', css="SurfaceInt.css", wing="CF Header.png", logo="Logo.svg")

if __name__ == '__main__':
    app.run(debug=True)
