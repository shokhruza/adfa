# 2 ta son uchun :  EKUK , EKUB


# pip install secure-smtplib
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "shokhruzaibodova@gmail.com"  # Enter your address
receiver_email = input("shokhruzaibodova@gmail.com")  # Enter receiver address
password = "qrckvacdvqqylkcw"
message = f"""
How to create amessage box in HTML?
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
