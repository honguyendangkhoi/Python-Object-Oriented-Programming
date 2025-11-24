import smtplib, datetime, random

dt=datetime.datetime.now()
week_day=dt.weekday()

my_email=""
password=""
receive_email=""

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email,password=password)

with open("quotes.txt","r",encoding="utf-8") as file: 
    data=file.readlines() #nếu là file txt thì phải dùng readlines còn json thì mới dùng json    
    try:
        data_from_file=random.choice(data).strip() #strip để bò xuống dòng
        if not data_from_file: #nếu rỗng
            raise ValueError("Quote rỗng") #nếu có lỗi thì raise nhảy tới except chứa lỗi, còn không thì nó tự out code luôn
    except ValueError as e:
        print(f"lỗi: {e}")
    else:
        if week_day==2:
            msg=f"Subject: Motivation Quotes\n\n{data_from_file}"
            connection.sendmail(from_addr=my_email,
                                to_addrs=receive_email,
                                msg=msg.encode("utf-8"))
            print("Sent !")
        else:
            print("Not Wednesday")

connection.close()