# zof_core.py
import math

# ---------------- SAFE EVAL FOR USER FUNCTIONS ----------------
SAFE_MATH = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
SAFE_MATH.update({"abs": abs, "max": max, "min": min})

def parse_function(expr):
    """Safely convert string expression to f(x)."""
    def f(x):
        local = {"x": x}
        return eval(expr, {"__builtins__": {}}, {**SAFE_MATH, **local})
    return f

# ---------------------- METHODS -------------------------------

def bisection(f, a, b, tol=1e-6, max_iter=100):
    logs = []
    fa = f(a); fb = f(b)
    if fa * fb > 0:
        raise ValueError("Bisection requires f(a) and f(b) with opposite signs.")

    for i in range(1, max_iter+1):
        c = 0.5*(a+b); fc = f(c)
        logs.append((i, a, b, fa, fb, c, fc, abs(b-a)))
        if abs(b-a) < tol:
            break

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return logs


def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    logs=[]
    fa=f(a); fb=f(b)
    if fa * fb > 0:
        raise ValueError("Regula Falsi requires opposite signs.")

    for i in range(1, max_iter+1):
        xr = b - fb*(a-b)/(fa-fb)
        fxr = f(xr)
        logs.append((i, a, b, fa, fb, xr, fxr, abs(b-a)))

        if abs(fxr) < tol or abs(b-a) < tol:
            break

        if fa * fxr < 0:
            b, fb = xr, fxr
        else:
            a, fa = xr, fxr

    return logs


def secant(f, x0, x1, tol=1e-6, max_iter=100):
    logs=[]
    f0 = f(x0); f1 = f(x1)

    for i in range(1, max_iter+1):
        if (f1 - f0)==0:
            raise ZeroDivisionError("Zero denominator in secant method.")

        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        f2 = f(x2)

        logs.append((i, x0, x1, f0, f1, x2, f2, abs(x2-x1)))

        if abs(x2 - x1) < tol:
            break

        x0, x1, f0, f1 = x1, x2, f1, f2

    return logs


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    logs=[]
    x = x0

    for i in range(1, max_iter+1):
        fx = f(x); dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative zero.")

        x_new = x - fx/dfx
        logs.append((i, x, fx, dfx, x_new, abs(x_new-x)))

        if abs(x_new - x) < tol:
            break

        x = x_new

    return logs


def fixed_point(g, x0, tol=1e-6, max_iter=100):
    logs=[]
    x = x0

    for i in range(1, max_iter+1):
        x_new = g(x)
        logs.append((i, x, x_new, abs(x_new-x)))

        if abs(x_new - x) < tol:
            break

        x = x_new

    return logs


def modified_secant(f, x0, delta=1e-3, tol=1e-6, max_iter=100):
    logs=[]
    x = x0

    for i in range(1, max_iter+1):
        f_x = f(x)
        denom = f(x + delta*x) - f_x
        if denom == 0:
            raise ZeroDivisionError("Zero denominator in Modified Secant.")

        x_new = x - delta*x*f_x/denom
        f_new = f(x_new)

        logs.append((i, x, f_x, x_new, f_new, abs(x_new-x)))

        if abs(x_new - x) < tol:
            break

        x = x_new

    return logs
