#workout1
print ('workout1')
a = int(input())
b = int(input())
print(a+b) # сложение
print(a-b) # вычитание
print(a*b) # умножение
print(a/b) # деление
print(a//b) # деление бзе остатка - целое число
print(a%b) # остаток от деления
print(a**b) # степень
print(a!=b) #сравнение
print()

# workout2
print ('workout2')
x = 5
y = 5
if x == y:
    result = True
else:
    result = False
print(result)
print()

#workout3
print ('workout3')
x = int(input())
if x == 5.0:
    print(True)
else:
    print(False)
    
#Assignments
print("Assignments")

#Calculator1
print ('Calculator1')
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
operation = input("Enter the operation (+,-,*,-,//,**,%):")
if operation == "+":
    result = a+b 
elif operation == "-" :
    result = a-b
elif operation == "*":
    result = a*b
elif operation == "/":
    if b != 0:
        result = a/b 
    else:
        result = "Error. no deleting to 0"
elif operation == "//":
    if b!= 0:
        result = a//b
    else:
        result = "Error"
elif operation == "%":
    if b!= 0:
        result = a%b 
    else:
        result = "Error"
elif operation == "**":
    result = a ** b 
else: 
    result = "Error"
print (result)
print()

#Calculator2
print ('Calculator2')
num = int(input("Enter the number:"))
if num % 2 == 0:
    print ("четное")
else:
    print("нечетное")

