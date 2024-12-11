# def custom_product(iterable, repeat):
#     if repeat == 1:
#         yield iterable
#     else:
#         result = []
#         sub_product = custom_product(iterable, repeat - 1)
#         for item in iterable:
#             for sub_item in sub_product:
#                 result.append(item + sub_item)
#         yield result
#
# result = custom_product('ABCD', 2)
# print(result)



# ///1
# def my_number(*args):
#     while True:
#         yield args
#
# for i in my_number(10):
#     print(i)

# /// 2
# def my_filter(func, iterable):
#     for i in iterable:
#         if func(i):
#             yield i
#
#
# print(list(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# /// 3
# def fibonachi(n):
#     s1 = 1
#     s2 = 1
#     if n == 1:
#         yield s1
#     if n == 2:
#         yield s1
#         yield s2
#     else:
#         i = 2
#         while i < n:
#             s3 = s1 + s2
#             yield s3
#             s1 = s2
#             s2 = s3
#             i += 1
#
#
# for i in fibonachi(8):
#     print(i)

# /// 4
# def my_password(func, iterable):
#     for i in iterable:
#         if func(i):
#             yield i
#
#
#
# print(list(my_password(lambda x: x % 4, [1000,10000])))

# /// 5


# /// 6

# def my_number(func, iterable):
#     for i in iterable:
#             yield func(i)
#
#
# print(list(my_number(lambda x: x * 2, [1, 2, 3, 4])))
