users: list[dict] = [
    {
        "id": 1,
        "first_name": "admin",
        "last_name": "admin",
        "birth_day": "2000-01-01",
        "phone": "+998993456789",
        "username": "admin",  # unique
        "password": "admin_01",
        "roll": "ADMIN",
        "courses_id": []
    }
]
"""
{
    "id" : 1,
    "first_name" : "ism",
    "last_name" : "familya",
    "birth_day" : "2000-01-01",
    "phone" : "+998993456789",
    "username" : "username", # unique
    "password" : "admin_01", 
    "roll" : "ADMIN" or "STUDENT",
    "course_id" : 2
}
"""

"""
{
    "id" : 1,
    "name" : "nomi",  # unique
    "number_of_students" : "studentlar soni",
    "is_active" : True or False,
}
"""

courses: list[dict] = []
session_user: dict | None = None


class User:
    def __init__(self,
                 id=None,
                 first_name=None,
                 last_name=None,
                 birth_day=None,
                 phone=None,
                 username=None,
                 password=None,
                 roll="STUDENT",
                 courses_id=None
                 ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day
        self.phone = phone
        self.username = username
        self.password = password
        self.roll = roll
        self.courses_id = courses_id

    def sequence_id(self):
        return users[-1].get("id")+1 if users else 1

    def check_username(self):
        for user in users:
            if user.get("username")==self.username:
                return True, "Already exits username!"
            return False, "Success save!"


    def is_auth(self):
        for user in users:
            if user.get("username") == self.username and user.get("password")==self.password:
                return user

    def save(self):
        users.append(self.__dict__)

    def is_admin(self):
        for user in users:
            if user.get("roll") == "ADMIN":
                return True
            return False

    def add_courses_id(self, course_id):
        for user in users:
            if user.get("id")==self.id:
                user["courses_id"]+= [course_id]
                break


class Course:

    def __init__(self,
                 id=None,
                 name=None,
                 number_of_students=0,
                 is_active=True):
        self.id = id
        self.name = name
        self.number_of_students = number_of_students
        self.is_active = is_active

    def self_courses(self, student_id):
        result = []
        courses_list = []
        for user in users:
            if user.get("id")==student_id:
                courses_list = user.get("courses_id")
        for course in courses:
            if course.get("id") in courses_list:
                result.append(course)
        return result

    def active_courses(self):
        result=[]
        for  course in courses:
            if course.get("is_active"):
                result.append(course)
        return result

    def sequence_id(self):
        return courses[-1].get("id") + 1 if courses else 1

    def save(self):
        courses.append(self.__dict__)

    def is_exists(self):
        for course in courses:
            if course.get("name")==self.name:
                return True, "Already exits name!"
            return False, "Success save!"


    def course_list(self):
        return courses

    def student_course(self, course_id):
        result = []
        for user in users:
            if course_id in user.get("courses_id"):
                result.append(user)
            return result


        # number_of_students


class Admin:
    def admin_account(self):
        global session_user
        menu = """
            1) Course add
            2) SHow Students
            0) log out
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.course_add()
            case "2":
                pass
            case "3":
                return

    def course_add(self):
        pass


class UI:

    def choose_course(self) -> int:
        pass

    def register(self):
        pass

    def main(self):
        menu = """
            1) Sign up
            2) Sign in
            3) exit
            >>>"""
        key: str = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def login(self):
        pass


class Student:

    def active_course_show(self):
        pass

    def join_course(self):
        pass

    def student_menu(self):
        global session_user
        menu = """
            1) Course list (+active)
            2) Join to course
            3) Self courses
            0) log out
            >>>"""
        key = input(menu)
        pass


UI().main()
