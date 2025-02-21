s1 = 'Hi'
s2 = "Python"
print(s1,s2)
print()

s = 'Python'
print(s[0])
print(s[-1])
print()

s = 'Programming'
print(s[:5])
print(s[2:5])
print(s[::-1])
print()

s = "hello world"
print(s.upper())
print(s.replace("world", "Python"))
print(s.split())
print()

s = "I am fine"
print(s.upper())
print(s.replace("fine", "good"))
print(s.replace("am", "am not okay right now"))
print(s.split())



# str строки
s1 = 'Hi'
s2 = "Python"
print(s1,s2)
print()

s = 'Python'
print(s[0]) # выведит первый символ, т.е. первую букву в это слове 
# P
print(s[-1]) # выводит последний символ, т.е. послежнюю букву 
# n
print()

# Срезы строк (slicing) - Срез позволяет взять часть строки.
# Формат - строка[начало:конец:шаг]

s = 'Programming'
print(s[:5]) # с первого до пятого индекса
# Progr 
print(s[2:5]) # с 2 по 4
# ogra
print(s[::-1]) # отзеркалено
# gnimmargorP 
print()

# Методы строк

print("Изменение регистра")
s = "Hello world"
print(s.upper()) 
# HELLO WORLD
print(s.lower())  
# "hello world"
print(s.title())  
# "Hello World" 
print(s.replace("world", "Python"))
# Hello Python
print(s.split())
#['Hello', 'world']
print()

print("Замена и удаление пробелов")
s = "  Python  "
print(s.replace(" ", "_"))  
# "__Python__"
print(s.strip())
# Python - удаляет пробелы с обеих сторон 

s = "I am fine"
print(s.replace("fine", "good"))
#I am good
print(s.replace("fine", "not okay right now"))
#I am not okay right now

print("Разделение и объединение")
print(s.split(","))
#['I am fine']
b = ["Your", "room","is","clean"]
print(" ".join(b))
#Your room is clean

a = "It's okay to not be okay"
print(a.find("okay"))
# 5 - ищет первое вхождение "okay" в строке a - индекс.
#Если "okay" не найдено, .find() вернёт -1.
print(a.count('o'))
#4 - сколько раз встречается "о".

print('Проверка содержимого')



