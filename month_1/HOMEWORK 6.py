# def check(password: str) -> bool:
#     if len(password) < 6:
#         return False
#
#     has_upper = any(c.isupper() for c in password)
#     has_lower = any(c.islower() for c in password)
#     has_digit = any(c.isdigit() for c in password)
#     special_chars = sum(not c.isalnum() for c in password)
#
#     if has_upper and has_lower and has_digit and special_chars >= 2:
#         return True
#     else:
#         return False
# password = input("enter the password: ")
# print(check(password))


