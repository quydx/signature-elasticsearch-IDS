import requests
from os import popen, system
import os

access_token = 'vqbeRcnpuntXmmASaWeHFbWhtcje5v8H'

def send_sms(content):
    data = {
	"to": ["01202996807"], 
	"content": content, 
	"sms_type": 2, 
	"sender": "Suricata alert"
	} 
    global access_token
    str_data = str(data).replace("'", "\"")
    cmd ='curl -i -u "%s" -H "Content-Type: application/json" -X POST -d \'%s\' http://api.speedsms.vn/index.php/sms/send' %(access_token, str_data)
    print(cmd)
    system(cmd)

def sendsms(phone_number, content):
    global access_token
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
    response = requests.post('http://api.speedsms.vn/index.php/sms/send', headers=headers, data=str_data, auth=(access_token, 'Gbmktzqh1@'))
    return response

def getUserInfo():
    global access_token
    response = requests.get('http://api.speedsms.vn/index.php/user/info', auth=(access_token, 'x'))
    return response

if __name__ == '__main__':
    phones = ['01202996807']
    res =  sendsms(phones,'abc')
    print(res.json())







