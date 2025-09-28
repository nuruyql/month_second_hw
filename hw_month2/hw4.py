class Vehicle:
    def start(self):
        print("Vehicle starting")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")


class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("ElectricCar starting")


class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print("Tesla ready")



t = Tesla()
t.start()
