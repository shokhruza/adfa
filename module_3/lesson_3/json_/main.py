import json

# json.loads()
# json.dumps()
# json.load()
# json.dump()

# l=[1,2,3,4,4]
# l=json.dumps(l)
# print(type(l))
# l=json.loads(l)
# print(l)


# users = [
#     {
#         "id": 1,
#         "name": "Jamol"
#     },
#     {
#         "id": 2,
#         "name": "Kamol"
#     }
# ]
#
# with open('test.json', 'r') as f:
#     json.dump(users, f, indent=3)
#
# with open('test.json', 'r') as f:
#     data = json.load(f)
#     print(data)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# with open('numbers.json', 'r') as f:
#     data = json.load(f)
#
# data = [i for i in data if i % 2 == 0]
# with open('numbers.json', 'w') as f:
#     json.dump(data, f)

with open('numbers.json', 'r') as f:
    data = json.load(f)
with open('test.json', 'r') as f:
    users = json.load(f)

new = [user for user in users if user.get("id") in data]
with open('test.json', 'w') as f:
    json.dump(new, f, indent=3)
