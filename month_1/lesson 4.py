# списки,кортежи.индексы и срезы.
# встроенные функции к набором
# списковые включение list comprehension
from os import remove

#  списки,индексы
# students = ['nurs',"era","nurgijit",'dod']
# # print(students)
# # print(students[0])
# # print(students[1])
# # print(students[-1])
# # print(students[2][3])

# срезы
students = ['nurs',"era","nurgidfajit",'dod']
# print(students[:2])
# print(students[-2:])
# print(students[1:3])
# print(students[::-1])
# print(students[2][:3] + students[2][-3:])
# print(students[1][::-1])


#add function
# students = ['nurs',"era","nurgijit",'dod']
# students.append('rayly')
# students.insert(1 ,'hokey')
# students.extend(['gogo','sisi'])
# students += ['alena','albert']


#edit function
# students = ['nurs',"era","nurgijit",'dod']
# students.sort()
# students.sort(reverse=True)
# students.reverse()
# students[2] = 'uali'
# students.sort(key=len)
# students = [student.title() for student in students]#list comprehension
# print(students)

#delete function
# students = ['nurs',"era","nurgijit",'dod']
# students_copy = students.copy()
#
# # students.remove('dod')
# # deleted = students.pop(0)
# # print(deleted)
# # del students[-1]
# # students.clear()
# # print(students)
#
# print(students_copy)


#Операторы
# numbers = [1,2,3,4,5,6,7,8,9,]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers))
# print(len('geeks'))

# numberss = (34,)
# print(type(numberss))
# number = 1,2,3,4,5,5,6
# print(type(number))

# number  = 34,
# number = list(number)
# number = tuple(number)
#
# print(number)






#
#
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
#
# letters = []
# numbers = []
#
# for item in data_tuple:
#     if isinstance(item, str):
#         letters.append(item)
#     else:
#         numbers.append(item)
#
# numbers.remove(6.13)
# numbers.remove(True)
# letters.append(True)
#
# index_3 = numbers.index(3)
# numbers.insert(index_3 + 1, 2)
# numbers.sort()
#
# letters.reverse()
# letters_fixed = []
# for item in letters:
#     if isinstance(item, str):
#         letters_fixed.append(item.title())
#     else:
#         letters_fixed.append(item)
# letters = letters_fixed
#
# numbers = [x**2 for x in numbers]
#
# letters = tuple(letters)
# numbers = tuple(numbers)
#
# print(letters)
# print(numbers)















