import smtplib
from email.message import EmailMessage

email = EmailMessage()

question1 = input("Please enter your email: ")
question2 = input("Now your password: ")
question3 = input("What is your name?")
question4 = input("And you are sending an email to...?")
question5 = input("What is the subject?")
question6 = input("Please enter the content.")

email["from"] = question3
email["to"] = question4
email["subject"] = question5

email.set_content(question6)
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(question1, question2)
    smtp.send_message(email)
    print("done!")
