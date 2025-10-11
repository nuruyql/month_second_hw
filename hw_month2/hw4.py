from abc import ABC, abstractmethod


@abstractmethod
class Vehicle(ABC):
    def start(self):
        print("s1s1")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Brym Brym")
class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("Tu-tu-tu-tu")
class Tesla(Car,ElectricCar):
    def start(self):
        super().start()
        print("SH-SH-SH")



vehicle = [Car,ElectricCar,Tesla]
for i in vehicle:
    i().start()
    