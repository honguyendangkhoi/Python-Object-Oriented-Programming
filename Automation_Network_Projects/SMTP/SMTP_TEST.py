import smtplib
import requests
import datetime
import json

dt=datetime
now=dt.datetime.now()
dict_now={"current time":now.isoformat()}
json_str=json.dumps(dict_now,indent=4)

with open("date_now.json","w") as file:
    json.dump(dict_now,file,indent=4)

print(json_str)

with open("date_now.json","r") as f:
    date_from_file = json.load(f)

for k,v in date_from_file.items():
    print(f"after Json: {k} = {v}")

# nghĩa là trước đó mình có output là "current time": "2025-11-19T10:32:25.848039"
# và current time là key còn "...." là value
# thì mình lặp từng key và value trong cái file này
# xong rồi mình in ra key = value cho dễ đọc

my_email="honguyendangkhoi@gmail.com"
password="jywf zftw fcay aaet"
receive_email="dngkhoyy@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email, password=password)
send=connection.sendmail(from_addr=my_email,to_addrs=receive_email,msg="Hello")
try: 
    send == True
    print("send completed")
except SyntaxError or IndexError:
    print(f"lỗi {SyntaxError} {IndexError}")

connection.close()
