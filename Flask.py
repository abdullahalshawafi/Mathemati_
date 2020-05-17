from flask import Flask, render_template, url_for, request
from methods.NewtonRaphson import Newton_Raphson
app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = 'edcb30ed4a6a5b467a2ed529ed889dbf'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/NonlinearSystem", methods=['GET', 'POST'])
def NonlinearSystem():
    if request.method == 'POST':
        Method  = request.form['Method']
        Eqs_No = int(request.form['Dim'])
        StoppingCriteria = float(request.form['StoppingCriteria'])
        iterations = int(request.form['Iterations'])
        if Eqs_No == 2:
            f_xy = request.form['Feq']
            g_xy = request.form['Geq']
            h_xy = 0
            X0 = float(request.form['X0'])
            Y0 = float(request.form['Y0'])
            Z0 = 0
        elif Eqs_No == 3:
            f_xy = request.form['Feq']
            g_xy = request.form['Geq']
            h_xy = request.form['Heq']
            X0 = float(request.form['X0'])
            Y0 = float(request.form['Y0'])
            Z0 = float(request.form['Z0'])
        result = [[0 for x in range(1)] for y in range(Eqs_No * iterations)]
        result = Newton_Raphson(Eqs_No, iterations, f_xy, g_xy, h_xy, X0, Y0, Z0, StoppingCriteria)
        Length = len(result)
        print(result)
        return render_template('NonlinearSystem.html', title='Nonlinear Systems', css="NonlinearSystems.css", Length=Length, Method=Method, iterations=iterations, Eqs_No=Eqs_No, results=result)
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
