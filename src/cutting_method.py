#!/usr/bin/env python3


import numpy as np
from sympy import *
from problem import collection
from result import Result, separator


def cutting_method(f_str, start, eps=0.01, debug=False, max_i=500):
    """
    najde kořen funkce x na vstupu
    využívá metodu sečen
    """
    x0 = np.float(start[0])
    x1 = np.float(start[1])
    i = 0

    x = Symbol('x')
    f_ddx_str = str(diff(diff(eval(f_str))))

    def f(x): return eval(f_str)
    def f_ddx(x): return eval(f_ddx_str)

    # rovnice sečny ke grafu funkce, daná body x0 a x1, výsledek je f(x0)
    def y(x0, x1): return f(x1) + ((f(x1) - f(x0)) / (x1 - x0)) * (x0 - x1)

    def sign_eq(x0, x1): return x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    def sign_no_eq(x0, x1): return x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))

    next_x_fce = sign_eq if f(x0) > 0 and f_ddx(x1) > 0 else sign_no_eq

    valid = 'OK'
    #while abs(y(x0, x1)) > eps:
    while abs(f(x0)) > eps:
        x2 = next_x_fce(x0, x1)
        x0 = x1
        x1 = x2
        i += 1

        if i > max_i:
            valid = 'ERR'
            break

    x = x0
    y = y(x0, x1)
    result = Result(x, y, i, 'cutting', valid)

    if debug:
        print(result)
        separator('=')

    return result


if __name__ == "__main__":
    for problem in collection.database:
        problem.show()
        separator('-')
        cutting_method(str(problem), problem.two_point(), debug=True)
