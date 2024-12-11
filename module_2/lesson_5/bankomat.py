import json

file = open("cards.json", "r")
cards = json.load(file)
file.close()

card: list[dict] = [
    {
        "id": 1,
        "card_number": 2826875762989573,
        "expire": "2024-03",
        "password": 6175,
        "balance": 81580.06
    }
]


class Card:
    def __init__(self,
                 id=None,
                 card_number=None,
                 expire=None,
                 password=None,
                 balance=81580.06):
        self.id = id
        self.card_number = card_number
        self.expire = expire
        self.password = password
        self.balance = balance

    def sequence_id(self):
        return cards[-1].get("id") + 1 if cards else 1

    def card_number(self, car_num):
        res = []
        for card in cards:
            if car_num <= card.get("card_number"):
                res.append(card)
        return self.card_number

    def card_expiration(self):
        for card in self.expire:
            if card.get("expire") == self.expire:
                return True
        return False

    def check_password(self):
        for card in self.password:
            if card.get("password") == self.password:
                return True
        return False

    def card_balance(self):
        return self.balance


class UI:
    def register(self):

        menu = """
        
                 1)KARTA MABLAG'INI KO'RISH>>>
                 2)NAQD PUL YECHISH>>>
                 3)MOBIL OPERATORLARGA TO'LOV QILISH>>>
                 0)LOG OUT>>>  
                   
                """
        key = input(menu)
        match key:
            case "1":
                self.card_summ()
            case "2":
                self.cash_withdrawal()
            case "3":
                self.pay_to_the_phone()
            case "0":
                self.main()

    def card_summ(self):
        return 81580.06

    def cash_withdrawal(self):
        pass

    def pay_to_the_phone(self):
        pass

    def main(self):
        print("               ========Enter card========        ")
        menu = """
                    1) PASSWORD >>>
                    0) LOG OUT >>>
                    """
        key: str = input(menu)
        match key:
            case "1":
                self.register()
            case "0":
                return


UI().main()

# {"id":1,"card_number":2826875762989573,"expire":"2024-03","password":6175,"balance":81580.06}
# bankomat
# ----------------------
# cards
#     id
#     card_number
#     expire
#     password
#     balance
# --------------------------
#
# ------------------ TZ ------------------------
# 1) enter card
#     card_number>>>
#     password>>>
#     expire>>>
#         1) transfer
#             to_card>>>
#             sum>>>
#
#         2) paynet
#         2) log out
# 2) exit