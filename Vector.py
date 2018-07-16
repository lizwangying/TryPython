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
            self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG = '不能标准化0向量'

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
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        '向量的点积'
        return sum([x*y for x,
                    y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degree=False):
        '向量的夾角計算'
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degree:
                degree_per_radian = 180./pi
                return angle_in_radians*degree_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('不能与0向量计算夹角')
            else:
                raise e


# v1 = Vector([3, 4])
# v2 = Vector([5.581, -2.136])
v3 = Vector([7.887, 4.138])
v4 = Vector([-8.802, 6.776])
# print(v1.plus(v2))
# print(v1.minus(v2))
# print(v1.times_scalar(2))
# print(v1.magnitude.__doc__)
# print(v2.normalized())
print(v3.dot(v4))

v5 = Vector([3.183, -7.627])
v6 = Vector([-2.668, 5.319])
print(v5.angle_with(v6,False))
