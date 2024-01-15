import smtplib

email = "si99alt@gmail.com"
password = 'test'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=email, password=password)