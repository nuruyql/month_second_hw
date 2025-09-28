# контексный мененджер "with",работа с файлами
# w - write (rewrite all)
# a - add
# x - check do we have the same names of files
from traceback import print_tb


# file = open("google","a",encoding="utf")
# file.write("asd")
# file.close()

# with open("google",'w') as file:
#     file.write("\nnew file,new date")
# with open("google",'x') as file:
#     file.write("\nnew file,new date")

#
# with open('new_file.txt','a') as file:
#     file.write('new file,new date')
#
# with open('new_file.txt','r',encoding='utf-8') as file:
#     print(file.read())
# from time import sleep
# with open('google','r',encoding='utf-8') as file:
#     for symbol in file.read():
#         print(symbol,end='')
#         if symbol == ' ':
#             continue
#         sleep(1)
#
#
#
#
# def guess_number():
#     low=1
#     high =100
#     attempts = []
#     count = 0
#
#     while True:
#         guess = (low + high) // 2
#         attempts.append(guess)
#         count += 1
#
#         print(f"Твое число {guess}?")
#         answer = input("Ответь: да / больше / меньше: ").strip().lower()
#
#         if answer == "да":
#             print(f"Я угадал число {guess} за {count} попыток!")
#             # записываем в файл
#             with open("results.txt", "a", encoding="utf-8") as f:
#                 f.write(f"Загаданное число: {guess}, Количество попыток: {count}, Попытки: {attempts}\n")
#             break
#         elif answer == "больше" or answer == "more":
#             low = guess + 1
#         elif answer == "меньше" or answer == "little":
#             high = guess - 1
#         else:
#             print("Некорректный ввод. Введи: да / больше / меньше")
#
# guess_number()
#
#
#
# def check_even(num):
#     if num % 2 == 0:
#         return "Чётное"
#     else:
#         return "Нечётное"
#
# print(check_even(4))
#
#
# def le_sym(symbols):
#     return len(symbols.replace(" ",""))
# print(le_sym("asd asd"))
#
#
#
#
# def nearest_number(numbers, target=0):
#     if not numbers:
#         return None
#
#     return min(numbers, key=lambda x: abs(x - target))
# numbers = []
# for i in range(3):
#     numbe = float(input("enter any num: "))
#     numbers.append(numbe)
# target = float(input("Enter target number: "))
# print(nearest_number(numbers,target))
# a = 34
# b = str(a)
# f =a + b
# print(f)




# array = [1,2,3,4,5,6,7,8,9]
# k = 7
# def ads(array,k):
#     for i in range(len(array)):
#         if array[i] == k:
#             return k
#     return None
# ads(array,k)

# numbers = [1,2,3,4,52,22]
# index = 2
# def find_index(numbers,index):
#     return numbers[index]
# print(find_index(numbers,index))


# def even_ood(num):
#     return num % 2 == 0
#
# print(even_ood(5))

# def last(num=[2,3,4,5,5,6]):
#     return num[-1]
# print(last())


# def we_have(num=[2,3,4,5,6,7]):
#     return x in num
# x = 3
# print(we_have())

# def sums(num = [2,3,44,4,4,4,5,6,6]):
#     defe = 4
#     fout = 0
#     for i in num:
#         if i == defe:
#             fout +=1
#     return fout
# print(sums())


arr =[7, 3, 5, 1, 9]
i = arr[0]
for n in arr :
    if n < i:
        i = n
print(i)























