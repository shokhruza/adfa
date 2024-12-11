from module_3.lesson_5.ToDo.config import Hash
from module_3.lesson_5.ToDo.errors.main import ErrorMessage
from module_3.lesson_5.ToDo.model.db_control import File


class User(File):
    def __init__(self,
                 id: int = None,
                 fullname: str = None,
                 email: str = None,
                 password: str = None,
                 join_at: str = None):
        self.id = id
        self.fullname = fullname  # length(word) == 2
        self.email = email  # unique
        self.password = password  # length > 4
        self.join_at = join_at

    def sequence_id(self):
        users: list[User] = self.all()
        return users[-1].id + 1 if users else 1

    def is_unique_email(self):
        users: list[User] = self.all()
        for user in users:
            if user.email == self.email:
                return False
            return True

    def is_valid(self):
        users: list[User] = self.all()
        if len(self.fullname.split()) != 2:
            raise ErrorMessage(" Invalid fullname! ")
        if len(self.password) < 4:
            raise ErrorMessage(" Invalid password! ")
        if not self.email.endswith("@gmail.com"):
            raise ErrorMessage(" Invalid email!, EXAMPLE:your@gmail.com")
        if not self.is_unique_email():
            raise ErrorMessage("Already exits email!")

    def save(self):
        users: list[User] = self.all()
        self.password = Hash(self.password).hashpw()
        users.append(self)
        self.write(users)

    def is_auth(self):
        users: list[User] = self.all()
        for user in users:
            if user.email == self.email and Hash(self.password, user.password).checkpw():
                return user
            raise ErrorMessage(" Not Found Account! ")

    def __repr__(self):
        return f"{self.fullname}"
