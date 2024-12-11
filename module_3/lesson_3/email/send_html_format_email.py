import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shokhruzaibodova@gmail.com"
receiver_email = "shokhruzaibodova@gmail.com"
password = "qrckvacdvqqylkcw"
message = MIMEMultipart("alternative")
message["Subject"] = "How to create a message box in HTML?"
message["From"] = sender_email
message["To"] = receiver_email
html = """
<html>
  <body>
        <p>Hi,<br>
           How are you?<br>
           <b><a href="http://www.realpython.com">Real Python</a></b> 
           <a href="http://t.me/TUIT_AI">My account</a>
           <button>click</button>
           has many great tutorials.
        </p>
  </body>
</html>
"""
part2 = MIMEText(html, "html")
message.attach(part2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
