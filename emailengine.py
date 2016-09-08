# -*- coding: iso-8859-1 -*-
def emailit(to,filename):
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from smtplib import SMTP

    msg = MIMEMultipart()
    msg['Subject'] = 'Invoice - Sales Management System'
    msg['From'] = 'sms@prateekv.com'
    msg['Reply-to'] = 'sms@prateekv.com'
    msg['To'] = to

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'

    # This is the textual part:
    part = MIMEText("Hello,\nPlease find attached your Invoice for the recent purchase with us. \n\nRegards\nTeam SMS")
    msg.attach(part)

    # This is the binary part(The Attachment):
    part = MIMEApplication(open("BillsGenerated/Bill Number- "+str(filename)+".txt", "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename="Bill Number- "+str(filename)+".txt")
    msg.attach(part)

    # Create an instance in SMTP server
    smtp = SMTP("host5.dnsinweb.com")
    # Start the server:
    smtp.ehlo()
    smtp.login("sms@prateekv.com", "Welcome123")

    # Send the email
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())