#``Напиши программу, которая запрашивает у пользователя строку и выводит:
#Сколько в ней символов (используй len()).
#Есть ли в ней только цифры (.isdigit()).
#Переведи её в верхний регистр (.upper()).``
``☜(⌒▽⌒)☞``


s = (input("Enter:"))
for letter in s:
    print(letter)
print(len(s))
print(s.isdigit())
print(s.isupper())

num = int(input())
for i in range(num):
    if i % 3 == 0:
        print(i)
    else:
        print('no') 
