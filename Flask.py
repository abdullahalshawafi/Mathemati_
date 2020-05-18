from flask import Flask, render_template, url_for, request, redirect
from methods.NewtonRaphson import Newton_Raphson
from methods.FixedPoint import FixedPointIteration
app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'edcb30ed4a6a5b467a2ed529ed889dbf'

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')

@app.route("/LinearSystem", methods=['GET', 'POST'])
def LinearSystem():
    if request.method == 'POST':
        pass
    else:
        return render_template('LinearSystem.html', title='Linear Systems', css="LinearSystem.css")

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
                return render_template('NonlinearSystem.html', title='Nonlinear Systems', css="NonlinearSystems.css", Length=Length, Method=Method, iterations=iterations, Eqs_No=Eqs_No, results=result)
        return redirect(url_for('NonlinearSystem'))
    else:
        return render_template('NonlinearSystem.html', title='Nonlinear Systems', css="NonlinearSystems.css")

@app.route("/EigenvalueProblem", methods=['GET', 'POST'])
def EigenvalueProblem():
    if request.method == 'POST':
        pass
    else:
        return render_template('EigenvalueProblem.html', title='Eigenvalue Problem', css="EigenvalueProblem.css")

if __name__ == '__main__':
    app.run(debug=True)
