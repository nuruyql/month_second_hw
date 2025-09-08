# операторы : принадлежности,назначение.цыклы

# in
# print("Y" in "python")



#ОПЕРАТОРЫ ПРИНАДЛЕЖНОСТИ
# number = 5
# number += 4
# number -= 6
# number **= 4
# print(number)

# counter = 0
# while counter < 100:
#     counter += 1
#     if counter == 20:
#         continue
#     if counter == 50:
#         break
#     print(counter)
# word = "gssassayman"
# for letter in word:
#     if letter == "y":
#         continue
#     if letter == "a":
#         break
#     print(letter)
#
# cash = 100
# percents = 0.1
# years = 4
# for  year in range(1, years +1):
#     cash += cash * percents
#     cash = round(cash,2)
#     print(f"{year} {cash}")
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# consonants = [
#     'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
#     'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
# ]
#
# while True:
#     word = input("enter any word: ")
#     if word.lower() == "stop":
#         break
#     if not word.isalpha():
#         print("please enter exactly  word")
#         continue
#     letters = 0
#     consonants_count = 0
#     vowels_count = 0
#     uppercase_count = 0
#     lowercase_count = 0
#
#
#     for letter in word:
#         if letter.isalpha():
#             letters += 1
#         if letter.lower() in vowels:
#             vowels_count+=1 #and vowels_count / word *100
#         elif letter.lower() in consonants:
#             consonants_count+=1 #and consonants_count / word *100
#         if letter.isupper():
#             uppercase_count += 1
#         elif letter.islower():
#             lowercase_count += 1
#     vowel = vowels_count / letters * 100
#     consonant = consonants_count / letters * 100
#
#
#     print(f"Vowels: {vowels_count}")
#     print(f"Consonants: {consonants_count}")
#     print(f"Uppercase letters: {uppercase_count}")
#     print(f"Lowercase letters: {lowercase_count}")
#     print(f"Letters: {letters}")
#     print(f"vowels: {vowel}%,"
#           f"consonants: {consonant}")
#














