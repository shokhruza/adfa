from datetime import date

users: list[dict] = []


class Base:
    def __init__(self, date):
        self.date = date

    def sequence_id(self):
        return self.date[-1].get("id") + 1 if self.date else 1


class User(Base):
    def __init__(self,
                 data=None,
                 id=None,
                 username=None,
                 fullname=None,
                 password=None,
                 join_date=None):
        super().__init__(data)
        self.id = id
        self.username = username
        self.fullname = fullname
        self.password = password
        self.join_date = join_date

    def check_username(self):
        for user in self.date:
            if user.get("username") == self.username:
                return True, "Accaunt already exits"
        return False, "Success"

    def is_login(self):
        for user in self.date:
            if user.get("username") == self.username and user.get("password") == self.password:
                return True
        return False

    def save(self):
        user = self.__dict__
        del user["date"]
        users.append(user)


class UI:
    def register(self):
        print("============= REGISTER =================")
        user = {
            "id": User(data=users).sequence_id(),
            "fullname": input("Fullname:"),
            "username": input("Username:"),
            "password": input("Password:"),
            "join_date": date.today()
        }
        user = User(**user, data=users)
        response:tuple = user.check_username()
        if response[0]:
            user.save()
        print(response[1])
        self.main()

    def login(self):
        print("============= LOGIN =================")
        user = {
            "username": input("Username : "),
            "password": input("Password : ")
        }
        user = User(**user, data=users)
        response:bool = user.is_login()
        if response:
            self.account()
            return
        print("Not found account")
        self.main()


    def account(self):
        print("WELCOME!")

    def main(self):
        menu = """
        1)REGISTER
        2)LOGIN
        3)EXIT
        >>>
        """
        key: str = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return


UI().main()
