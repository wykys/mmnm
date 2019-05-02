#!/usr/bin/env python3


import numpy as np
from sympy import *
from problem import collection
from result import Result, separator


def modified_newton_method(f_str, start, eps=0.01, debug=False, max_i=500):
    """
    najde kořen funkce x na vstupu
    využívá modifikovanou newtonovu metodu
    to znamená že se nepřepočítává hodnota
    derivace v každé iterace ale je konstantní
    """

    x0 = float(start)

    x = Symbol('x')
    f_dx_str = str(diff(eval(f_str)))

    def f(x): return eval(f_str)
    def f_dx(x): return eval(f_dx_str)

    const = f_dx(x0)

    x = np.float(x0)
    i = 0

    valid = 'OK'
    while abs(f(x)) > eps:
        x = x - f(x) / const
        i += 1

        if i > max_i:
            valid = 'ERR'
            break

    y = f(x)
    result = Result(x, y, i, 'modified newton', valid)

    if debug:
        print(result)
        separator('=')

    return result


if __name__ == "__main__":

    for problem in collection.database:
        problem.show()
        separator('-')
        modified_newton_method(str(problem), problem.one_point(), eps=0.5, debug=True)
