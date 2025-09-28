from abc import ABC, abstractmethod

# === Product (Продукт) ===
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# === Concrete Products (Конкретные продукты) ===
class Truck(Transport):
    def deliver(self):
        return "Delivering goods by land in a truck 🚚"


class Ship(Transport):
    def deliver(self):
        return "Delivering goods by sea in a ship 🚢"


class Plane(Transport):
    def deliver(self):
        return "Delivering goods by air in a plane ✈️"


# === Creator (Создатель) ===
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()   # 👈 фабричный метод
        print("Planning delivery...")
        print(transport.deliver())
        print("Delivery completed!\n")


# === Concrete Creators (Конкретные логистики) ===
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


class AirLogistics(Logistics):
    def create_transport(self):
        return Plane()


# === Client Code (Клиентский код) ===
if __name__ == "__main__":
    logistics_list = [RoadLogistics(), SeaLogistics(), AirLogistics()]

    for logistics in logistics_list:
        logistics.plan_delivery()
