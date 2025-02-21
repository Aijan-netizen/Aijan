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
a = '12345'
print(a.isdigit()) #ТОЛЬКО из цифр (0-9) - True
print(a.isalpha()) #только из букв (a-z, A-Z) - False
print(a.islower()) #все буквы в нижнем регистре (a-z) - False
print(a.isspace()) #Только пробелы - False
print(a.isalnum()) #Только буквы + цифры (без пробелов и знаков) - True(даже если там только буква или только цифра всегда True)
print(a.isupper()) #Все буквы в верхнем регистре - False
print(a.istitle()) #Каждое слово с заглавной буквы - False

a = 'A'
print(a.isalnum()) #Только буквы + цифры (без пробелов и знаков) - True

print('Цикл for по строке')
s = "Python"
for letter in s: 
#перебор каждый символ с новой строки в столбик
    print(letter)

print('Подсчёт количества символов:')
s = "Привет, мир!"
количество = len(s) 
#len(s) возвращает длину строки (то есть количество символов)
print(количество)  
# 12




