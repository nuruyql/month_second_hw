# import datetime
#
# class Person:
#     def __init__(self, name, birth_date, occupation):
#         self.name = name
#         self.__birth_date = birth_date  # приватный атрибут
#         self.__occupation = occupation
#         self.__higher_edu = False
#
#     @property
#     def age(self):
#         today = datetime.date.today()
#         # вычисляем возраст на основе даты рождения
#         years = today.year - self.__birth_date.year
#         # уменьшаем на 1, если день рождения ещё не наступил в этом году
#         if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
#             years -= 1
#         return years
#
#     @property
#     def occupation(self):
#         return self.__occupation
#
#     def get_edu(self):
#         return self.__higher_edu
#
#     def set_edu(self, higher_ed):
#         self.__higher_edu = higher_ed
#
#     def introduce(self):
#         check_higher_ed = "higher education" if self.__higher_edu else "no higher education"
#         return (f"Hello, my name is {self.name}, I am {self.age} years old and I work as a {self.__occupation}, "
#                 f"I have {check_higher_ed}, my birth date is {self.__birth_date}")
#
#
# class ClassMate(Person):
#     def __init__(self, name, birth_date, occupation, group_name):
#         super().__init__(name, birth_date, occupation)
#         self.group_name = group_name
#
#     def introduce(self):
#         return f"{super().introduce()} And I am in group '{self.group_name}'."
#
#
# class Friend(Person):
#     def __init__(self, name, birth_date, occupation, hobby):
#         super().__init__(name, birth_date, occupation)
#         self.hobby = hobby
#
#     def introduce(self):
#         return f"{super().introduce()} My hobby is {self.hobby}."
#
#
# # Создаем объекты с датой рождения
# person1 = Person("Nurbol", datetime.date(2006, 5, 10), "Backend developer")
# person1.set_edu(True)
#
# person2 = ClassMate("Max", datetime.date(2003, 4, 20), "Frontend developer", "CS-101")
# person2.set_edu(False)
#
# person3 = Friend("Timur", datetime.date(2006, 3, 15), "Security developer", "Basketball")
# person3.set_edu(False)
#
# # Список всех объектов
# people = [person1, person2, person3]
#
# # Вызываем introduce для каждого объекта через цикл
# for p in people:
#     print(p.introduce())

# class Person:
#     def __init__(self, name, age):  # исправлено
#         self.name = name      # публичный
#         self._age = age       # защищённый (protected)
#
#     def display_info(self):
#         print(f"Имя: {self.name}, Возраст: {self._age}")
#
# class Student(Person):
#     def birthday(self):
#         self._age += 1        # можно изменять защищённый атрибут в наследнике
#         print(f"С Днем Рождения! Возраст теперь {self._age}")
#
#
# # Использование
# p = Person("Alice", 20)
# p.display_info()           # Имя: Alice, Возраст: 20
#
# s = Student("Bob", 18)
# s.birthday()               # С Днем Рождения! Возраст теперь 19




from dataclasses import dataclass,field


@dataclass
class Person:
    name: str
    __occupation: str
    __higher_education: bool = field(default=False)

    def introduce(self):
        check_higher_ed = "higher education" if self.__higher_education else "no higher education"
        return (f"My name is {self.name},"
                f"i work as {self.__occupation}"
                f"i have {check_higher_ed}"
                )
    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education

class Classmate(Person):
    def __init__(self,name,occupation,group_name):
        super().__init__(name,occupation)
        self.group_name = group_name
    def introduce(self):
        return f"{super().introduce()} and my group is {self.group_name}"


class Friend(Person):
    def __init__(self,name,occupation,hobby):
        super().__init__(name,occupation)
        self.hobby = hobby
    def introduce(self):
        return f"{super().introduce()} and my hobby is {self.hobby}"
class BestFriend(Friend):
    def __init__(self,name,occupation,hobby,shared_memory):
        super().__init__(name,occupation,hobby)
        self.shared_memory = shared_memory
    def introduce(self):
        return f"{super().introduce()} and i remember about our {self.shared_memory}"




classmate1 = Classmate("Nurbol","Backend Developer","CS24-12")
classmate1._Person__higher_education = True
classmate2 = Classmate("Aktan","Frontend Developer","CS24-14")
friend1 = Friend("Maxim","Frontend Developer","skiing")
friend2 = Friend("Timur","Backend Developer","mobile games")
best_friend = BestFriend("Muhammed","Dentist","football","first meeting")
introduce_object = [classmate1,classmate2,friend2,friend1,best_friend]
for i in introduce_object:
    print(i.introduce())
