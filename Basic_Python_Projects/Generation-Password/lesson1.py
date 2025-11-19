import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2''3','4','5','6','7','8','9','0']
symbols=['!','#','$','@','%','^','&',"8",'(',')']

lt=int(input("how many letters you want?: "))
num=int(input("how many letters you want?: "))
sym=int(input("how many symbols you want?: "))

password_list=[]
for char in range(0,lt):
        password_list.append(random.choice(letters))
for char in range(0,num):
        password_list.append(random.choice(numbers))
for char in range(0,sym):
        password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
        password+=char

print(f"password: {password}")