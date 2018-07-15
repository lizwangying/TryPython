# This Python file uses the following encoding: utf-8
from math import sqrt, pi, acos
from decimal import Decimal, getcontext


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        '向量之间的加法'
        new_coordinates = [x+y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        '向量之间的减法'
        new_coordinates = [x-y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        '向量乘以一个数字'
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        '向量的大小计算函数'
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))
    
    def normalized(self):
        '标准化向量，1.计算出向量大小，2.使向量长度为1'
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception("不能标准化0向量")


    def dot(self, v):
        '向量的点积'
        new_coordinates = [x*y for x,
                           y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def angle_with(self, v, in_degree=False):
        '向量的夾角計算'
        u1 = self.normalized()
        u2 = v.normalized()
        

        


v1 = Vector([3, 4])
v2 = Vector([5.581, -2.136])
print(v1.plus(v2))
print(v1.minus(v2))
print(v1.times_scalar(2))
print(v1.magnitude.__doc__)
print(v2.normalized())
