numbers = [1,2,3,4,5]
print(numbers[2]) # 3 (индексация с 0)
print(numbers[1]) # 2 (индексация с 0)
print(numbers[0]) # 1 (индексация с 0)

numbers.append(6) # Добавляет 6 в конец списка
print(numbers) 
# [1, 2, 3, 4, 5, 6]

numbers.remove(1) #удаляет цифру 1 
print (numbers)
# [2, 3, 4, 5, 6]

numbers = [1,2,3,4,5]
numbers.pop(1) #удаляет цифру, под индексом 1
print (numbers)
# [1, 3, 4, 5]

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    print(num)
#список цифр в столбик 

numbers.sort()  # Сортирует список
print (numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()  # Отзеркаливает список
print (numbers)
#[9, 8, 7, 6, 5, 4, 3, 2, 1]
