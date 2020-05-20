from flask import Flask, render_template, url_for, request, redirect
from methods.NewtonRaphson import Newton_Raphson
from methods.FixedPoint import FixedPointIteration
from methods.PDE_Solve import Grid, PDE_Solver, boundry , point
app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'edcb30ed4a6a5b467a2ed529ed889dbf'

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')

@app.route("/PolynomialInterpolation", methods=['GET', 'POST'])
def PolynomialInterpolation():
    if request.method == 'POST':
        pass
    else:
        return render_template('PolynomialInterpolation.html', title='Polynomial Interpolation', css="PolynomialInterpolation.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/SplineInterpolation", methods=['GET', 'POST'])
def SplineInterpolation():
    if request.method == 'POST':
        pass
    else:
        return render_template('SplineInterpolation.html', title='Spline Interpolation', css="SplineInterpolation.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/LeastSquareReg", methods=['GET', 'POST'])
def LeastSquareReg():
    if request.method == 'POST':
        pass
    else:
        return render_template('LeastSquareReg.html', title='Least Square Reg.', css="LeastSquareReg.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/SurfaceFitting", methods=['GET', 'POST'])
def SurfaceFitting():
    if request.method == 'POST':
        pass
    else:
        return render_template('SurfaceFitting.html', title='Surface Fitting', css="SurfaceFitting.css", wing="CF Header.png", logo="Logo.svg")

@app.route("/PDE", methods=['GET', 'POST'])
def PDE():
    if request.method == 'POST':
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

        grid=Grid(boundaries,h,k)
        points=grid.get_points(grid.get_boundry_rows_points(),grid.get_boundry_cols_points())
        pde=PDE_Solver(points,grid)
        pde.Get_Parameters(dxx,dyy,dx,dy,u_coeff,function)
        x_point=float(request.form['x_cordinates'])
        y_point=float(request.form['y_cordinates'])
        _point=point(x_point,y_point,False)
        U=request.form['Output_U']
        U_Value=pde.Solve_At_Point(_point)
        U=U_Value
        print(U)
        return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg",U=U)
    else:
        return render_template('PDE.html', title='Numerical PDE', css="PDE.css", wing="DE - copy.png", logo="Logo.svg")

@app.route("/LinearSystem", methods=['GET', 'POST'])
def LinearSystem():
    if request.method == 'POST':

        pass

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

        if Method and Eqs_No and StoppingCriteria and iterations and f_xy and g_xy and X0 and Y0:
            if Method == "NewtonRaphson":
                if Eqs_No == 2:
                    result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, 0, X0, Y0, 0, StoppingCriteria)
                    Length = len(result[1])
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
    if request.method == 'POST':
        pass
    else:
        return render_template('EigenvalueProblem.html', title='Eigenvalue Problem', css="EigenvalueProblem.css", wing="SE - copy2.png", logo="Logo Greeny.svg")

if __name__ == '__main__':
    app.run(debug=True)
