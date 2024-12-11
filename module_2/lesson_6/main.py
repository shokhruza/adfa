import bcrypt

salt = bcrypt.gensalt()
password = "1234".encode()
hash_pass = bcrypt.hashpw(password, salt)
check_pass = bcrypt.checkpw("1234".encode(), hash_pass)
print(check_pass)

passwords = []
while True:
    menu = """
    1)add
    2)check
    3)exit
    """
    key = input(menu)
    match key:
        case "1":
            passwords = input("Password: ").encode()

        # case "2":
        #     for hash_pw in passwords:
        #         return("password!")
        #         break
        #     else:
        #         return ("Not found password!")
        # case "3":
        #     return