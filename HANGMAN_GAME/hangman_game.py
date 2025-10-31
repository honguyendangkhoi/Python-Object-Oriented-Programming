import random
word_list=["mouse","dog","cat"]
heart=["♡","♡","♡","♡","♡"]

chosen_word=random.choice(word_list)

#tao ham de hien chu da doan dung #tao ham de choi tiep
#hien underscore
word_length=len(chosen_word)
placeholder=""

for position in range(word_length):
    placeholder="_"
    print(placeholder,end="")

game_over=False #tao flag
guessed_word=[]

#xu ly logic
while not game_over:
    guess=input("\nguess a letter: ").lower()
    print(guess)

    display=""

    #in underscore
    for letter in chosen_word:
        if letter == guess:
            display+=letter #cho trong se duoc thay bang chu
            guessed_word.append(letter)
        elif letter in guessed_word:
            display+=letter
        else:
            display+="_"       
    
    if guess not in chosen_word:
        print(f"letter {guess} is not in list\n")
        heart.remove("♡")
        print(f"you have {len(heart)}*♡ left\n")

    print(display)
    if "_" not in display:
        print(f"\nthe answer is: {chosen_word}")
        print("You won")
        game_over=True
    elif heart==[]:
        print("You lose")
        game_over=True