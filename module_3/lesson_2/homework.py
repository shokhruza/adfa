# import calendar
#
#
# def to_print(file=False):
#     def decorator(func):
#         def wrapper(*args, **kwargs ):
#             result = func(calendar.calendar(2025))
#             if file:
#                 with open('calendar_.txt', 'w') as f:
#                     f.write(result)
#             return result
#         return wrapper
#     return decorator
#
# @to_print(file=False)
# def create_calendar(file):
#     return file.read()


# calendar_data = create_calendar('calendar_.txt')
# print(2025)

# import datetime
#
# str_datetime = "2023-01-01 12:12:12"
# date_time = datetime.datetime.fromisoformat(str_datetime)
# print(date_time.strftime("%f"))


# import time, datetime
# x = datetime.date(2023, 1, 1)
# y = datetime.date(1970, 1, 1)
# print((x-y).total_seconds())
# secund = time.time()
# date = datetime.date.fromtimestamp(secund)
# print(datetime.datetime.fromtimestamp(1672531200.0))


import calendar
print(calendar.calendar(2024,2,2))