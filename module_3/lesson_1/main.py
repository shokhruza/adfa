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

# def my_filter(func, iterable):
#     for i in iterable:
#         if func(i):
#             yield i
#
#
# print(list(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))


# def count(n, step=1):
#     while True:
#         yield n
#         n += step
#
#
# for i in count(10, 3):
#     print(i)

# def cycle(iterable):
#     while True:
#
#
# for i in cycle(1, 2):
#     print(i)


# def repeat(start,step=None):
#     if step:
#         for i in range(step):
#             yield start
#     else:
#         while True:
#             yield start
# for i in repeat(10, 2):
#     print(i)

# def dropwile(func,iterable):
#     for i in iterable:
#         if not func(next(i)):
#             yield i
#
# print(list(dropwile(lambda x: x < 5, [1,4,6,4,1])))


# def takewhile(func, iterable):
#     for i in iterable:
#         if not func(i):
#             break
#         yield i
#
#
# print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))


# def chain(*args):
#     for i in args:
#         yield from i
#
# for i in chain([1, 2, 3], [1, 2]):
#     print(i)

# def batched(start,step):
#     while True:
#         if len(start) <= step:
#             yield start
#             break
#         else:
#             yield start[:step]
#             start = start[step:]
#
# for i in batched([1,2,3,4,5], 3):
#     print(i)

