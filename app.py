from flask import Flask, render_template, request
from zof_core import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            method = request.form["method"]
            expr = request.form["expr"]
            tol = float(request.form["tol"])
            max_iter = int(request.form["max_iter"])
            f = parse_function(expr)

            # Method handling
            if method == "bisection":
                a=float(request.form["a"]); b=float(request.form["b"])
                logs=bisection(f,a,b,tol,max_iter)

            elif method == "regula":
                a=float(request.form["a"]); b=float(request.form["b"])
                logs=regula_falsi(f,a,b,tol,max_iter)

            elif method == "secant":
                x0=float(request.form["x0"]); x1=float(request.form["x1"])
                logs=secant(f,x0,x1,tol,max_iter)

            elif method == "newton":
                x0=float(request.form["x0"])
                dexpr=request.form["dexpr"]
                if dexpr.strip():
                    df=parse_function(dexpr)
                else:
                    df=lambda x: (f(x+1e-6)-f(x-1e-6))/(2e-6)
                logs=newton_raphson(f,df,x0,tol,max_iter)

            elif method == "fixed":
                gexpr=request.form["gexpr"]
                g=parse_function(gexpr)
                x0=float(request.form["x0"])
                logs=fixed_point(g,x0,tol,max_iter)

            elif method == "modified":
                x0=float(request.form["x0"])
                delta=float(request.form["delta"])
                logs=modified_secant(f,x0,delta,tol,max_iter)

            result = logs

        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
