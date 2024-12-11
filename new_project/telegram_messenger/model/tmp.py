from datetime import datetime
DATABASE_PATH = "/new_project/telegram_messenger/database"


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


class UserDTO(File):
    def __init__(self,
                 id=None,
                 fullname=None,
                 username=None,
                 phone_number=None,
                 bio=None,
                 photo=None):
        self.id = id
        self.username = username
        self.bio = bio
        self.phone_number = phone_number
        self.fullname = fullname
        self.photo = photo


class ChannelDTO(File):
    def __init__(self,
                 id=None,
                 name=None,
                 username=None,
                 admin_id=None):
        self.id = id
        self.name = name
        self.username = username
        self.admin_id = admin_id




class ChannelsMemberDTO(File):
    def __init__(self,
                 id=None,
                 channel_id=None,
                 user_id=None
                 ):
        self.id = id
        self.channel_id = channel_id
        self.user_id = user_id



class ContactDTO(File):
    def __init__(self,
                 id=None,
                 user_id=None,
                 owner_id=None
                 ):
        self.id = id
        self.user_id = user_id
        self.owner_id = owner_id



class GroupDTO(File):
    def __init__(self,
                 id=None,
                 name=None,
                 status=None,
                 description=None,
                 username=None,
                 admin_id=None
                 ):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.username = username
        self.admin_id = admin_id



class GroupMemberDTO(File):
    def __init__(self,
                 id=None,
                 group_id=None,
                 user_id=None
                 ):
        self.id = id
        self.group_id = group_id
        self.user_id = user_id


class MessageDTO(File):
    def __init__(self,
                 id=None,
                 type=None,
                 message=None,
                 status=None,
                 to_receiver_id = None,
                 send_user_id =None,
                 date_time=str(datetime.now())
                 ):
        self.id = id
        self.type = type
        self.message = message
        self.status = status
        self.to_receiver_id=to_receiver_id
        self.send_user_id=send_user_id
        self.date_time=date_time





# TODO -> ChannelDTO, ChannelsMemberDTO, ContactDTO, GroupDTO, GroupMemberDTO , MessageDTO
