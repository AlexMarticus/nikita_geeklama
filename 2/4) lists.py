#два str один int один float один bool один list один tuple
# Создайте пустой список, определите его тип и выведите в консоль.
answer_1= ["apple", "ban", 1, 2.5, False, [], () ]
print(type(answer_1[-1]))
# требуемый вывод:
# <class 'list'>

# Допишите код, чтобы gift_list был заполненным кортежем. Порядок элементов значения не имеет.
gift_list= ("Камера", "Наушники", "Часы")
print(gift_list)
# требуемый вывод:
# ("Камера", "Наушники", "Часы")


# Создай список, внутри которого будет другой список

spisok = [[[()]]]
print(spisok)


# Создай кортеж, внутри которого будут: 1) кортеж, 2) список, 3)целое число

ftvy = ((), [], 4) 


# Допишите код, что бы вывести последний элемент списка.
sample = ["abc", "xyz", "aba", 1221]
# требуемый вывод:
# 1221
print(sample[3], sample[-1])


# Допишите код, что бы вывести расширенный список.
sample = ["Green", "White", "Black"]
#sample.append("Red")
#sample.append("Pink")
#sample.append("Yellow")
sample.insert(0, "Red")
sample.extend(("Pink", "Yellow"))
print(sample)
# требуемый вывод:
# ["Red", "Green", "White", "Black", "Pink", "Yellow"]

# Исправьте ошибки в коде, что бы посчитать сумму элементов в списке.
sample = [11, 33, 50]
print(sum(sample))
# требуемый вывод:
# 94
