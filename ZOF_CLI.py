#!/usr/bin/env python3
"""
ZOF_CLI.py
Command-line Zero Of Functions solver implementing:
1. Bisection
2. Regula Falsi (False Position)
3. Secant
4. Newton-Raphson
5. Fixed Point Iteration
6. Modified Secant

Usage: run and follow the menu prompts.
"""

from zof_core import *

def print_table(rows):
    for row in rows:
        print("\t".join(f"{v:.8g}" if isinstance(v, (int,float)) else str(v) for v in row))

def main():
    print("=== Zero of Functions (CLI Solver) ===")
    expr = input("Enter f(x) in Python syntax: ")

    f = parse_function(expr)

    print("""
1. Bisection
2. Regula-Falsi
3. Secant
4. Newton-Raphson
5. Fixed Point
6. Modified Secant
""")

    choice = int(input("Choose method: "))
    tol = float(input("Tolerance: "))
    max_iter = int(input("Max Iterations: "))

    if choice == 1:
        a = float(input("a: ")); b = float(input("b: "))
        logs = bisection(f, a, b, tol, max_iter)

    elif choice == 2:
        a = float(input("a: ")); b = float(input("b: "))
        logs = regula_falsi(f, a, b, tol, max_iter)

    elif choice == 3:
        x0=float(input("x0: ")); x1=float(input("x1: "))
        logs = secant(f, x0, x1, tol, max_iter)

    elif choice == 4:
        x0=float(input("x0: "))
        dexpr = input("Enter derivative f'(x) or press ENTER for numerical: ")
        if dexpr.strip():
            df = parse_function(dexpr)
        else:
            df = lambda x: (f(x+1e-6)-f(x-1e-6))/(2e-6)
        logs = newton_raphson(f, df, x0, tol, max_iter)

    elif choice == 5:
        gexpr=input("Enter g(x): ")
        g=parse_function(gexpr)
        x0=float(input("x0: "))
        logs=fixed_point(g, x0, tol, max_iter)

    elif choice == 6:
        x0=float(input("x0: "))
        delta=float(input("delta: "))
        logs = modified_secant(f, x0, delta, tol, max_iter)

    print("\n=== ITERATIONS ===")
    print_table(logs)

    print("\nApproximate Root:", logs[-1][-2])

if __name__ == "__main__":
    main()
