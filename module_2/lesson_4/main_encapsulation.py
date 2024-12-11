# ============= public ==============
# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# a=A(2,3)
# print(a.a)
# print(a.b)

# ============= protected =============
# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self._b=b
#     @property
#     def b(self):
#         return self._b
#
#     @b.setter
#     def b(self,new_val):
#         self._b=new_val
#
# a=A(2,3)
# a.b=4
# print(a.a)
# print(a.b)

# ============= private ==============
# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.__b=b
# a=A(1,2)
# print(a.a)



