DATABASE_PATH = "/module_exam/ToDo_/database"

class File:
    @classmethod
    def read(cls) -> list:
        file_name=f"{cls.__name__.lower()[:-3]}s.txt"
        file_path=f"{DATABASE_PATH}/{file_name}"
        with open(file_path, 'r') as f:
            data = f.read().split('\n')
        if data == ['']:
            data = []
        result = []
        for item in data:
            obj=cls(*item.split('|'))
            result.append(obj)
        return result

    @classmethod
    def write(cls,data: list) -> None:
        file_name = f"{cls.__name__.lower()[:-3]}s.txt"
        file_path = f"{DATABASE_PATH}/{file_name}"
        for item, obj in enumerate(data):
            data[item] = "|".join(map(str, obj.__dict__.values()))
        str_data = "\n".join(data)
        with open(file_path, "w") as f:
            f.write(str_data)

class UserDTO:
    def __init__(self,
                 id=None,
                 fullname=None,
                 phone_number=None,
                 password=None
                 ):
        self.id=id
        self.fullname=fullname
        self.phone_number=phone_number
        self.password=password
class TodoDTO:
    def __init__(self,
                 id=None,
                 title=None,
                 description=None,
                 completed=bool,
                 data_time=None,
                 join_date=None
                 ):
        self.id=id
        self.title=title
        self.description=description
        self.completed=completed
        self.data_time=data_time
        self.join_date=join_date
