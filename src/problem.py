#!/usr/bin/env python3
# database with problem from MMNM for testing
from sympy import *
from result import separator
from test_equation import test_equation


class Problem(object):
    def __init__(self, problem, a=0.5, b=1):

        test_equation(problem)

        self.problem = problem

        if a < b:
            self.start_point_a = a
            self.start_point_b = b
        else:
            self.start_point_a = b
            self.start_point_b = a

    def one_point(self):
        if self.start_point_b is None:
            return self.start_point_a
        else:
            return (self.start_point_a + self.start_point_b) / 2

    def two_point(self):
        points = [self.start_point_a, self.start_point_b]
        if self.start_point_b is None:
            points[1] = 0
        return points

    def __str__(self):
        return self.problem

    def show(self):
        x = Symbol('x')
        pretty_print(eval(self.problem))

    def latex(self):
        x = Symbol('x')
        return 'f(x): ' + str(latex(eval(self.problem))) + ' = 0'


class Collection(object):
    def __init__(self):
        self.database = []

    def append(self, problem, a=0, b=None):
        self.database.append(Problem(problem, a, b))

    def show(self):
        for problem in self.database:
            problem.show()
            separator('=')


collection = Collection()
collection.append('exp(x/2) - x**2 - 1', 0.5, 1)
collection.append('sin(x/2) - x**2', 0.3, 1.3)
collection.append('sin(x/2) * cos(x) - 1', 0.5, 1)
collection.append('256*x**9 - 576*x**7 + 432*x**5 - 120*x**3 + 9*x', 1, 2)
collection.append('x**3 + 1', 0, 2)

if __name__ == '__main__':
    init_printing()
    collection.show()
