
class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def introduce(self,name,age,occupation):
        return f"Hello my name is {self.name}, i am {self.age} years old and i work as a {self.occupation}"
class ClassMate(Person):
    def __init__(self, name, age, occupation, place_of_residents):
        super().__init__(name,age,occupation)
        self.place_of_residents = place_of_residents

    def introduce(self):
        return (
            f"Hello my name is {self.name}, "
            f"I am {self.age} years old and "
            f"I work as a {self.occupation} and "
            f"I live in {self.place_of_residents}."
        )
class Friend(Person):
    def __init__(self,name,age,occupation,hobby):
        super().__init__(name,age,occupation)
        self.hobby = hobby
    def introduce(self):
        return (f"Hello my name is {self.name}"
                f" and i am {self.age} years old,"
                f" i work as a {self.occupation} and"
                f" my hobby is {self.hobby}")
person1 = Person("Nurbol",17,"Backend developer")
person1.introduce()
person2 = ClassMate("Max",17,"Frontend developer","Bishkek")
person2.introduce()
person3 = Friend("Timur",17,"Security developer","Basketball")
person3.introduce()

