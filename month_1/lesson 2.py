#Логический тип данных.Операторы: условные,сравнение,логические.
# counter = int(input("enter your attemps: "))
# while counter > 0:
#     time = input("enter date: ").strip().lower().upper()
#     if time == "stop":
#         break
#     if  time == "day":
#         print("good day")
#     elif time == "morning":
#         print("good morning")
#     elif time == "evening":
#         print("good evening")
#     else:
#         print("hello")
#     counter -=1
#     print(f"you have {counter} attemps ")



while True:
    birthmonth = int(input("Enter your birth month (1-12): "))
    birthday = int(input("Enter your birthday (1-31): "))
    if birthmonth == 100:
        break
    if (birthmonth == 12 and birthday >= 22 ) or (birthmonth == 1 and birthday <= 19):
        print("You are Capricorn (Kozerog)")
    elif (birthmonth == 1 and birthday >= 20) or (birthmonth == 2 and birthday <= 18):
        print("You are Aquarius (Vodoley)")
    elif (birthmonth == 2 and birthday >= 19) or (birthmonth == 3 and birthday <= 20):
        print("You are Pisces (Ryby)")
    elif (birthmonth == 3 and birthday >= 21) or (birthmonth == 4 and birthday <= 19):
        print("You are Aries (Oven)")
    elif (birthmonth == 4 and birthday >= 20) or (birthmonth == 5 and birthday <= 20):
        print("You are Taurus (Telec)")
    elif (birthmonth == 5 and birthday >= 21) or (birthmonth == 6 and birthday <= 20):
        print("You are Gemini (Bliznecy)")
    elif (birthmonth == 6 and birthday >= 21) or (birthmonth == 7 and birthday <= 22):
        print("You are Cancer (Rak)")
    elif (birthmonth == 7 and birthday >= 23) or (birthmonth == 8 and birthday <= 22):
        print("You are Leo (Lev)")
    elif (birthmonth == 8 and birthday >= 23) or (birthmonth == 9 and birthday <= 22):
        print("You are Virgo (Deva)")
    elif (birthmonth == 9 and birthday >= 23) or (birthmonth == 10 and birthday <= 22):
        print("You are Libra (Vesy)")
    elif (birthmonth == 10 and birthday >= 23) or (birthmonth == 11 and birthday <= 21):
        print("You are Scorpio (Skorpion)")
    elif (birthmonth == 11 and birthday >= 22) or (birthmonth == 12 and birthday <= 21):
        print("You are Sagittarius (Strelec)")
    else:
        print("Invalid date")
#

# user_input = input("Введите число: ")
#
# try:
#     number = int(user_input)
#     if number > 0:
#         print(f"{number} — положительное число")
#     elif number < 0:
#         print(f"{number} — отрицательное число")
#     else:
#         print("Вы ввели ноль")
# except ValueError:
#     print("Ошибка: введено не число. Пожалуйста, введите целое число.")



# age = int(input("enter any number: "))
# name = input("enter your name: ")
#
# aft1 = age + 10
#
# print(f"{name} will be {aft1} years old after 10 years")
















