import math
t = float(input("Введение t: "))
a=3*t-6
b=-1*t
c=2*(t-6)
if a == 0:
    x=-c/b
    print("x = " ,x)
else:
    D = b**2-4*a*c
print("D:", D )
print("a:", a)
print("b:",b)
print ("c:", c)
if D>=0:
    x1 =(-b + math.sqrt(D))/(2*a)
    x2=(-b- math.sgrt(D))/(2*a)
    print("x1 =", x1, "\nx2 =", x2)
else:
    print("D<0")