# def two_Sums(nums, target):
#     seen = set()
#     pairs = set()
#
#     for i in nums:
#         need = target - i
#         if need in seen:
#             pairs.add(tuple(sorted((i, need))))
#         seen.add(i)
#     return list(pairs)
#
# # Пример вызова
# nums = [5, 4, 6, 7, 8, 9, 8, 7, 7, 2, 1, 3]
# target = 10
#
# print(two_Sums(nums, target))











