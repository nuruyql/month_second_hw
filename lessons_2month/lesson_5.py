class Founder:
    def __init__(self,amount=0):
        self.amount = amount
    def __str__(self):
        return f"views of Money: {self.amount}, Eq : "
    def __add__(self, other):
        return Founder(self.amount + other.amount)
    def __sub__(self, other):
        return Founder(self.amount - other.amount)
    def __eq__(self, other):
        return self.amount == other.amount

mone1 = Founder(5000)
mone2 = Founder(2900)
total = mone1 + mone2
print(total,mone2 == mone1)