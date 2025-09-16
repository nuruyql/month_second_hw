class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.__occupation = occupation
        self.__higher_edu = False
    def get_occupation(self):
        return self.__occupation
    def set_edu(self,higher_ed):
        self.__higher_edu = higher_ed


    def introduce(self):
        check_higher_ed = "higher education" if self.__higher_edu else "no higher education"
        return f"Hello, my name is {self.name}, I am {self.age} years old and I work as a {self.__occupation} , i have {check_higher_ed} "


class ClassMate(Person):
    def __init__(self, name, age, occupation, group_name):
        super().__init__(name, age, occupation)
        self.group_name = group_name

    def introduce(self):
        return f"{super().introduce()} and I am in group '{self.group_name}'."


class Friend(Person):
    def __init__(self, name, age, occupation, hobby):
        super().__init__(name, age, occupation)
        self.hobby = hobby

    def introduce(self):
        return f"{super().introduce()} My hobby is {self.hobby}."


# Создаем объекты
person1 = Person("Nurbol", 17, "Backend developer")
person1.set_edu(True)
person2 = ClassMate("Max", 17, "Frontend developer", "CS-101")
person2.set_edu(False)
person3 = Friend("Timur", 17, "Security developer", "Basketball")
person3.set_edu(False)

# Список всех объектов
people = [person1, person2, person3]

# Вызываем introduce для каждого объекта через цикл
for p in people:
    print(p.introduce())
