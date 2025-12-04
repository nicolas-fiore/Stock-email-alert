from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib
import os


def alert():
    content = open_file()
    print(content)
    send_email(content)



def open_file(): 
    with open('final.txt', 'r') as file: 
        file = file.read()
        return file



def send_email(message):
    load_dotenv()
    email = os.getenv("EMAIL") 
    password = os.getenv("PASSWORD")
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Portfolio Update"
    message["From"] = email
    message["To"] = email
    
    part1 = MIMEText(open_file(), "plain")
    message.attach(part1)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server: 
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message.as_string())



if __name__ == "__main__": 
    alert()

#! EXAMPLE
# text = """\
# Testing to see if this works {time}
# Lests GOOOOOOOOOOOO"""

# html = """\
# <html>
#     <head>
#         <body>
#             <p style="color:red;">Testing to see if this works """ +time+ """</p>
#             <p>Lests <b>GOOOOOOOOOOOO</b>
#         </body>
#     </head>
# </html>
# """
#! EXAMPLE



# part2 = MIMEText(html, "html")

# message.attach(part2)

