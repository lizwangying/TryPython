import sys
sys.path.append("./")
from  Vector import*
try:
    import unittest2 as unittest
except ImportError:
    import unittest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_VectorPlus():
    v1 = Vector([1, 1])
    v2 = Vector([2, 2])
    v3 = v1.plus(v2)
    assert v3 == (3, 3)


# class testPlus(unittest.TestCase):
#     def test_VectorPlusMethod(self):
#         v1 = Vector([1, 1/])
#         v2 = Vector([2, 3])
#         v3 = v1.plus(v2)
#         self.assertEqual(v3.coordinates,(3,4))
