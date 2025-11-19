import smtplib, pandas, datetime,os,random

connection=smtplib.SMTP("smtp.gmail.com")

my_email="honguyendangkhoi@gmail.com"
password="pgdf azbt ycqt umia"
subject="Happy Birthday"

connection.starttls()
connection.login(user=my_email,password=password)

date=datetime.datetime.now()
date_today=date.day
date_month=date.month

f_csv=r"C:\Users\Admin\Desktop\Test\Python_Test_Labs\birthdays.csv"
f_letters=r"C:\Users\Admin\Desktop\Test\Python_Test_Labs\letter_templates"

with open(f_csv) as file_csv:
    lines=pandas.read_csv(file_csv)
    
    for index, row in lines.iterrows():
        name=row["name"]
        day=row["day"]
        month=row["month"]
        email=row["email"]

        if month==date_month and day==date_today:
            letter_file=os.listdir(f_letters) #os.listdir là nó sẽ list tất cả file trong folder
            choice_letter=random.choice(letter_file)
            with open(os.path.join(f_letters,choice_letter),"r",encoding="utf-8") as file_txt: #os.path.join sẽ nối đường dẫn từ thư mục đến file
                letter=file_txt.read() 
                new_letter = letter.replace("[NAME]",name)
                connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject: {subject}\n\n{new_letter}")
                print("Sent!")

connection.close()

# thứ tự làm:
# Mở kết nối SMTP (chuẩn bị gửi email)
# Lấy ngày hiện tại (để biết ai sinh nhật hôm nay)
# Đọc CSV (lấy dữ liệu người nhận)
# Lặp từng người (xử lý từng người)
# Kiểm tra birthday (chỉ xử lý người đúng hôm nay)
# Chọn template ngẫu nhiên (cá nhân hóa nội dung)
# Mở template và replace [NAME] (tạo email hoàn chỉnh)
# Gửi email (thực hiện hành động cuối cùng)
# Đóng kết nối SMTP (giải phóng tài nguyên)