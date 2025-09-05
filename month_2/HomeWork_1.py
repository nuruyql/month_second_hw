# homework_1.py

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "имеет высшее образование" if self.higher_education else "не имеет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, "
              f"моя профессия — {self.occupation}. Я {edu_status}.")


# Создаём несколько объектов класса Person
person1 = Person("Иван Иванов", "1995-04-12", "Программист", True)
person2 = Person("Сакура Харуно", "1990-03-28", "Медик-ниндзя", True)
person3 = Person("Монки Д. Луффи", "2000-05-05", "Пират", False)

# Распечатываем атрибуты
print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

# Вызываем метод introduce у каждого объекта
person1.introduce()
person2.introduce()
person3.introduce()
