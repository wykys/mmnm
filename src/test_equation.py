from sympy import *

def test_equation(f_str: str):
    try:
        x = Symbol('x')
        eval(f_str)
    except SyntaxError:
        print('error: incorrect equation')
        exit()
