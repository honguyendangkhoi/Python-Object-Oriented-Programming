#tạo if input easy thì 10 attemps, hard thì 5 attemps
#lần đầu nhập số bất kỳ, nếu sai thì in ra too low hay too high
#số lần attemps giảm 1 mỗi lần sai
#nhập lại
#đoán đúng thì print you win

import random
import time
print("Number Guessing Game")
rand=random.randint(1,100)
level=input("Number between 1 and 100. Choose a difficulty 'easy' or 'hard': ")

easy_live=["♡","♡","♡","♡","♡","♡","♡","♡","♡","♡"]
hard_live=["♡","♡","♡","♡","♡"]
new_live=[]

def guessing_num():
    if level=='easy':
        choice=int(input("make a guess: "))
        if choice==rand:
            print(f"You won. The number is: {choice}",end="")
            return
        if choice<rand:
            easy_live.pop(0)
            new_live=easy_live
            print("too low")
            print(f"You have {len(new_live)} {'♡ '*len(new_live)}left")
        else:
            print("too high")
            easy_live.pop(0)
            new_live=easy_live
            print(f"You have {len(new_live)} {'♡ '*len(new_live)}left")
        if not easy_live:
            print(f"You lost. The correct number was {rand}")
            return
        return guessing_num()   
                 
    if level=='hard':
        choice=int(input("make a guess: "))
        if choice==rand:
            print(f"You won. The number is: {choice}",end="")
            return
    if choice<rand:
        hard_live.pop(0)
        new_live=hard_live
        print("too low")
        print(f"You have {len(new_live)} {'♡ '*len(new_live)}left")
    else:
        print("too high")
        hard_live.pop(0)
        new_live=hard_live
        print(f"You have {len(new_live)} {'♡ '*len(new_live)}left")
    if not hard_live:
        print(f"You lost. The correct number was {rand}")
        return
    return guessing_num()

guessing_num()