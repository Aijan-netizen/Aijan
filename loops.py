#loops while and for
print('while')
x = 0
while x < 3:
    print(f"meaning of x: {x}") 
    #берет значениe, без f результат будет просто {x}, с ним вместо скобок и икса идут индексы (0-2)
    x +=1 
    #увеличивает х на 1, без него цикл будет бесконенчым (будет только 0 без стопа)
    #+= увеличивает на 1, тк х<3 икс меньше трех
    #-= уменьшает на 1, при х>3 икс больше нуля
print()   

print('for')
for i in range(5): #numbers from 0 to 4
    print(i)
for letter in 'Hi':  
    print(letter)
#выводит каждую букву слова отдельно в список
for a in 'Hello': 
    print(a) 
#i, a, letter просто переменные
print()

print(' break')
for i in range(5):
    if i == 3:
        break #stop the loop when i would be 3. перветцикл, когда i бдует равно 3
    print(i)
print ()

x = 0
while x < 5:
    print ( x)
    x += 1 
    if x == 3:
        break
print()

print(' continue')
for i in range(5):
    if i == 2:
        continue # пропускает итерацию/повторение - здесь это цифра 2
    print(i)
print()

print(' else')
for i in range (4):
    print (i)
else:
    print("Цикл завершён без break")
print()

for i in range(5):
    print(i)
    if i == 1:
        break
else:
    print('Цикл завершился без else, так как уже есть break')
print()

n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print("Цикл завершен")
print()

n = 3
while n > 0:
    print (n)
    if n == 2:
        break
    n -=1
else:
    print('Цикл завершен без else, так как уже есть break')
print()

print("Зачем нужен else? пример:")
numbers = [1,3,5,7,9]
for a in numbers:
    if a == 4:
        print ("We find 4!")
        break
else:
    print("Don't find 4")
print("else сработал, потому что 4 в списке нет, и цикл завершился сам.Если бы 4 была в списке, break прервал бы цикл, и else не сработал бы.")
print()

print('вложенные циклы')   
for i in range(3):  # Внешний цикл
    for j in range(2):  # Внутренний цикл
        print(f"i={i}, j={j}")
print()

