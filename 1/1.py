#  ЗАДАНИЕ 1
#  Нужно создать список учеников (их фамилии <придумай сам>).
#  Создать второй список с их средним баллом (от 1.00 до 4.99), где индекс ученика
#  соответсвует индексу его оценки <придумай сам
surnames = ['John', 'Smith', 'Mikhail']
marks = [3.99,4.51,4.9]


#  ЗАДАНИЕ 2
#  Добавить каждому ученику по 0.01 баллу
for mark in range(len(marks)):
    marks[mark] += 0.01
print(marks)

#  ЗАДАНИЕ 3
#  Вычесть у 4ого ученика 0.5 балла
marks[2] -= 0.5
print(marks)
#  ЗАДАНИЕ 4
#  Добавить нового ученика и средний его балл <придумай сам
surnames.append("Nikita")
marks.append(5)
print(surnames, marks)
