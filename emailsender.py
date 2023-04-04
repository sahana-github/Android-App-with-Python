import smtplib
to = input("Enter the mail of recipent : ")
content = input("Enter the content wanst to write :")
def send(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemailgmail.com','1234')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()

send(to,content)
