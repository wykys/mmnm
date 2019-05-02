import numpy as np


class Result(object):
    def __init__(self, x, y, i, name='', valid='OK'):
        self.name = name
        self.x = x  # x value
        self.y = y  # y value
        self.i = i  # number of iteration
        self.valid = valid

    def __str__(self):
        return f'{self.name}\n    x: {self.x}\n    y: {self.y}\n    i: {self.i}'

    def array(self):
        return [self.name, self.x, self.y, self.i, self.valid]


def separator(c: str = '='):
    print(c*80)
