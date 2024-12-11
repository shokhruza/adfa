# import threading
# import os
# import time
# import json
#
# def function(num):
#     time.sleep(2)
#     print(10 * num)
#     print("process id: ", os.getpid())
#
#
# start = time.time()
# t1 = threading.Thread(target=function, args=(1,))
# t2 = threading.Thread(target=function, args=(2,))
# t3 = threading.Thread(target=function, args=(3,))
# t4 = threading.Thread(target=function, args=(4,))
# t5 = threading.Thread(target=function, args=(5,))
# t6 = threading.Thread(target=function, args=(6,))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
#
# print(time.time() - start)


# import threading
# import os
# import time
#
#
# def function1():
#     time.sleep(2)
#     print("function1", os.getpid())
#
#
# def function2():
#     time.sleep(3)
#     print("function2", os.getpid())
#
#
# def function3():
#     time.sleep(1)
#     print("function3", os.getpid())
#
#
# def function4():
#     time.sleep(5)
#     print("function4", os.getpid())
#
#
# f = [function1, function2, function3, function4]
# start = time.time()
# threads = []
# for i in f:
#     t = threading.Thread(target=i)
#     t.start()
#     threads.append(t)
#     for thread in threads:
#         thread.join()
#
# print(time.time() - start)


# pip install secure-smtplib
import smtplib, ssl
import threading
import os
import time

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "shokhruzaibodova@gmail.com"  # Enter your address
receiver_email = input("shokhruzaibodova@gmail.com")  # Enter receiver address
password = "qrckvacdvqqylkcw"
message = f"""
send message
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



start = time.time()

print(time.time() - start)
