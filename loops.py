#loops while and for
print('while')
x = 0
while x < 3:
    print(f"meaning of x: {x}") #берет значениe, без f результат будет просто {x}, с ним вместо скобок и икса идут индексы (0-2)
    x +=1 #увеличивает х на 1, без него цикл будет бесконенчым (будет только 0 без стопа)
print()   

print('for')
for i in range(5): #numbers from 0 to 4
    print(i)
for letter in 'Hi': #выводит какждую букву слова отдельно в список 
    print(letter)
for a in 'Hello': #i, a, letter просто переменные
    print(a) 
print()

#break, continue, else in loops
print('break, continue, else in loops')
for i in range(5):
    if i == 3:
        break #stop the loop when i would be 3. перветцикл, когда i бдует равно 3
    print(i)
print ()

for i in range(5):
    if i == 2:
        continue # пропускает итерацию/повторение - здесь это цифра 2
    print(i)
print()

for i in range(3):
    print(i)
else:
    print("Цикл завершился без break")  # выполняется, если цикл не завершился через break
print()
 
