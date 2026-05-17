import math
a,b,c=int(input()),int(input()),int(input())
D=b**2-4*a*c
if D<0 :
    print('корней нет')
else :
    s = ((-b - math.sqrt(D)) / 2 * a)
    f = ((-b + math.sqrt(D)) / 2 * a)
    print(s,f)
