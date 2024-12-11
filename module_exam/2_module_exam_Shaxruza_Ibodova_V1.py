# 2-savol
# from math import sqrt
#
#
# class Calculator:
#     def __init__(self,
#                  num1=None,
#                  num2=None
#                  ):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self, num1, num2):
#         return num1 + num2
#
#     def substraction(self, num1, num2):
#         return num1 - num2
#
#     def multiplication(self, num1, num2):
#         return num1 * num2
#
#     def ildiz(self, num1, num2):
#         return int(sqrt(num1)), int(sqrt(num2))
#
#     def divison(self, num1, num2):
#         return int(num1 / num2)
#
#
# print(Calculator().add(5, 5))
# print(Calculator().substraction(5, 6))
# print(Calculator().multiplication(5, 6))
# print(Calculator().ildiz(4, 9))
# print(Calculator().divison(4, 2))

# 3-savol
# res = "00"
# file = open("NUM.TXT", "r")
# numbers = [res if int(num) % 2 == 0 else num for num in file.read().split()]
# file = open("NUM.TXT", "w")
# file.write(" ".join(map(str, numbers)))
# file.close()


# 4-savol
# class SANOQ_SISTEMA_10:
#     def __init__(self, read, saqlash, chop_qilish):
#         self.read = read
#         self.saqlash = saqlash
#         self.chop_qilish = chop_qilish
#
#
# class SANOQ_SISTEMA_2(SANOQ_SISTEMA_10):
#     def __init__(self, read, saqlash,chop_qilish ):
#         super().__init__(read, saqlash, chop_qilish)
#
#
# class SANOQ_SISTEMA_8(SANOQ_SISTEMA_10):
#     def __init__(self, read, saqlash, chop_qilish):
#         super().__init__(read, saqlash, chop_qilish)
#
#
# class SANOQ_SISTEMA_16(SANOQ_SISTEMA_10):
#     def __init__(self, read, saqlash,chop_qilish):
#         super().__init__(read, saqlash, chop_qilish)
#


