import numpy as np
from matplotlib import pyplot as plt
from numpy import *


def graph(problem, result):

    a = min(problem.two_point())
    b = max(problem.two_point())

    if result is not None:
        tmp = list([res.x for res in result if res.x != float('NaN') and res.valid == 'OK'])
        tmp.append(a)
        a = float(min(tmp))

        tmp = list([res.x for res in result if res.x != float('NaN') and res.valid == 'OK'])
        tmp.append(b)
        b = float(max(tmp))

    x = np.linspace(a, b, 1000)
    y = eval(str(problem))

    fig = plt.figure()
    plt.plot(x, y, label='fce')

    if result is not None:
        for res in result:
            if res.x != float('NaN') and res.y != float('NaN') and res.valid == 'OK':
                plt.plot([res.x], [res.y], 'x', label=str(res.name))

    plt.grid(which='both', linestyle=':')
    plt.title(f'${problem.latex()}$', fontsize=14)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
