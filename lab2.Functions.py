import functools

# 1.	Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
# print(squared)
"""
map()
Функция вызывается со всеми элементами в списке,
и в результате возвращается новый список,
содержащий элементы, возвращенные
данной функцией для каждого исходного элемента
"""

items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, items))
print("Задание 1. \n"
      "          Используя функцию map() переписать функцию \n")
print("Дано: ", items)
print("Результат: ", squared)


###################################################################
# 2.	Используйте функцию reduce() и перепишите код
# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
# print(product)
"""
reduce(function, iterable[, initializer])
Функция reduce() модуля functools кумулятивно
применяет функцию function к элементам итерируемой
iterable последовательности, сводя её к единственному значению
initializer - начальное значение.
"""

product_list = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, product_list, 1)
print("Задание 2. \n"
      "          Используйте функцию reduce() и перепишите код \n")
print("Результат: ", product)


#####################################################################
#3.	Используйте функцию map() и перепишите код
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
"""
map()
Функция вызывается со всеми элементами в списке,
и в результате возвращается новый список,
содержащий элементы, возвращенные
данной функцией для каждого исходного элемента
"""

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Задание 3. \n"
      "          Используя функцию map() перепишите код \n")
print("Результат: ", squared)


#####################################################################
# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
"""
Функция zip() используется для совмещения двух и более списков в один.
Она возвращает итератор кортежей, где i-ый кортеж
содержит i-ый элемент из каждого из переданных списков.
"""

x = [1, 2, 3]
y = [4, 5, 6]
a = list(zip(x,y))
print("Задание 4. \n"
       "          Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip() \n")
print("Список x: ", x)
print("Список y: ", y)
print("Результат: \n ", a)



#####################################################################
# 5.	Используйте функцию zip() чтобы преобразовать код:
#
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
#

name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

Name = list(zip(name_hero, name_real))
print("Задание 5. \n"
       "          Используйте функцию zip() чтобы преобразовать код \n")

print("Результат: ")
for i in range(len(Name)):
    print(f"{i + 1}. {Name[i][0]} is {Name[i][1]}")


#####################################################################
# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# нечетные элементы в новый список.
"""
Функция вызывается со всеми элементами в списке, 
и в результате возвращается новый список, 
содержащий элементы, для которых функция результирует в True
"""

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
new_list = list(filter(lambda x: x % 2 != 0, numbers))

print("Задание 6. \n"
       "          С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] \n"
       "          нечетные элементы в новый список. \n")
print("Список numbers: ", numbers)
print("Результат (Список new_list): ", new_list)