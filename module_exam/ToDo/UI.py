from error import ErrorMessage
from module_exam.ToDo.model.user import User
class UserUI:

    def register(self):
        user = {
            "id": User(),
            "fullname": input("Fullname : "),
            "phone_number": input("Phone number : "),
        }
        user = User(**user)
        user.is_valid()
        user.save()
        UI().main()

    def login(self):
        global session_user
        auth = {
            "phone_number": input("Phone number : ")
        }
        user = User(**auth)
        session_user = user.is_auth()
        self.account()

    def update_field(self):
        try:
            print(session_user.__dict__)
            menu = """
                1) fullname
                2) phone_number
                0) <= back
                >>>"""
            key = input(menu)
            if key == "0":
                self.settings()
                return
            field = User.get(key)
            new_val = input("New value : ")
            User(id=session_user.id).update(field, new_val)
            self.account()
        except ErrorMessage as messsage:
            print(messsage)
            self.settings()

    def settings(self):
        global session_user
        menu = """
            1) update profile
            2) delete account
            0) <-back
        """
        match input(menu):
            case "1":
                self.update_field()
            case "2":
                y_n = input("Are you sure [y/N] : ")
                if y_n == 'y':
                    User(id=session_user.id).delete()
                    session_user = None
                    UI().main()
                self.settings()
            case "0":
                self.account()


class TodoUI:
    pass
class UI:
    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exits
                >>>"""

            match input(menu):
                case "1":
                    UserUI().register()
                case "2":
                    UserUI().login()
                case "3":
                    return
        except ErrorMessage as message:
            print(message)
            self.main()


UI().main()
