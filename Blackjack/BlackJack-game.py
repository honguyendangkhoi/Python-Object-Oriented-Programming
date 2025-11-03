import random
import time
print("BLACKJACK GAME")

def blackjack():
    over=True
    rand=random.randint(1,10)
    rand1=random.randint(1,10)
    your_card=rand+rand1

    rand=random.randint(1,10)
    rand1=random.randint(1,10)
    opponent_card=rand + rand1

    while opponent_card < 17:
        rand=random.randint(1,10)
        if opponent_card + rand > 21:
            break
        opponent_card+=rand

    print(f"your card: {your_card}")
    if your_card==21:
        print("BLACKJACK")
        pass
    else:
        choice=input("draw ? (d) or stop ? (s): ")

        while over != False:
            if choice == 'd':
                rand1=random.randint(1,10)
                your_card+=rand1
                print(f"your card: {your_card}")
                if your_card > 21:
                    print("busted")
                    break
                choice=input("draw ? (d) or stop ? (s): ")
            else:
                print("your opponent card is", end="")
                time.sleep(1)
                print(f": {opponent_card}")

                if 21 >= your_card > opponent_card:
                    print("YOU WON")
                elif your_card<opponent_card<=21:
                    print("YOU LOSE")
                elif opponent_card>21 and 16<=your_card<=21:
                    print("YOU WON")
                elif your_card>21:
                    print("BUSTED")
                    break
                elif your_card==21 and your_card > opponent_card:
                    print("YOU WON")
                elif your_card==opponent_card:
                    print("DRAW")

                over=False

blackjack()