# class Product:
#     a=5
#     def __init__(self,name,price,color):
#         self.name=name
#         self.price=price
#         self.color=color
# product = Product("HP VICTUS", "$750", "Blue")
#
# print(product.name,product.price,product.color)

# class MyStr:
#     def __init__(self, object: str):
#         self.object = object
#
#     def count(self, x, __start=None, __end=None):
#         if not __start:
#             __start = 0
#         if not __end:
#             __end = len(self.object)
#         c = 0
#         l = len(x)
#
#         for i in range(len(self.object[__start:__end]) - l):
#             if self.object[__start:__end][i:i + l] == x:
#                 c += 1
#         return c
#
#     def find(self, x, __start=None, __end=None):
#         if __start:
#             __start = 0
#         if not __end:
#             __end = len(self.object)
#         c = 0
#         l = len(x)
#         for i in range(len(self.object[__start:__end]) - l):
#             if self.object[__start:__end][i:i + l] == x:
#                 return i
#         else:
#             return -1
#     def rjust(self, width,field_char):
#         if len(self.object)>=width:
#             return self.object
#         else:
#             res=field_char*(width - len(self.object))
#         return res + self.object
#     def format(self, *args):
#         for i in args:
#             args.replace("{}")
#         return
#
#
# print(MyStr("Name: {}, age: {}").format('John',20))

