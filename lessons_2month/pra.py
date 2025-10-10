# def difference(maxi, delitel):
#     total = maxi * (maxi + 1) // 2
#     summa_3del = maxi // delitel
#
#     num2 = delitel* summa_3del * (summa_3del + 1) // 2
#
#     return total - 2 * num2
#
# print(difference(10, 3))



# def numberOfSteps(num: int) -> int:
#     steps = 0
#     while num > 0:
#         if num % 2 == 0:  # even
#             num //= 2
#         else:             # odd
#             num -= 1
#         steps += 1
#     return steps
# print(numberOfSteps(20))


# def is_power_of_two(n: int) -> bool:
#     return n > 0 and (n & (n - 1)) == 0
# print(is_power_of_two(3))
#
#

# def degree(num):
#     return num >0 and (num & (num -1))==0
# print(degree(4))

# def twoN(nums,target):
#     known = {}
#
#     for i, num in enumerate(nums):
#         need = target - num
#         if need in known:
#             return [known[need],i]
#         known[num]=i
#
#
#
#
# print(twoN([1,2,34,5,6,7,8],36))


# def the_same(nums) -> bool:
#     return len(nums) != len(set(nums))
#
#
# print(the_same([11,12,3,5,6,4]))


# def square(nums):
#     squared = [i**2 for i in nums]
#     squared.sort()
#     return squared
# print(square([2,3,4,4]))


# def sum_dict(nums):
#     return sum(i for i in nums if i % 2 == 0)
# print(sum_dict([23,4,5,6,7]))


from datetime import datetime

class Friend:
    def __init__(self, name, birth_date):
        self.name = name
        self.__birth_date = birth_date  # приватный атрибут

    @property
    def age(self):
        today = datetime.today()
        # Вычисляем возраст по годам
        years = today.year - self.__birth_date.year
        # Проверяем, был ли день рождения в этом году
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            years -= 1
        return years

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Пример использования:
friend1 = Friend("Maxim", datetime(2000, 2, 20))
friend2 = Friend("Anna", datetime(1995, 10, 10))

print(friend1.introduce())
print(friend2.introduce())

# Можно обращаться к age напрямую:
print(friend1.age)  # → возраст Максим
