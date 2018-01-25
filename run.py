from app import app 
from app.mail import *
from app.speedsms import *
if __name__ == '__main__': 
    sms = SMS()
    phones = ['01202996807']
    res =  sms.sendsms(phones,'naaaaaaaaaaaa')
    print(res.json())
    app.run(host='0.0.0.0', port=80, debug=True)  
