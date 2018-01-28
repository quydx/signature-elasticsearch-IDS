import requests
import urllib
import smtplib
from elasticsearch import Elasticsearch
import sqlite3
import os

class Email():
    def __init__(self, list_recipient, message):
	self.list_recipient = list_recipient
	self.message = message    
    def send_gmail(self):
	gmail_user = "quy196hp8@gmail.com"
	gmail_pwd = "gbmktzqh"
	SUBJECT = "[ATTT] Canh bao Suricata"
	TEXT = "\nCanh bao Suricata \n\n"+self.message+"\n\n\n\n"
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_pwd)
	BODY = '\r\n'.join(['From: ATTT VEGA','Subject: %s' % SUBJECT, '', TEXT])
	server.sendmail(gmail_user, self.list_recipient, BODY)
	server.close()

if __name__ == '__main__':
    e =  Email(['quy196hp@gmail.com'], "canh bao suricata")
    e.send_gmail()
