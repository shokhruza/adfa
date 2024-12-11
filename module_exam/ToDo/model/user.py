from abc import ABC, abstractmethod
from module_exam.ToDo.model.tmp import UserDTO
from module_exam.ToDo.error import ErrorMessage
import random

class AbstractCRUD(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self, filed, new_val):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get(self):
        pass


class User(UserDTO, AbstractCRUD):
    def user_list(self):
        u = UserDTO
        users: list[UserDTO] = u.read()
        return users

    def is_auth(self):
        users = self.user_list()
        for user in users:
            if user.phone_number == self.phone_number:
                code = self.send_code()
                input_code = input("Code >>>")
                if not input_code == code:
                    return "Wrong code"
                return user
        return "Not found"

    def username_valid(self):
        users = self.user_list()
        for user in users:
            if self.username == user.username:
                return False
        return True

    def is_valid(self):
        if len(self.phone_number) != 13:
            raise ErrorMessage("Invalid phone Number!")
        self.username_valid()


    def update(self, filed, new_val):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                if filed == "fullname":
                    user.fullname = new_val
        UserDTO.write(users)


    def delete(self, id):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                users.remove(user)
        UserDTO.write(users)

    def save(self):
        users = self.user_list()
        users.append(self)
        UserDTO.write(users)

    def send_code(self):
        code = str(random.randrange(100_000, 1_000_000))
        with open("C:/Users/HP Victus/PycharmProjects/python_P21/module_exam/ToDo/database/password.txt ", "w") as f:
            f.write(code)