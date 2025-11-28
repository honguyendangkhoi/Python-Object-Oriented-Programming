import requests,os
from datetime import datetime

x_app_id=os.environ["APP_ID"]
x_app_key=os.environ["API_KEY"]

url="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_url="https://api.sheety.co/8580c85f137bab42cbd34eb29a98131e/myWorkouts/sheet1"

query_dict={
    "run":{"type":"cardio"},
    "swim":{"type":"cardio"},
    "walk":{"type":"cardio"},
    "cycle":{"type":"cardio"},
    "weightlifting":{"type":"cardio"},
}

query_list=[]

user_query=input("Type your exercises (run / swim / walk / cycle / weightlifting): ").lower()
ex_list=user_query.split()

flag=False
while flag!=True:
    for ex_l in ex_list:
        if ex_l in query_dict:
            query_list.append(ex_l)
            value = query_dict[ex_l]
            flag=True
        else:
            user_query=input("Type your exercises again: ")
            if user_query in query_dict: #kiểm tra trong dict thì cứ in thôi
                query_list.append(user_query)
                flag=True #ko cần gán vào result nữa vì result chỉ để kiểm tra điều kiện if và lấy biến trong def ra để dùng

duration_list=[]

for i in range(len(query_list)): #mỗi bài 1 thời gian khác nhau
    user_duration=float(input(f"Type your duration times for {query_list[i]} (min): "))
    ex_name=query_list[i]
    duration_list.append(user_duration)
    dur=duration_list[i]

weight_flag=False
while not weight_flag: #chạy đến khi flag = true
    user_weight=int(input("Type your weight: "))
    if user_weight>=30:
        weight_flag=True
    else:
        print("Invalid weight ! Type again")

height_flag=False
while not height_flag:
    user_height=float(input("Type your height (cm): "))
    if user_height >= 100:
        height_flag=True
    else:
        print("invalid height ! Type again")

age_flag=False
while not age_flag:
    user_age=int(input("Type your age: "))
    if user_age > 0:
        age_flag=True
    else:
        print("Type your age again: ")

gender_list=[
    "male",
    "female",
]

user_gender=""

while user_gender not in gender_list:
    user_gender=input("Type your gender (male/female): ").lower()
    if user_gender not in gender_list:
        print("invalid gender ! Type again")

if user_gender in gender_list:
    valid_gender=user_gender
else:
    user_gender=input("Type your gender (male/female): ")
    valid_gender=user_gender

nutrition_data={
    "query": ", ".join(query_list), #.join là nối các phần tử trong list thành string lẻ, nhớ cái này
    "weight_kg":user_weight,
    "height_cm":user_height,
    "age":user_age,
    "gender":valid_gender,
    "duration_time":dur,
}

headers={
    "x-app-id":x_app_id,
    "x-app-key":x_app_key,
}

total_calories=0
total_duration=0
exercise_names = [] #logic: tạo 1 list rỗng trước rồi add vô xong duyệt qua từng string trong list

for ex_data in query_list: #duyệt exercises trong result_data và chuyển về index phải >0
    nutrition_data={"query":ex_data} #gán ex_data mới vào query trong dict
    response=requests.post(url=url,json=nutrition_data,headers=headers) #ý tưởng gửi từng request cho mỗi API
    result_data=response.json() #gán tên riêng cho từng bài tập
    
    for ex_result in result_data["exercises"]: #gán từng ex riêng
        exercise_names.append(ex_result["name"].title()) #append vô list thôi
        total_calories += ex_result["nf_calories"]
        total_duration += ex_result["duration_min"]

today_date=datetime.now().strftime("%d/%m/%Y")
now_date=datetime.now().strftime("%X")

exer_names=" + ".join(exercise_names)

sheet_inputs={
    "sheet1":{
        "date":today_date,
        "time":now_date,
        "exercises":exer_names,
        "duration":total_duration,
        "calories":total_calories,
    }
}

sheet_response=requests.post(url=sheety_url,json=sheet_inputs)

print(sheet_response.text)