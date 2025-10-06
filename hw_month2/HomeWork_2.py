
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    occupation: str

    def introduce(self):
        return (f"My name is {self.name},"
                f"i work as {self.occupation}"
                )
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
classmate2 = Classmate("Aktan","Frontend Developer","CS24-14")
friend1 = Friend("Maxim","Frontend Developer","skiing")
friend2 = Friend("Timur","Backend Developer","mobile games")
best_friend = BestFriend("Muhammed","Dentist","football","first meeting")
introduce_object = [classmate1,classmate2,friend2,friend1,best_friend]
for i in introduce_object:
    print(i.introduce())
