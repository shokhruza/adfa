from new_project.ToDo.config import BASE_PATH
from os.path import join
from json import dump, load

DB_PATH = join(BASE_PATH, "database")


class File:
    @classmethod
    def all(cls) -> list:
        file_name = cls.__name__.lower() + "s.json"
        with open(join(DB_PATH, file_name), "r") as f:
            data = load(f)

        for i, dict_ in enumerate(data):
            data[i] = cls(**dict_)
        return data

    @classmethod
    def write(cls, data: list) -> None:
        file_name = cls.__name__.lower() + "s.json"
        for i, obj in enumerate(data):
            data[i] = obj.__dict__
        with open(join(DB_PATH, file_name), "w") as f:
            dump(data, f, indent=3)


"""
id
fullname
email # unique
password
join_at
"""

#
# user = User(1 , "Botir" , 'botir@gmail.com' , '1111' , '2024-02-22')
#
# print(User().write([user , user]))
# print(User().all())
