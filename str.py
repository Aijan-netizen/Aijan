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

s = "hello world"
print(s.upper()) 
# HELLO WORLD
print(s.replace("world", "Python"))
# hello Python
print(s.split())
# ['hello', 'world']
print()

s = "I am fine"
print(s.upper())
#I AM FINE
print(s.replace("fine", "good"))
#I am good
print(s.replace("am", "am not okay right now"))
#I am not okay right now fine
print(s.split())
#['I', 'am', 'fine']
