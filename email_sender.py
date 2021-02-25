import smtplib
from email.message import EmailMessage


def SendEmail(user_email, name):
    # user_email = self.user_email
    # name = self.name
    email = EmailMessage()
    #text in 'From Field' in email
    email['from'] = "YourNextEmployee@gmail.com"
    #email address to send to
    email['to'] = user_email
    #Email subject
    email['subject'] = 'Time to setup interview?'

    #Email body contect, can be in text, html, ect..
    email.set_content(f"Hi {name}, \n \t I'm sending you this from a python email program I built. I also scrapped linkedin using python to get your email. Hope you don't mind, and hope to talk to you soon for an interview.")

    #below code logs into email server, composes email, then sends, prints to console when completed.
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        #The line below is the loggin info for the email client to send from. ('Username/email', 'password')
        smtp.login('email', 'password')
        smtp.send_message(email)


