import requests
import urllib
import smtplib
from elasticsearch import Elasticsearch
import sqlite3
import os

class Email():
    def send_gmail(self, rcv_list , message):
	gmail_user = "quy196hp8@gmail.com"
	gmail_pwd = "gbmktzqh"
	SUBJECT = "[ATTT] Canh bao Suricata"
	TEXT = "\nCanh bao Suricata \n\n"+message+"\n\n\n\n"
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_pwd)
	BODY = '\r\n'.join(['From: ATTT VEGA','Subject: %s' % SUBJECT, '', TEXT])
	server.sendmail(gmail_user, rcv_list, BODY)
	server.close()

if __name__ == '__main__':
    pass
