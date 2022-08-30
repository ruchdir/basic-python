from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'ruchdi.dev@gmail.com'
email_password = 'cympgyrkmpeycekm'

#https://temp-mail.org/
email_receiver = 'podewo3589@rxcay.com'
subject = 'Test Send Mail'
body = """
  Test send mail from Python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())

