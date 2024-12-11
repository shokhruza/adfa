from abc import ABC, abstractmethod
import random
from new_project.telegram_messenger.error import ErrorMessage
from new_project.telegram_messenger.model.tmp import UserDTO


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
    def is_valid(self):
        if len(self.phone_number) != 13:
            raise ErrorMessage("Invalid phone Number!")
        self.username_valid()

    def sequence_id(self):
        users = self.user_list()
        return int(users[-1].id) + 1 if users else 1

    def send_code(self):
        code = str(random.randrange(100_000, 1_000_000))
        with open("/new_project/telegram_messenger/phone_message.txt", "w") as f:
            f.write(code)

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

    def save(self):
        users = self.user_list()
        users.append(self)
        UserDTO.write(users)

    def username_valid(self):
        users = self.user_list()
        for user in users:
            if self.username == user.username:
                return False
        return True

    def update(self, filed, new_val):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                if filed == "fullname":
                    user.fullname = new_val
                elif filed == "username":
                    self.username = new_val
                    if not self.username_valid():
                        return False, "Already exits"
                    user.username = new_val
                elif filed == "bio":
                    user.bio = new_val
                elif filed == "photo":
                    user.photo = new_val
        UserDTO.write(users)

    def delete(self, id):
        users = self.user_list()
        for user in users:
            if user.id == self.id:
                users.remove(user)
        UserDTO.write(users)

    def user_list(self):
        u = UserDTO
        users: list[UserDTO] = u.read()
        return users

    def get(self):
        users: list[UserDTO] = self.user_list()
        for user in users:
            if user.id == self.id:
                return user
