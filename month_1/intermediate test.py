#first task
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# try:
#     expenses = [float(input(f"Enter your expenses for {day}: ")) for day in days]
#
#     total = sum(expenses)
#     average = total / len(days)
#
#     if 1 <= average <= 200:
#         print("Your average is small")
#     elif 201 <= average <= 500:
#         print("Your average is middle")
#     elif average > 500:
#         print("Your average is big")
#     else:
#         print("You spent nothing")
#
#     print(f"All expenses for week: {total}")
#     print(f"Average per day: {round(average, 2)}")
#
# except ValueError:
#     print("Please enter numbers only!")




# colors = ['red','green','yellow']
#
# while True:
#     color = input("enter the color of traffic: ").lower()
#     if color == "stop":
#         print("you left")
#         break
#     if color not in colors:
#         print(f"enter accepted colors \naccepted colors: {colors}")
#         continue
#     if color == colors[0]:
#         print("stop!")
#     elif color == colors[1]:
#         print("go on")
#     elif color == colors[2]:
#         print("move little bit")
#     else:
#         print("have a good evening")




#second task
# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
#
# designations = []
# codes = []
#
# for item in data:
#     if item.isdigit():
#         codes.append(item)
#     else:
#         designations.append(item)
#
# print("Designations:", designations)
# print("Codes:", codes)
# operatos = dict(zip(designations ,[ {item} for item in codes]))
#
# for bad in ["Fonex","Katel"]:
#     operatos.pop(bad,None)
# operatos["O!"].add("0999")
# operatos["Megacom"].add("0555")
# operatos["Beeline"].add("0777")
#
# for designations, codes in operatos.items():
#     print(f"{designations} - {codes}")