#кортеж занимает намного меньше памяти чем список

# Присвойте переменной целое число и получите вывод <class 'int'>.
current_month = "4"
type_var = type(current_month)
print(type_var)
# требуемый вывод:
# <class 'int'>

# Исправьте ошибки в коде, что бы получить требуемый вывод.
polar_radius_title = "Радиус Земли"
polar_radius_float = 6378.1
print(polar_radius_title, polar_radius_float)
# требуемый вывод:
# Радиус Земли 6378.1

# Создайте переменные, что бы получить требуемый вывод.
str_type, int_type, float_type, bool_type = "100", 2, 2.5, True
print("Типы данных: ", end="\n")
print(type(str_type), type(int_type), type(float_type), type(bool_type), sep=" - ")
# требуемый вывод:
# Типы данных: <class 'str'>, <class 'int'>, <class 'float'>, <class 'bool'>


# Измените и дополните код, что бы переменная salary_type хранила результат функции type() со значением int.
salary = '50000'
salary_type = type(int(salary))
print(salary_type)
# требуемый вывод:
# <class 'int'>

# Исправьте ошибку в коде, что бы получить требуемый вывод.
# данный код
mark = int("5")
print(f"{mark}+ баллов")
# требуемый вывод:
# 5+ баллов
