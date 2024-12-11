# def plus_one(number):
#     def add_one(number):
#         return number + 1
#
#     result = add_one(number)
#     return result
#
#
# print(plus_one(4))

# def plus_one(number):
#     return number + 1
#
#
# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)
#
#
# print(function_call(plus_one))


# def hello_function():
#     def say_hi():
#         return "HI"
#
#     return say_hi
#
#
# hello = hello_function()
# print(hello())


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return 'hi there'
#
#
# @uppercase_decorator
# def say_hello():
#     return 'hello there'
#
#
# print(say_hi())
# print(say_hello())


# def two_division(function):
#     def wrapper(*args):
#         func = function(*args) / 2
#         return func
#
#     return wrapper
#
#
# @two_division
# def summa(*args):
#     return sum(args)
#
#
# print(summa(1, 2, 3, 4, 5))


# def two_division(num):
#     def inner(function):
#         def wrapper(*args):
#
#             return function(*args) / num
#
#         return wrapper
#
#     return inner
#
#
# @two_division(10)
# def summa(*args):
#     return sum(args)
#
#
# print(summa(1, 2, 3, 4, 5))

users = [
    {
        "id": 1,
        "username": "botir",
        "password": "1111",
        "role": "ADMIN"
    },
    {
        "id": 2,
        "username": "baxa",
        "password": "2222",
        "role": "USER"
    },
    {
        "id": 3,
        "username": "Jamol",
        "password": "0000",
        "role": "USER"
    }
]


#
#
# def is_auth(function):
#     def wrapper(username,password):
#         for user in users:
#             if user.get("username") == username and user.get("password")==password:
#                 return function()
#         return "Not found acoount"
#     return wrapper
#
#
#
# @is_auth
# def account():
#     return True, "Welcome"
#
#
# print(account(username="baxa", password="1111"))

def is_auth(function):
    def wrapper(*args, **kwargs):
        for user in users:
            if user.get("username") == kwargs.get("username") and user.get("password") == kwargs.get("password"):
                return function(*args, **kwargs)
        return "Not found acoount"

    return wrapper


def permisson(role):
    def inner(function):
        def wrapper(*args, **kwargs):
            for user in users:
                if user.get("username") == kwargs.get('username') and user.get("password") == kwargs.get('password'):
                    if role == kwargs.get('role'):
                        return function(*args)
                    else:
                        return 'Permisson denied'

        return wrapper

    return inner


@is_auth
@permisson(role=["ADMIN", "USER"])
def summa(*args, **kwargs):
    return sum(args, kwargs)


print(summa(1, 2, username="baxa123", password="2222"))
print(summa(1, 2, username="baxa", password="2222"))
print(summa(1, 2, username="botir", password="1111"))
