# first variation of code
a = float(input('Enter the number'))

if a % 3 ==0  and a % 5==0:
    re = "Divisible by both 3 and 5"
elif a % 3 ==0 and a % 5 !=0:
    re = "Divisible by 3"
elif a % 5==0 and a % 3 != 0:
    re = "Divisible by 5"
else:
    re = "Not divisible by 3 or 5"
print(re)  
print()

# second variation of code
a = int(input('Enter the number: '))  

if a % 3 == 0 and a % 5 == 0:
    re = "Divisible by both 3 and 5"
elif a % 3 == 0:
    re = "Divisible by 3"
elif a % 5 == 0:
    re = "Divisible by 5"
else:
    re = "Not divisible by 3 or 5"
print(re)
