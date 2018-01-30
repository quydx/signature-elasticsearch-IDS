from app import app 
from app.mail import *
from app.speedsms import *
from es_realtime_alert import ESAlert
import threading
from elasticsearch import Elasticsearch
from datetime import datetime
from pprint import pprint
import time


def httpServer(): 
    app.run(host='0.0.0.0', port=80, debug=True) 

def suricataAlert():
    alert = ESAlert('192.168.158.74', 9200)
    index='suricataids-bd-alert-'+ datetime.now().strftime("%Y.%m.%d")
    email = Email()
    sms = SMS()
    phones = ['01202996807']
    message = "ATTT Suricata Alert \n"
    rcv_list = ['quy196hp@gmail.com']
    count = 0
    while True:
	signature_list = [signature.rstrip("\n") for signature in open('app/signatures_warning')]
	for sign in signature_list :
	    res = alert.query(index=index, signature_list = [sign], interval=300)
	    all_hits = res['hits']['hits']
	    leng = len(all_hits)
	    count += leng
	    list_src_ip = []
	    if leng > 0:
		for hit in all_hits:
		    ip = hit['_source']['src_ip']
		    if ip not in list_src_ip:
			list_src_ip.append(ip)
		ip_list = ",".join(ip for ip in list_src_ip)
		message += "%s :%s: %d hits :source ip %s\n" %(all_hits[0]['_source']['timestamp'], sign , leng, ip_list)
	if count > 0:
	    email.send_gmail(rcv_list, message)
	    print('A warning email was sent')
	    #sms.sendsms(phones, message)
	time.sleep(295)
	
if __name__ == '__main__': 
    #suricataAlert()
    #alert_thread = threading.Thread(target = suricataAlert, args=()) 
    #alert_thread.start()
    httpServer()
