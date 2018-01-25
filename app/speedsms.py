import requests
from os import popen, system
import os

class SMS:
    def __init__(self):    
	self.access_token = 'vqbeRcnpuntXmmASaWeHFbWhtcje5v8H'
    
    def send_sms(self, content):
	data = {
	    "to": ["01202996807"], 
	    "content": content, 
	    "sms_type": 2, 
	    "sender": "Suricata alert"
	    } 
	self.access_token
	str_data = str(data).replace("'", "\"")
	cmd ='curl -i -u "%s" -H "Content-Type: application/json" -X POST -d \'%s\' http://api.speedsms.vn/index.php/sms/send' %( self.access_token, str_data)
	print(cmd)
	system(cmd)

    def sendsms(self, phone_number, content):
	pstr = ''
	for number in phone_number:
	    pstr += "%s,"%number

	pstr = pstr.rstrip(",")
	print('pstr = ', pstr)
	headers = {
		'Content-Type': 'application/json',
		}
	data = {
	    "to": [pstr], 
	    "content": content, 
	    "sms_type": 2, 
	    "sender": "Suricata alert"
	    }  
	str_data = str(data).replace("'", "\"")
	response = requests.post('http://api.speedsms.vn/index.php/sms/send', headers=headers, data=str_data, auth=(self.access_token, ''))
	return response

    def getUserInfo(self):
	response = requests.get('http://api.speedsms.vn/index.php/user/info', auth=(self.access_token, 'x'))
	return response

if __name__ == '__main__':
    phones = ['01202996807']
    sms = SMS()
    res =  sms.sendsms(phones,'abc')
    print(res.json())







