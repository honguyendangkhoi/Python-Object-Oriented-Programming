import smtplib
from email.message import EmailMessage
import mimetypes

my_email="honguyendangkhoi@gmail.com"
password="favx drjw ygaj vxyu"
to_addrs="dngkhoyy@gmail.com"
subject="Test"
body="Attached file"

msg = EmailMessage()
msg["From"]=my_email
msg["To"]=to_addrs
msg["Subject"]=subject
msg.set_content(body)

file_path= r"C:\Users\Admin\Desktop\PYTHON_UDEMY\SMTP\my_file.txt"

mimetypes, _ = mimetypes.guess_type(file_path) #mime type trả về 2 giá trị, type và file nén, nếu ko dùng cái nào thì _
if mimetypes is None:
    mimetypes="application/octet-stream"

main_type, sub_type = mimetypes.split("/",1)

with open(file_path, "rb") as file:
    msg.add_attachment(file.read(),
                       maintype=main_type,
                       subtype=sub_type,
                       filename="my_file.txt")

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.ehlo() 
    connection.starttls()
    connection.ehlo()
    connection.login(user=my_email,
                    password=password)
    connection.send_message(msg) #msg đã tạo ở đầu file nên gộp luôn, phải tạo EmailMessage
    
print("Email OK")

#bước 1 vào my gg account tạo app passwords
#bước 2 đổi SMTP thành port 587
#bước 3 thêm ehlo() để kiểm tra và kết nối giao thức tới server Gmail
#bước 4 code y chang, \n\n là xuống dòng để ghi nội dung