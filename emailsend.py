# eMail
import smtplib

sender_email_addr = "sender@live.com"
receiver_email_addr = "empfaenger@eprovider.com"
password = "sender_password"
message = "Das ist die zu sendende Nachricht."

server = smtplib.SMTP("smtp.live.com", 587)
server.starttls()
server.login(sender_email_addr, password)
print("Login erfolgreich.")
server.sendmail(sender_email_addr, receiver_email_addr, message)
print("eMail verschickt.")
server.close()
