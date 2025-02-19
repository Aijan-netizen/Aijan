# Calculator
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