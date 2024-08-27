from ctypes import *
midpoint = CDLL('./mp.so')
a = 0
b = -2
c = 4
d = 3

mid_point = midpoint.mp
mid_point.restype = c_float

print (mid_point(c_float(a), c_float(b)))
print (mid_point(c_float(c), c_float(d)))
