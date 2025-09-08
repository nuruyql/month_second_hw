# lambda функции, обработка исключений.
# stude = ["","","",""]
from traceback import print_tb


# def show_words(func,words):
#     for word in words:
#         print(func(word))
# show_words(
#     lambda word: word.title(),words:['migas','blue','delte']
# )



# students = ('feol','red','veriab','fear')
#
# map_students = list(map(lambda name: name.tite(),students))
#
# filter_students = list(filter(lambda name: 'e' '''not'''in name,students))
#
# sorted_students = sorted(students, key=lambda name:name.count('e'), reverse=True)
# intersection()

# adil = ['kyrgyz','english','turkish','russian']
# alim = ['kyrgyz','kazah','russian']
#
#
# # same_lang = list(set(adil) & set(alim))
# print(adil.)


# lambda_exampl = lambda number: number + 15
# print(lambda_exampl(23))
# an_num = int(input("any number: "))
# multi_num = lambda *args: filter([x * an_num for x in args])
#
# print(multi_num(2,3,4))


# a = [2, 3, 4, 5]
# b = [3, 4, 5, 8]
#
# result = sum(map(lambda x, y: x + y, a, b))
# print(result)

def get_element(*args):
    print(f"Работаем со списком: {args}")
    print("Введите индекс элемента или 'exit' для выхода:")

    while True:
        user_input = input("Индекс: ")

        if user_input.lower() == "exit":
            break

        try:
            index = int(user_input)
            print(f"Элемент с индексом {index}: {args[index]}")
        except ValueError:
            print(" нужно ввести число или 'exit'.")
        except IndexError:
            print(f"Индекс вне диапазона,accebtable индексы: от 0 до {len(args) - 1}")
print(get_element(2,3,4,5,6,7,8,8,6))


# def nearest_number(iterable, target):
#     sorted_list = sorted(iterable, key=lambda x: abs(x - target))
#     return target, sorted_list
#
# nums = [10, 5, 30, 25, 8]
# target = 20
#
# print(nearest_number(iterable=nums, target=target))
#Напиши функцию squares(numbers), которая принимает список чисел и возвращает новый список их квадратов с помощью map и lambda.

# def squares(*args):
#     return list(map(lambda x : x**2,args))
#
# print(squares(2,3,4,5,6))

# def even_num(*args):
#     return list(filter(lambda x :x % 2 ==0,*args))
# print(even_num(2,3,4,5,6,7,8))



#
# def multiply_by(*args):
#     return list(map(lambda x : x * 2,args))
# print(multiply_by(2,3,4))

# def division(numbers,n):
#     return sum(filter(lambda x : x > n,numbers))
# print(division([2,3,4,5,6,7,8,4,5],3))
#
# def closest_to_average(*args):
#     avg = round((args) / len(args),2)
#     sorted_list = sorted(args, key=lambda x: abs(x - avg))
#     return avg, sorted_list
# print(closest_to_average(3,4,5,6,7,7))

