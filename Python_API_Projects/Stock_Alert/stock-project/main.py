import requests, smtplib, os
from email.message import EmailMessage

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":"IBM",
    "interval":"60min",
    "apikey":"",
}

url_web="https://www.alphavantage.co/query"

response = requests.get(url=url_web,params=parameters)
response.raise_for_status()
data=response.json()

daily_data=data["Time Series (Daily)"] #de duyet dict long thi tao 2 bien xong for items roi truy cap phan tu binh thuong

sorted_dates=sorted(daily_data.keys()) #hoc thuoc cach duyet qua tung dict

trend_dict={}

for i in range(len(sorted_dates)-1):
    old_date=sorted_dates[i] #i=0 la ngay hien tai
    new_date=sorted_dates[i+1] #i+1 la ngay tiep theo
    old_close=float(daily_data[old_date]["4. close"])
    new_close=float(daily_data[new_date]["4. close"])

    if new_close>old_close*1.05:
        trend_dict[new_date]="Increase"
    elif old_close*0.95>new_close:
        trend_dict[new_date]="Decrease"
    else:
        trend_dict[new_date]="Stable"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_param={
    "apiKey":"",
    "q":COMPANY_NAME,
}
news_url="https://newsapi.org/v2/everything"

news=requests.get(url=news_url,params=news_param)
news.raise_for_status()

data_news=news.json()

my_email=""
password=os.environ["EMAIL_PASSWORD"]
receive_email=""

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email,password=password)

msg=EmailMessage()
subject="Stock Alert"
msg['Subject']=subject
msg['From'] = my_email
msg['To'] = receive_email

all_trends=trend_dict.values()

if "Increase" in all_trends or "Decrease" in all_trends:
    message_lines = []

# Duyệt từng ngày có biến động giá
for date, trend in trend_dict.items():
    if trend in ["Increase", "Decrease"]:
        old_close = float(daily_data[sorted_dates[sorted_dates.index(date)-1]]["4. close"])
        new_close = float(daily_data[date]["4. close"])
        change_percent = round(((new_close - old_close) / old_close) * 100, 2) #Làm tròn
        arrow = "🔺" if change_percent > 0 else "🔻"

        for article in data_news["articles"][:3]: #Slicing
            title = article.get("title", "No title") #truyền thêm biến No title phòng trường hợp không có title
            description = article.get("description", "No description")
            message_lines.append(
                f"{STOCK}: {arrow}{abs(change_percent)}%\n"
                f"Headline: {title}\n"
                f"Brief: {description}\n"
            )

# Nối tất cả message
final_message = "\n".join(message_lines)
msg.set_content(final_message)
connection.send_message(msg)
connection.quit()

# with open("trend.txt","w") as file:
#     for date,trend in trend_dict.items():
#         if trend=="Stable": #dùng trend vì trend là value trong vòng lặp
#             file.write("")
#         else:
#             file.write(f"{date}: {trend}\n")

# with open("trend.txt","r") as f_open:
#     content=f_open.read()
#     print(content)

