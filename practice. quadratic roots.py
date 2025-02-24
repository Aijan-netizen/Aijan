import math
a = float(input("Enter:"))
b = float(input("Enter:"))
c = float(input("Enter:"))
if a == 0:
    print('error')
else:
    d = b**2 - 4*a*c 
    print (f'discriminant: {d}')
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f'two roots: {x1} & {x2}')
elif d == 0:
    x = -b/(2*a)
    print(f"one root: {x}")
else:
    print("There's no roots")
