
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    birth_date: str
    occupation: str
    higher_edu: bool
    def introduce(self) -> str:
        introduc = []
        introduc.append(f"-- My name is {self.name}")
        introduc.append(f"-- My bitrh date is {self.birth_date}")
        introduc.append(f"-- I work as a {self.occupation}")
        introduc.append(self.check_higher_ed())
        return "\n".join(introduc)
    def check_higher_ed(self):
        if self.higher_edu:
            return "-- i have higher education"
        else:
            return "-- i have no higher education"


person1 = Person("Nurbol","24.07","Backend Developer",True)
person2 = Person("Aktan","29.04","Frontend Developer",False)
print(person1.introduce())
print("\n"+"-"*50 +"\n")
print(person2.introduce())


