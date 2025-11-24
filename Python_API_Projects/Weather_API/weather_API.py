import requests,smtplib, os
from twilio.rest import Client

account_sid="AC1108fb378ee9fff442294926fd293904"
auth_token = "8109fddfe7b34ff840e5428c6ccc5b1a"

api_keys="2cdf31b7f1b2bc63a9e7facf8808d410"
Endpoin_site="https://api.openweathermap.org/data/2.5/forecast"

parameters={
    "appid":api_keys,
    "cnt":4,
    "lat":10.823099, #phai dat dung ten
    "lon":106.629662,
}

response=requests.get(url=Endpoin_site,params=parameters)
response.raise_for_status()

data=response.json()
# id_weather_data=data["list"][0]["weather"][0]["id"] #gọi nó bằng index, 

will_rain=False
for hour_data in data["list"]:      #mở từng dấu ngoặc vuông để truy cập vô index của nó
    hour_check=hour_data["weather"][0]["id"]
    if int(hour_check) < 700:
        will_rain=True
if will_rain:
    my_email="honguyendangkhoi@gmail.com"
    password="pgdf azbt ycqt umia"
    receive_email="dngkhoyy@gmail.com"
    subject="Rainning Alert"
    msg=f"Subject: {subject}\n\n Bring Raincoat" #phai co Subject: 

    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs=receive_email,
                        msg=msg.encode("utf-8"))
    client= Client(account_sid,auth_token)
    message=client.messages.create(
        to="",
        from_="+19472215926",
        body="Bring Umbrella",
    )
    print(message.status)
    print("Sent!")

else:
    print("Nothing")