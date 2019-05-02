#!/usr/bin/env python3

from problem import collection, Problem
from newton_method import newton_method
from modified_newton_method import modified_newton_method
from cutting_method import cutting_method
from sympy import init_printing
from result import separator
from graph import graph
import argparse
import pandas as pd
import numpy as np


def work(problem, eps, max_i, plot=False):
    equation = str(problem)
    one_point = problem.one_point()
    two_point = problem.two_point()

    problem.show()
    separator('-')
    result = None

    try:
        result = [
            newton_method(equation, one_point, eps=eps, max_i=max_i),
            modified_newton_method(equation, one_point, eps=eps, max_i=max_i),
            cutting_method(equation, two_point, eps=eps, max_i=max_i),
        ]

        print(
            pd.DataFrame(
                map(lambda r: r.array(), result),
                columns=['method', 'x', 'y', 'iteration', 'valid']
            ).to_string(index=False)
        )
        separator('=')

    except:
        print('error: inappropriate starting conditions')

    if plot:
        graph(problem, result)


if __name__ == '__main__':
    separator('=')
    init_printing()

    parser = argparse.ArgumentParser('wykys numeric equation solver')
    parser.add_argument(
        '-q',
        '--equation',
        dest='equation',
        action='store',
        default=None,
        type=str,
        help='user equation'
    )

    parser.add_argument(
        '-e',
        '--epsilon',
        dest='eps',
        action='store',
        default=0.01,
        type=float,
        help='calculation accuracy'
    )

    parser.add_argument(
        '-i',
        '--interval',
        dest='interval',
        action='store',
        default=[0.1, 0.5],
        type=float,
        nargs=2,
        help='start points'
    )

    parser.add_argument(
        '-m',
        '--max_i',
        dest='max_i',
        action='store',
        default=500,
        type=int,
        help='maximum iteration'
    )

    parser.add_argument(
        '-p',
        '--plot',
        dest='plot',
        action='store_true',
        default=False,
        help='plot graph'
    )

    equation = parser.parse_args().equation
    interval = parser.parse_args().interval
    max_i = parser.parse_args().max_i
    plot = parser.parse_args().plot
    eps = parser.parse_args().eps

    if equation is not None:
        work(Problem(equation, interval[0], interval[1]), eps, max_i, plot)

    else:
        for problem in collection.database:
            work(problem, eps, max_i, plot)
