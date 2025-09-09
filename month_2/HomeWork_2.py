class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I work as a {self.occupation}"


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
person2 = ClassMate("Max", 17, "Frontend developer", "CS-101")
person3 = Friend("Timur", 17, "Security developer", "Basketball")

# Список всех объектов
people = [person1, person2, person3]

# Вызываем introduce для каждого объекта через цикл
for p in people:
    print(p.introduce())
