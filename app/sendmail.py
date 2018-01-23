#!/usr/bin/python

import smtplib
sender = ''
receivers = []

message = """

"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender , receiver, message)
    print('Send mail to successful!')
except SMTPException:
    print('Send mail unsuccessful!')
