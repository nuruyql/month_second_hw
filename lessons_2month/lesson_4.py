# class Animal:
#     def speak(self):
#         print("Animal speaking")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("мяу")
#         super().speak()
#
# class Dog(Animal):
#     def speak(self):
#         print("гав")
#         super().speak()
#
# class CatDog(Dog, Cat):
#     def speak(self):
#         print("гав мяу")
#         super().speak()
#
#
# kotopes = CatDog()
# kotopes.speak()
# print(CatDog.__mro__) # methods resolution order
# print(Dog.__mro__)


# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     @abstractmethod
#     def walk(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
#
#     def walk(self):
#         pass
# dog1 = Dog()
# dog1.make_sound()


class Animal:
    def speak(self):
        print("Hy")
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Myi")
class CatDog(Dog,Cat):
    pass



























