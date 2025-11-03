alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ")
text=input("type your message:\n ").lower()
shift=int(input("Type the shift number:\n "))

def encrypt(text,shift):
    new_text=[]
    if direction == 'encode':
        letter=text
        for letter in text:
            if letter in alphabet:
                index=alphabet.index(letter)
                index_new=(index+shift)%26
                new_text.append(alphabet[index_new])
        print(f"your code: {''.join(new_text)}")


def decrypt(text,shift):
    new_text=[]
    if direction == 'decode':
        letter=text
        for letter in text:
            if letter in alphabet:
                index=alphabet.index(letter)
                index_new=(index-shift)%26
                new_text.append(alphabet[index_new])
        print(f"your code: {''.join(new_text)}")

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("not in option !")

#nen them 1 dong lua chon ham o ngoai neu co nhieu ham de tranh bi loi