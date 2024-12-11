# vendors = []
# class Vendor:
#     def init(self , id , user_id , balance):
#         self.id = id
#         self.user_id = user_id
#         self.balance = balance
#     def save(self):
#         vendors.append(self)
#
#     def delete(self,vendor_id):
#         for vendor in vendors:
#             if vendor.id == vendor_id:
#                 vendors.remove(vendor)
#     def update(self, field , new_val):
#         for vendor in vendors:
#             if vendor.id == self.id:
#                 if field == "user_id":
#                     vendor.user_id = new_val
#                 elif field == "balance":
#                     vendor.balance = new_val
#
#
#
#     def get_vendor(self , vendor_id):
#         for vendor in vendors:
#             if vendor.id == vendor_id:
#                 return vendor.dict
#
#     def repr(self):
#         return f"{self.balance}"
#
# v = Vendor( 'a','b', 100000)
# v2 = Vendor("c",'s', 2000)
# v2.save()
# v.save()
# v.update("balance" , 50000)
# print(v.get_vendor(2))
# print(vendors)


# users=[]
# class User:
#     def __init__(self, id, fullname,phone,email,role,join_at):
#         self.id = id
#         self.fullname = fullname
#         self.phone = phone
#         self.email = email
#         self.role = role
#         self.join_at = join_at
#
#     def save(self):
#         users.append(self)
#     def delete(self, user_id):
#         for user in users:
#             if user.id == user_id:
#                 users.remove(user)
#     def update(self, field , new_val):
#         for user in users:
#             if user.id == self.id:
#                 if field == "id":
#                     user.id = new_val
#                 elif field == "fullname":
#                     user.balance = new_val
#
#
#     def repr(self):
#         return f"{self.fullname}"


# l = [
#     {
#         "name": "name 1",
#         "price": 73,
#         "color": "color 1",
#         "id": "1"
#     },
#     {
#         "name": "name 2",
#         "price": 54,
#         "color": "color 2",
#         "id": "2"
#     },
#     {
#         "name": "name 3",
#         "price": 62,
#         "color": "color 3",
#         "id": "3"
#     },
#     {
#         "name": "name 4",
#         "price": 41,
#         "color": "color 4",
#         "id": "4"
#     },
#     {
#         "name": "name 5",
#         "price": 82,
#         "color": "color 5",
#         "id": "5"
#     },
#     {
#         "name": "name 6",
#         "price": 91,
#         "color": "color 6",
#         "id": "6"
#     },
#     {
#         "name": "name 7",
#         "price": 20,
#         "color": "color 7",
#         "id": "7"
#     },
#     {
#         "name": "name 8",
#         "price": 56,
#         "color": "color 8",
#         "id": "8"
#     },
#     {
#         "name": "name 9",
#         "price": 13,
#         "color": "color 9",
#         "id": "9"
#     },
#     {
#         "name": "name 10",
#         "price": 97,
#         "color": "color 10",
#         "id": "10"
#     },
#     {
#         "name": "name 11",
#         "price": 12,
#         "color": "color 11",
#         "id": "11"
#     },
#     {
#         "name": "name 12",
#         "price": 77,
#         "color": "color 12",
#         "id": "12"
#     },
#     {
#         "name": "name 13",
#         "price": 15,
#         "color": "color 13",
#         "id": "13"
#     },
#     {
#         "name": "name 14",
#         "price": 27,
#         "color": "color 14",
#         "id": "14"
#     },
#     {
#         "name": "name 15",
#         "price": 34,
#         "color": "color 15",
#         "id": "15"
#     },
#     {
#         "name": "name 16",
#         "price": 57,
#         "color": "color 16",
#         "id": "16"
#     },
#     {
#         "name": "name 17",
#         "price": 87,
#         "color": "color 17",
#         "id": "17"
#     },
#     {
#         "name": "name 18",
#         "price": 86,
#         "color": "color 18",
#         "id": "18"
#     },
#     {
#         "name": "name 19",
#         "price": 6,
#         "color": "color 19",
#         "id": "19"
#     },
#     {
#         "name": "name 20",
#         "price": 10,
#         "color": "color 20",
#         "id": "20"
#     },
#     {
#         "name": "name 21",
#         "price": 34,
#         "color": "color 21",
#         "id": "21"
#     },
#     {
#         "name": "name 22",
#         "price": 5,
#         "color": "color 22",
#         "id": "22"
#     },
#     {
#         "name": "name 23",
#         "price": 0,
#         "color": "color 23",
#         "id": "23"
#     },
#     {
#         "name": "name 24",
#         "price": 53,
#         "color": "color 24",
#         "id": "24"
#     },
#     {
#         "name": "name 25",
#         "price": 33,
#         "color": "color 25",
#         "id": "25"
#     },
#     {
#         "name": "name 26",
#         "price": 9,
#         "color": "color 26",
#         "id": "26"
#     },
#     {
#         "name": "name 27",
#         "price": 23,
#         "color": "color 27",
#         "id": "27"
#     },
#     {
#         "name": "name 28",
#         "price": 51,
#         "color": "color 28",
#         "id": "28"
#     },
#     {
#         "name": "name 29",
#         "price": 98,
#         "color": "color 29",
#         "id": "29"
#     },
#     {
#         "name": "name 30",
#         "price": 13,
#         "color": "color 30",
#         "id": "30"
#     },
#     {
#         "name": "name 31",
#         "price": 98,
#         "color": "color 31",
#         "id": "31"
#     },
#     {
#         "name": "name 32",
#         "price": 40,
#         "color": "color 32",
#         "id": "32"
#     },
#     {
#         "name": "name 33",
#         "price": 17,
#         "color": "color 33",
#         "id": "33"
#     },
#     {
#         "name": "name 34",
#         "price": 4,
#         "color": "color 34",
#         "id": "34"
#     },
#     {
#         "name": "name 35",
#         "price": 50,
#         "color": "color 35",
#         "id": "35"
#     },
#     {
#         "name": "name 36",
#         "price": 58,
#         "color": "color 36",
#         "id": "36"
#     },
#     {
#         "name": "name 37",
#         "price": 36,
#         "color": "color 37",
#         "id": "37"
#     },
#     {
#         "name": "name 38",
#         "price": 78,
#         "color": "color 38",
#         "id": "38"
#     },
#     {
#         "name": "name 39",
#         "price": 52,
#         "color": "color 39",
#         "id": "39"
#     },
#     {
#         "name": "name 40",
#         "price": 11,
#         "color": "color 40",
#         "id": "40"
#     },
#     {
#         "name": "name 41",
#         "price": 69,
#         "color": "color 41",
#         "id": "41"
#     },
#     {
#         "name": "name 42",
#         "price": 57,
#         "color": "color 42",
#         "id": "42"
#     },
#     {
#         "name": "name 43",
#         "price": 62,
#         "color": "color 43",
#         "id": "43"
#     },
#     {
#         "name": "name 44",
#         "price": 22,
#         "color": "color 44",
#         "id": "44"
#     },
#     {
#         "name": "name 45",
#         "price": 10,
#         "color": "color 45",
#         "id": "45"
#     },
#     {
#         "name": "name 46",
#         "price": 48,
#         "color": "color 46",
#         "id": "46"
#     },
#     {
#         "name": "name 47",
#         "price": 17,
#         "color": "color 47",
#         "id": "47"
#     },
#     {
#         "name": "name 48",
#         "price": 77,
#         "color": "color 48",
#         "id": "48"
#     },
#     {
#         "name": "name 49",
#         "price": 36,
#         "color": "color 49",
#         "id": "49"
#     },
#     {
#         "name": "name 50",
#         "price": 10,
#         "color": "color 50",
#         "id": "50"
#     },
#     {
#         "name": "name 51",
#         "price": 42,
#         "color": "color 51",
#         "id": "51"
#     },
#     {
#         "name": "name 52",
#         "price": 85,
#         "color": "color 52",
#         "id": "52"
#     },
#     {
#         "name": "name 53",
#         "price": 83,
#         "color": "color 53",
#         "id": "53"
#     },
#     {
#         "name": "name 54",
#         "price": 68,
#         "color": "color 54",
#         "id": "54"
#     },
#     {
#         "name": "name 55",
#         "price": 71,
#         "color": "color 55",
#         "id": "55"
#     },
#     {
#         "name": "name 56",
#         "price": 16,
#         "color": "color 56",
#         "id": "56"
#     },
#     {
#         "name": "name 57",
#         "price": 63,
#         "color": "color 57",
#         "id": "57"
#     },
#     {
#         "name": "name 58",
#         "price": 26,
#         "color": "color 58",
#         "id": "58"
#     },
#     {
#         "name": "name 59",
#         "price": 75,
#         "color": "color 59",
#         "id": "59"
#     },
#     {
#         "name": "name 60",
#         "price": 57,
#         "color": "color 60",
#         "id": "60"
#     },
#     {
#         "name": "name 61",
#         "price": 36,
#         "color": "color 61",
#         "id": "61"
#     },
#     {
#         "name": "name 62",
#         "price": 17,
#         "color": "color 62",
#         "id": "62"
#     },
#     {
#         "name": "name 63",
#         "price": 99,
#         "color": "color 63",
#         "id": "63"
#     },
#     {
#         "name": "name 64",
#         "price": 13,
#         "color": "color 64",
#         "id": "64"
#     },
#     {
#         "name": "name 65",
#         "price": 25,
#         "color": "color 65",
#         "id": "65"
#     },
#     {
#         "name": "name 66",
#         "price": 50,
#         "color": "color 66",
#         "id": "66"
#     },
#     {
#         "name": "name 67",
#         "price": 75,
#         "color": "color 67",
#         "id": "67"
#     },
#     {
#         "name": "name 68",
#         "price": 47,
#         "color": "color 68",
#         "id": "68"
#     },
#     {
#         "name": "name 69",
#         "price": 85,
#         "color": "color 69",
#         "id": "69"
#     },
#     {
#         "name": "name 70",
#         "price": 97,
#         "color": "color 70",
#         "id": "70"
#     },
#     {
#         "name": "name 71",
#         "price": 67,
#         "color": "color 71",
#         "id": "71"
#     },
#     {
#         "name": "name 72",
#         "price": 74,
#         "color": "color 72",
#         "id": "72"
#     },
#     {
#         "name": "name 73",
#         "price": 46,
#         "color": "color 73",
#         "id": "73"
#     },
#     {
#         "name": "name 74",
#         "price": 15,
#         "color": "color 74",
#         "id": "74"
#     },
#     {
#         "name": "name 75",
#         "price": 22,
#         "color": "color 75",
#         "id": "75"
#     },
#     {
#         "name": "name 76",
#         "price": 95,
#         "color": "color 76",
#         "id": "76"
#     },
#     {
#         "name": "name 77",
#         "price": 41,
#         "color": "color 77",
#         "id": "77"
#     },
#     {
#         "name": "name 78",
#         "price": 91,
#         "color": "color 78",
#         "id": "78"
#     },
#     {
#         "name": "name 79",
#         "price": 94,
#         "color": "color 79",
#         "id": "79"
#     },
#     {
#         "name": "name 80",
#         "price": 99,
#         "color": "color 80",
#         "id": "80"
#     },
#     {
#         "name": "name 81",
#         "price": 27,
#         "color": "color 81",
#         "id": "81"
#     },
#     {
#         "name": "name 82",
#         "price": 96,
#         "color": "color 82",
#         "id": "82"
#     },
#     {
#         "name": "name 83",
#         "price": 88,
#         "color": "color 83",
#         "id": "83"
#     },
#     {
#         "name": "name 84",
#         "price": 51,
#         "color": "color 84",
#         "id": "84"
#     },
#     {
#         "name": "name 85",
#         "price": 2,
#         "color": "color 85",
#         "id": "85"
#     },
#     {
#         "name": "name 86",
#         "price": 45,
#         "color": "color 86",
#         "id": "86"
#     },
#     {
#         "name": "name 87",
#         "price": 100,
#         "color": "color 87",
#         "id": "87"
#     },
#     {
#         "name": "name 88",
#         "price": 50,
#         "color": "color 88",
#         "id": "88"
#     },
#     {
#         "name": "name 89",
#         "price": 8,
#         "color": "color 89",
#         "id": "89"
#     },
#     {
#         "name": "name 90",
#         "price": 84,
#         "color": "color 90",
#         "id": "90"
#     },
#     {
#         "name": "name 91",
#         "price": 38,
#         "color": "color 91",
#         "id": "91"
#     },
#     {
#         "name": "name 92",
#         "price": 89,
#         "color": "color 92",
#         "id": "92"
#     },
#     {
#         "name": "name 93",
#         "price": 70,
#         "color": "color 93",
#         "id": "93"
#     },
#     {
#         "name": "name 94",
#         "price": 33,
#         "color": "color 94",
#         "id": "94"
#     },
#     {
#         "name": "name 95",
#         "price": 61,
#         "color": "color 95",
#         "id": "95"
#     }
# ]
#
#
# class Product:
#     def __init__(self, id=None, name=None, price=None, color=None):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.color = color
#
#     def filter_price(self, from_price, to_price):
#         res = []
#         for product in l:
#             if from_price <= product.get("price") <= to_price:
#                 p = Product(product.get("id"), product.get("name"), product.get("price"), product.get("color"))
#                 res.append(p)
#         return res
#
#
#
#     def __repr__(self):
#         return f"{self.price}"
#
#
# p = Product()
# print(p.filter_price(40,60))


# products = [
#     {
#         "product_id": 28,
#         "count": 5,
#         "order_date": 1705748890,
#         "id": "1"
#     },
#     {
#         "product_id": 21,
#         "count": 52,
#         "order_date": 1705748830,
#         "id": "2"
#     },
#     {
#         "product_id": 35,
#         "count": 45,
#         "order_date": 1705748770,
#         "id": "3"
#     },
#     {
#         "product_id": 46,
#         "count": 22,
#         "order_date": 1705748710,
#         "id": "4"
#     },
#     {
#         "product_id": 92,
#         "count": 25,
#         "order_date": 1705748650,
#         "id": "5"
#     },
#     {
#         "product_id": 96,
#         "count": 46,
#         "order_date": 1705748590,
#         "id": "6"
#     },
#     {
#         "product_id": 97,
#         "count": 78,
#         "order_date": 1705748530,
#         "id": "7"
#     },
#     {
#         "product_id": 64,
#         "count": 41,
#         "order_date": 1705748470,
#         "id": "8"
#     },
#     {
#         "product_id": 54,
#         "count": 97,
#         "order_date": 1705748410,
#         "id": "9"
#     },
#     {
#         "product_id": 73,
#         "count": 20,
#         "order_date": 1705748350,
#         "id": "10"
#     },
#     {
#         "product_id": 52,
#         "count": 13,
#         "order_date": 1705748290,
#         "id": "11"
#     },
#     {
#         "product_id": 80,
#         "count": 89,
#         "order_date": 1705748230,
#         "id": "12"
#     },
#     {
#         "product_id": 65,
#         "count": 8,
#         "order_date": 1705748170,
#         "id": "13"
#     },
#     {
#         "product_id": 85,
#         "count": 84,
#         "order_date": 1705748110,
#         "id": "14"
#     },
#     {
#         "product_id": 14,
#         "count": 72,
#         "order_date": 1705748050,
#         "id": "15"
#     },
#     {
#         "product_id": 9,
#         "count": 7,
#         "order_date": 1705747990,
#         "id": "16"
#     },
#     {
#         "product_id": 89,
#         "count": 9,
#         "order_date": 1705747930,
#         "id": "17"
#     },
#     {
#         "product_id": 45,
#         "count": 59,
#         "order_date": 1705747870,
#         "id": "18"
#     },
#     {
#         "product_id": 98,
#         "count": 60,
#         "order_date": 1705747810,
#         "id": "19"
#     },
#     {
#         "product_id": 10,
#         "count": 82,
#         "order_date": 1705747750,
#         "id": "20"
#     },
#     {
#         "product_id": 56,
#         "count": 13,
#         "order_date": 1705747690,
#         "id": "21"
#     },
#     {
#         "product_id": 41,
#         "count": 47,
#         "order_date": 1705747630,
#         "id": "22"
#     },
#     {
#         "product_id": 58,
#         "count": 87,
#         "order_date": 1705747570,
#         "id": "23"
#     },
#     {
#         "product_id": 15,
#         "count": 67,
#         "order_date": 1705747510,
#         "id": "24"
#     },
#     {
#         "product_id": 7,
#         "count": 61,
#         "order_date": 1705747450,
#         "id": "25"
#     },
#     {
#         "product_id": 63,
#         "count": 83,
#         "order_date": 1705747390,
#         "id": "26"
#     },
#     {
#         "product_id": 37,
#         "count": 31,
#         "order_date": 1705747330,
#         "id": "27"
#     },
#     {
#         "product_id": 54,
#         "count": 41,
#         "order_date": 1705747270,
#         "id": "28"
#     },
#     {
#         "product_id": 70,
#         "count": 80,
#         "order_date": 1705747210,
#         "id": "29"
#     },
#     {
#         "product_id": 4,
#         "count": 19,
#         "order_date": 1705747150,
#         "id": "30"
#     },
#     {
#         "product_id": 98,
#         "count": 8,
#         "order_date": 1705747090,
#         "id": "31"
#     },
#     {
#         "product_id": 97,
#         "count": 72,
#         "order_date": 1705747030,
#         "id": "32"
#     },
#     {
#         "product_id": 89,
#         "count": 26,
#         "order_date": 1705746970,
#         "id": "33"
#     },
#     {
#         "product_id": 52,
#         "count": 72,
#         "order_date": 1705746910,
#         "id": "34"
#     },
#     {
#         "product_id": 65,
#         "count": 37,
#         "order_date": 1705746850,
#         "id": "35"
#     },
#     {
#         "product_id": 38,
#         "count": 64,
#         "order_date": 1705746790,
#         "id": "36"
#     },
#     {
#         "product_id": 96,
#         "count": 70,
#         "order_date": 1705746730,
#         "id": "37"
#     },
#     {
#         "product_id": 44,
#         "count": 38,
#         "order_date": 1705746670,
#         "id": "38"
#     },
#     {
#         "product_id": 44,
#         "count": 14,
#         "order_date": 1705746610,
#         "id": "39"
#     },
#     {
#         "product_id": 30,
#         "count": 46,
#         "order_date": 1705746550,
#         "id": "40"
#     },
#     {
#         "product_id": 90,
#         "count": 9,
#         "order_date": 1705746490,
#         "id": "41"
#     },
#     {
#         "product_id": 17,
#         "count": 56,
#         "order_date": 1705746430,
#         "id": "42"
#     },
#     {
#         "product_id": 39,
#         "count": 2,
#         "order_date": 1705746370,
#         "id": "43"
#     },
#     {
#         "product_id": 67,
#         "count": 9,
#         "order_date": 1705746310,
#         "id": "44"
#     },
#     {
#         "product_id": 60,
#         "count": 58,
#         "order_date": 1705746250,
#         "id": "45"
#     },
#     {
#         "product_id": 17,
#         "count": 17,
#         "order_date": 1705746190,
#         "id": "46"
#     },
#     {
#         "product_id": 72,
#         "count": 79,
#         "order_date": 1705746130,
#         "id": "47"
#     },
#     {
#         "product_id": 30,
#         "count": 72,
#         "order_date": 1705746070,
#         "id": "48"
#     },
#     {
#         "product_id": 29,
#         "count": 17,
#         "order_date": 1705746010,
#         "id": "49"
#     },
#     {
#         "product_id": 46,
#         "count": 34,
#         "order_date": 1705745950,
#         "id": "50"
#     },
#     {
#         "product_id": 88,
#         "count": 4,
#         "order_date": 1705745890,
#         "id": "51"
#     },
#     {
#         "product_id": 67,
#         "count": 20,
#         "order_date": 1705745830,
#         "id": "52"
#     },
#     {
#         "product_id": 91,
#         "count": 9,
#         "order_date": 1705745770,
#         "id": "53"
#     },
#     {
#         "product_id": 45,
#         "count": 62,
#         "order_date": 1705745710,
#         "id": "54"
#     },
#     {
#         "product_id": 48,
#         "count": 42,
#         "order_date": 1705745650,
#         "id": "55"
#     },
#     {
#         "product_id": 38,
#         "count": 65,
#         "order_date": 1705745590,
#         "id": "56"
#     },
#     {
#         "product_id": 11,
#         "count": 4,
#         "order_date": 1705745530,
#         "id": "57"
#     },
#     {
#         "product_id": 92,
#         "count": 18,
#         "order_date": 1705745470,
#         "id": "58"
#     },
#     {
#         "product_id": 80,
#         "count": 77,
#         "order_date": 1705745410,
#         "id": "59"
#     },
#     {
#         "product_id": 72,
#         "count": 3,
#         "order_date": 1705745350,
#         "id": "60"
#     },
#     {
#         "product_id": 94,
#         "count": 68,
#         "order_date": 1705745290,
#         "id": "61"
#     },
#     {
#         "product_id": 2,
#         "count": 61,
#         "order_date": 1705745230,
#         "id": "62"
#     },
#     {
#         "product_id": 84,
#         "count": 30,
#         "order_date": 1705745170,
#         "id": "63"
#     },
#     {
#         "product_id": 28,
#         "count": 31,
#         "order_date": 1705745110,
#         "id": "64"
#     },
#     {
#         "product_id": 33,
#         "count": 26,
#         "order_date": 1705745050,
#         "id": "65"
#     },
#     {
#         "product_id": 40,
#         "count": 73,
#         "order_date": 1705744990,
#         "id": "66"
#     },
#     {
#         "product_id": 37,
#         "count": 91,
#         "order_date": 1705744930,
#         "id": "67"
#     },
#     {
#         "product_id": 89,
#         "count": 60,
#         "order_date": 1705744870,
#         "id": "68"
#     },
#     {
#         "product_id": 74,
#         "count": 36,
#         "order_date": 1705744810,
#         "id": "69"
#     },
#     {
#         "product_id": 62,
#         "count": 56,
#         "order_date": 1705744750,
#         "id": "70"
#     },
#     {
#         "product_id": 28,
#         "count": 90,
#         "order_date": 1705744690,
#         "id": "71"
#     },
#     {
#         "product_id": 39,
#         "count": 29,
#         "order_date": 1705744630,
#         "id": "72"
#     },
#     {
#         "product_id": 72,
#         "count": 5,
#         "order_date": 1705744570,
#         "id": "73"
#     },
#     {
#         "product_id": 7,
#         "count": 33,
#         "order_date": 1705744510,
#         "id": "74"
#     },
#     {
#         "product_id": 58,
#         "count": 65,
#         "order_date": 1705744450,
#         "id": "75"
#     },
#     {
#         "product_id": 74,
#         "count": 2,
#         "order_date": 1705744390,
#         "id": "76"
#     },
#     {
#         "product_id": 95,
#         "count": 15,
#         "order_date": 1705744330,
#         "id": "77"
#     },
#     {
#         "product_id": 11,
#         "count": 12,
#         "order_date": 1705744270,
#         "id": "78"
#     },
#     {
#         "product_id": 57,
#         "count": 3,
#         "order_date": 1705744210,
#         "id": "79"
#     },
#     {
#         "product_id": 35,
#         "count": 11,
#         "order_date": 1705744150,
#         "id": "80"
#     },
#     {
#         "product_id": 75,
#         "count": 24,
#         "order_date": 1705744090,
#         "id": "81"
#     },
#     {
#         "product_id": 74,
#         "count": 25,
#         "order_date": 1705744030,
#         "id": "82"
#     },
#     {
#         "product_id": 53,
#         "count": 91,
#         "order_date": 1705743970,
#         "id": "83"
#     },
#     {
#         "product_id": 48,
#         "count": 26,
#         "order_date": 1705743910,
#         "id": "84"
#     },
#     {
#         "product_id": 61,
#         "count": 32,
#         "order_date": 1705743850,
#         "id": "85"
#     },
#     {
#         "product_id": 85,
#         "count": 74,
#         "order_date": 1705743790,
#         "id": "86"
#     },
#     {
#         "product_id": 70,
#         "count": 71,
#         "order_date": 1705743730,
#         "id": "87"
#     },
#     {
#         "product_id": 94,
#         "count": 91,
#         "order_date": 1705743670,
#         "id": "88"
#     },
#     {
#         "product_id": 29,
#         "count": 28,
#         "order_date": 1705743610,
#         "id": "89"
#     },
#     {
#         "product_id": 9,
#         "count": 38,
#         "order_date": 1705743550,
#         "id": "90"
#     },
#     {
#         "product_id": 72,
#         "count": 2,
#         "order_date": 1705743490,
#         "id": "91"
#     },
#     {
#         "product_id": 83,
#         "count": 57,
#         "order_date": 1705743430,
#         "id": "92"
#     },
#     {
#         "product_id": 65,
#         "count": 55,
#         "order_date": 1705743371,
#         "id": "93"
#     },
#     {
#         "product_id": 55,
#         "count": 79,
#         "order_date": 1705743311,
#         "id": "94"
#     },
#     {
#         "product_id": 67,
#         "count": 67,
#         "order_date": 1705743251,
#         "id": "95"
#     },
#     {
#         "product_id": 6,
#         "count": 92,
#         "order_date": 1705743191,
#         "id": "96"
#     },
#     {
#         "product_id": 15,
#         "count": 98,
#         "order_date": 1705743131,
#         "id": "97"
#     },
#     {
#         "product_id": 6,
#         "count": 32,
#         "order_date": 1705743071,
#         "id": "98"
#     },
#     {
#         "product_id": 41,
#         "count": 13,
#         "order_date": 1705743011,
#         "id": "99"
#     },
#     {
#         "product_id": 30,
#         "count": 77,
#         "order_date": 1705742951,
#         "id": "100"
#     }
# ]

# class Product:
#     def __init__(self, product_id=None, count=None, order_date=None, id=None):
#         self.product_id = product_id
#         self.count = count
#         self.order_date = order_date
#         self.id = id
#
#     def filter_price(self, from_count, to_count):
#         res = []
#         for product in products:
#             if from_count <= product.get("count") <= to_count:
#                 p = Product(**product)
#                 res.append(p)
#         return res
#
#     def count(self,):
#
#
#     def __repr__(self):
#         return f"{self.count}"
#
#
# p = Product()
# print()


# truck 1-namuna
# import json
#
# file = open("truck.json", "r")
# truck = json.load(file)
# file.close()
#
#
# class Truck:
#     def __init__(self,id=None,truck_name=None,car_number=None,status=None,country=None,size=None,date=None):
#         self.id=id
#         self.truck_name=truck_name
#         self.car_number=car_number
#         self.status=status
#         self.country=country
#         self.size=size
#         self.date=date
#     def filter_date(self, from_date, to_date):
#         res=[]
#         for trucks in truck:
#             if from_date <= trucks.get("date") <= to_date:
#                res.append(trucks)
#         return res
#
#     def car_number(self, car_num):
#         res=[]
#         for trucks in truck:
#             if car_num<=trucks.get("car_number"):
#                 res.append(trucks)
#         return self.car_number
#
#
#     def status_search(self, status):
#         for trucks in truck:
#             if trucks["truck_name"]==self.truck_name:
#                 status.append(trucks)
#         return (f"status_search: {status}")
#
#     def add(self):
#         res=[]
#         for trucks in truck:
#             res.append(trucks)
#         return res
#
#
#     def empty_truck_with_country(self, country):
#         res=[]
#         for trucks in truck:
#             if country<=trucks.get("country"):
#                 res.append(trucks)
#         return res
#
#     def filter_size(self, size):
#         res=[]
#         for trucks in truck:
#             if size<=trucks.get("size"):
#                 res.append(trucks)
#         return res

# print(*Truck().filter_date("2023-12-08","2024-01-18"), sep='\n')
# print(f"Car Number: {truck.get_car_number()}")
# print(Truck().status_search == "FINISHED")
# print(Truck.add(2,"GS"))
# print(*Truck().empty_truck_with_country("Russia"),sep='\n')
# print(*Truck().filter_size("XS"),sep='\n')


#{"id": 1, "truck_name": "GS", "car_number": 9710, "status": "FINISHED", "country": "Russia", "size": "XS", "date": "2022-08-24"}


# truck 2-namuna
# import json
# from datetime import date
#
# # type hinting
# file = open("truck.json", "r")
# data: list[dict] = json.load(file)
# file.close()
#
#
# class Truck:
#     def init(self,
#                  id: int = None,
#                  truck_name: str = None,
#                  car_number: int = None,
#                  status: str = None,
#                  country: str = None,
#                  size: str = None,
#                  date: str = None
#                  ) -> None:
#         self.id = id
#         self.truck_name = truck_name
#         self.car_number = car_number
#         self.status = status
#         self.country = country
#         self.size = size
#         self.date = date
#
#     def sequence_id(self):
#         return data[-1].get("id") + 1
#
#     def add(self) -> None:
#         if self.status == "1":
#             status = "START"
#         if self.status == "2":
#             status = "EMPTY"
#         if self.status == "3":
#             status = "PROCESS"
#         if self.status == "4":
#             status = "FINISHED"
#         self.status = status
#         data.append(self.dict)
#
#     def filter_date(self, from_date: str, to_date: str) -> list[dict]:
#         from_date = date.fromisoformat(from_date)
#         to_date = date.fromisoformat(to_date)
#         result = []
#         for truck in data:
#             truck_date = date.fromisoformat(truck.get("date"))
#             if from_date <= truck_date <= to_date:
#                 result.append(truck)
#         return result
#
#     def car_number(self, number: int) -> dict:
#         for truck in data:
#             if truck.get("car_number") == number:
#                 return truck
#
#     def status_search(self, status: str) -> list[dict]:
#         result = []
#         for truck in data:
#             if truck.get("status") == status.upper():
#                 result.append(truck)
#         return result
#
#     def empty_truck_with_country(self, country: str) -> list[dict]:
#         result = []
#         for truck in data:
#             if truck.get("status") == "EMPTY" and truck.get("country") == country.title():
#                 result.append(truck)
#         return result
#
#     def filter_size(self, size: str) -> list[dict]:
#         result = []
#         for truck in data:
#             if size.upper() in truck.get("size"):
#                 result.append(truck)
#         return result
#
#
# status_menu = """
#     1) START
#     2) EMPTY
#     3) PROCESS
#     4) FINISHED
#     >>>"""
#
# size_menu = """
#     1) S
#     2) M
#     3) L
#     4) XS
#     5) XL
#     6) 2XL
#     7) 3XL
#     >>>"""

# truck = {
#     "id" : Truck().sequence_id(),
#     "truck_name" : input("Truck name : "),
#     "car_number" : input("Car number : "),
#     "status" : input(status_menu),
#     "country" : input("Country : "),
#     "size" : input(size_menu),
#     "date" : date.today()
# }

# print(len(data))
# Truck(**truck).add()
# print(len(data))


# print(*Truck().filter_date("2021-01-01", "2023-01-01"), sep= "\n")


# print(Truck().sequence_id())

# print(*Truck().filter_size("X"), sep = "\n")

# print(*Truck().empty_truck_with_country("Hungary") , sep = "\n")


# print(*Truck().status_search("PROCESS"), sep = "\n")
