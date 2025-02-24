#1️⃣.tuple - Кортежи 
print('Tuple')
my_tuple = (1,2,3,'hello')
print(my_tuple[0])  #1
print(my_tuple[-1]) #hello
print(my_tuple[-3]) #2
print(my_tuple[1])  #2
print(len(my_tuple))#4 - длина кортежа
print()

# Распаковка кортежа
a,b,c,d = my_tuple
print(a,d) # 1 hello
print(b,c) #2 3
print()

# Соединение кортежей
tuple1 = (1,2,3)
tuple2 = (4,5,6)
new_t = tuple1 + tuple2
print(new_t) #(1, 2, 3, 4, 5, 6)
print()


#2️⃣.set - Множества 
print('Set')
my_set = {1,2,3,4,5,6,6,6,7,8,9}
print(my_set) # {1,2,3,4,5,6,7,8,9}
print()

#Добавление элемента
my_set.add(0)
print(my_set)# {0,1,2,3,4,5,6,7,8,9}
print()

# Удаление элемента
my_set.remove(3) #Удаляет, но если элемента нет — ошибка
my_set.discard(7) #Удаляет, если есть, иначе просто пропускает
print(my_set)
#{0,1,2,4,5,6,8,9}
my_set.remove(3) #KeyError: 3
my_set.discard(7)#ничего не вывело - даже если нет даноого жлемента, просто пропускает
my_set.pop() #{2,4,5,6,8,9} - удаляет случайный элемент - чаще первый 
print(my_set)
print()

# Проверка наличия элемента
print(2 in my_set) #True
print(10 in my_set) #False
print()

#🔄 Операции с множествами
set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,0}

print(set1 | set2)# Объединение (union)
#{0,1,2,3,4,5,6,7,8,9}
print(set1 & set2)# Пересечение (intersection)
#{5,6}
print(set1 - set2)# Разность (difference)
#{1,2,3,4}
print(set1 ^ set2)# Симметричная разность (XOR)
#{0,1,2,3,4,7,8,9}


#3️⃣.dictionary - Словари 
my_dict = {
    "name": "Aijan",
    "age":"19",
    "city":"Bishkek"
    }
    
# Доступ к значениям
print(my_dict["name"]) #Aijan
print()

# Добавление нового ключа
my_dict["job"] = "Student"
print()

# Изменение значения
my_dict["age"] = "19"
print()

# Удаление элемента
del my_dict["city"]
print()

# Проверка наличия ключа
print("age" in my_dict) #True
print()

# Получение всех ключей и значений
print(my_dict.keys()) #dict_keys(['name','age','job'])
print(my_dict.values()) #dict_values(['Aijan','19','Student'])
print()

#🔄 Объединение словарей 
dict1 = {"a":1, "b":2, "c":7}
d2 = {"c":3, "d":4, "a":9}

merged = {**dict1, **d2}
print(merged)
#{"a":1, "b":2, "c":3, "d":4} - (если есть одинаковые ключи, то берётся значение из второго словаря)


#4️⃣.List comprehensions - Генераторы списков 
# Позволяют быстро создавать списки на основе других коллекций.
#📌 Обычный способ:
num = []
for i in range (10):
    num.append(i*2)
print(num) ## [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#📌 Генератор списков:
n = [i * 2 for i in range (10)]
print(n)# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

n = [1* 2 for i in range (10)]
print(n)#  [2,2,2,2,2,2,2,2,2,2] - случайный вывод

#🔹 Генератор с условием:
e = [i for i in range(10) if i % 2 == 0]
print(e) #[0,2,4,6,8]

#🔹 Генератор для словаря:
squares = {i: i**2 for i in range(5)}
print(squares) #{0:0, 1:1, 2:4, 3:9, 4:16}



























