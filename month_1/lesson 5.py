# СЛОВАРИ - dict, МНОЖЕСТВА - set.
# {key: value}

# print(set('geeks'))

letter_1 = {'a', 'b', 'c'}
letter_2 = {'c', 'd', 'e'}

# print(letter_1.union(letter_2))
# print(letter_1.difference(letter_2))
# print(letter_1.intersection(letter_2))
# print(letter_1.symmetric_difference(letter_2))

# number_1 = [1, 2, 3, 2, 4, 1, 5, 3]
# number_2 = (1, 2, 3, 2, 4, 1, 5, 3)
# number_3 = {1, 2, 3, 2, 4, 1, 5, 3}

# print(type(number_3))
# print(number_1)
# print(number_2)
# print(number_3)

# student = {
#     'name': "adil'",
#     'age': 18
# }
# print(student)

# fruits_list = ['apple', 'lemon', 'cherry']
# fruits_dict = {'apple': 5, 'lemon': 0.5, 'cherry': 3}

# print(student.keys())
# print(student.values())
# print(student.items())
"""Вывод пар ключ:значение словаря"""
# dict_items([('name', "adil'"), ('age', 18)])
# for key, value in student.items():
#     print(f'{key} - {value}')

"""Вывод словаря в столбик"""
# for i in student:
#     print(f'{i}: {student[i]}')

"""add"""
# student['weight'] = 83
# student.update({'country': 'KG', 'height': 1.87})

"""edit"""
# student['age'] = 19

"""delete"""
# student.pop('country')
# del student['weight']

"""Доступ к значения словаря"""
# print(student.get('nam', 'нет такого ключа'))
# print(student['nam'])
# print(student['name'])
# print(student['age'])
# print(type(student))



















