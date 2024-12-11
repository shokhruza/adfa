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
