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
    pprint(alert)
    index='suricataids-bd-alert-'+ datetime.now().strftime("%Y.%m.%d")
    print(index)
    while True:
	signature_list = [signature.rstrip("\n") for signature in open('app/signatures_warning')]
	print(signature_list) 
	res = alert.query(index=index, signature_list = signature_list, interval=30)
	leng = len(res['hits']['hits'])
	if leng > 0:
	    print('find %d alert warning' % leng)
	time.sleep(28)



if __name__ == '__main__': 
    try:
	#suricataAlert()
	#web_thread = threading.Thread(target = httpServer, args=())
	#web_thread.start()
	alert_thread = threading.Thread(target = suricataAlert, args=()) 
	alert_thread.start()
	httpServer()
    except:
	print "ERROR in main"
#    sms = SMS()
#    phones = ['01202996807']
#    res =  sms.sendsms(phones,'naaaaaaaaaaaa')
#    print(res.json())
