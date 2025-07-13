from math import *

class Vector:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)
    
    def __repr__(self): #how to represent if print(class)
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return hypot(self.x, self.y) #hypotnuse

v1=Vector(2, 4)
v2=Vector(2, 1)
print(v1+v2) #translates to v1.__add__(v2)
print(v1*3) #translates to v1.__mul__(3)
print(abs(v1*3)) #translates to mod of 3*v1