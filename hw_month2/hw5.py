

class Distance:

    _to_meters = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self._to_meters:
            raise ValueError("Unsupported unit! Use 'cm', 'm', or 'km'.")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self._to_meters[self.unit]

    @staticmethod
    def from_meters_to_km(meters, unit):
        return meters / Distance._to_meters[unit]


    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только объекты Distance")

        total_meters = self.to_meters() + other.to_meters()

        new_value = self.from_meters_to_km(total_meters, self.unit)
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно вычитать только объекты Distance")

        result_meters = self.to_meters() - other.to_meters()


        if result_meters < 0:
            raise ValueError("Результат не может быть отрицательным расстоянием")

        new_value = self.from_meters_to_km(result_meters, self.unit)
        return Distance(new_value, self.unit)


    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()


# ТЕСТИРОВАНИЕ
if __name__ == "__main__":
    d1 = Distance(100, "m")
    d2 = Distance(2, "km")
    d3 = Distance(5000, "cm")

    print("d1:", d1)
    print("d2:", d2)
    print("d3:", d3)

    print("\nСложение:")
    print("d1 + d2 =", d1 + d2)
    print("d1 + d3 =", d1 + d3)

    print("\nВычитание:")
    print("d2 - d1 =", d2 - d1)

    print("\nСравнение:")
    print("d1 == d3:", d1 == d3)
    print("d2 > d1:", d2 > d1)
    print("d1 < d2:", d1 < d2)
