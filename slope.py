import math

def slope(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    return m

def intercept(x1, y1, x2, y2):
    b = y1 - (slope(x1, y1, x2, y2)*x1)
    return b

print intercept(1,3,2,6)
