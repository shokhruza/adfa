"""
file access mode:
    r   -> read
    w   -> yangilash
    a   -> qo'shish
    x   -> yaratish
"""
# file = open("test.txt", mode="r")
#
# file.close()
#
# print(file.read())

# 1-savol
# num = int(input("num : "))
# s = ''
# for i in range(1, num+1):
#     s += f"{str(i)} "
# file = open("test.txt", mode="w")
# file.write(s)
# file.close()

# 2-savol
# num1 = int(input("num1 : "))
# num2 = int(input("num2 : "))
# s = [i for i in range(num1, num2+1) if i % 2 == 0]
# file = open("nums.txt", mode="w")
# for i in s:
#     file.write(f"{str(i)} ")
# file.close()

# 3-savol
# user_info={
#     "fullname": input("Fullname: "),
#     "age": int(input("Age: ")),
#     "address": input("Address: ")
#
# }
# s = f"{user_info['fullname']}|{user_info['age']}|{user_info['address']}"
# file = open("users.txt", mode="w")
# file.write(s)
# file.close()

# 4-savol
# import json
#
# file = open("todos.json", "r")
# todos = json.load(file)
# file.close()
# user_info={
#     "userId": int(input("UserID : ")),
#     "id": int(input("ID : ")),
#     "title": input("title : "),
#     "completed": input("completed : ")
# }
#
# file = open("todos.json",mode="w")
# file.write(",".join(map(str, todos)))
# file.close()

# 5-savol
# file = open("NUM.TXT", "r")
# numbers=[int(num) for num in file.read().split() if int(num) % 2 != 0]
# file = open("NUM.TXT", "w")
# file.write(" ".join(map(str, numbers)))
# file.close()

# 6-savol
# file = open("sentences.txt", "r")
# a=file.read()
# s=' '.join(a.split())
# file = open("sentences.TXT", "w")
# file.write(s)
# file.close()
#


# 7-savol
# user_info={
#     "fullname": input("Fullname: "),
#     "age": int(input("Age: ")),
#     "address": input("Address: ")
#
# }
#
# s = f"{user_info['fullname']}|{user_info['age']}|{user_info['address']}"
# file = open("users.txt", mode="w")
# file.write(s)
# file.close()
#
# 2-usul
# users = []
# with open('sentences.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         parts = line.strip().split('|')
#
#         user = {
#             "fullname": parts[0],
#             "age": int(parts[1]),
#             "address": parts[2]
#         }
#         users.append(user)
# for user in users:
#     print(user)