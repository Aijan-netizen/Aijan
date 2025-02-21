name = "Aijan"
age = "19"
print (f"My name is {name}. I'm {age} years old.")
#My name is Aijan. I'm 19 years old.

a = float(input('Enter the num: '))
b = float(input('Enter the num: '))
print(f"Sum of the {a} & {b} equals to: {a+b} ")
#Sum of the 67.0 & 89.0 equals to: 156.0

print(f"Next year:{2025+1}")
#Next year:2026

print(f"Letters in 'спиноцеребеллярная атаксия': {len('спиноцеребеллярная атаксия')}")
#Letters in 'спиноцеребеллярная атаксия': 26 - кол-во букв в слове

print("Округление чисел")
pi = 3.1415926535
# ._f – округляет число до _ символов после запятой.
print(f"Number (¬‿¬):{pi:.4f}") 
#Number (¬‿¬):3.1416
print(f"Number ((❁´◡`❁)):{pi:.2f}") 
#Number (¬‿¬):3.1416

print('Вывод чисел в процентах')
accuracy = 0.9876
print(f"accuracy:{accuracy:.5%}")
#accuracy:98.76000%
print(f"accuracy:{accuracy:.1%}")
#accuracy:98.8%

print('Выравнивание текста')
print(f"|{'Python':^10}|")  # Выравнивание по центру
print(f"|{'Python':<10}|")  # Выравнивание налево
print(f"|{'Python':>10}|")  # Выравнивание направо

print('Строки f с циклами')
for i in range(0,12): #12 примеров (с умножения на 0 до 11)
    print(f" 2 х {i} = {2*i}") # 2 х 0 = 0

