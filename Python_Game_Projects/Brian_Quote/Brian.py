from tkinter import *
import random,os
from PIL import Image, ImageTk

os.chdir(r"C:\Users\Admin\Desktop\PYTHON_UDEMY\Python_API_Projects\Brian_Quote")

with open("Brian_Quotes.txt","r",encoding="utf-8") as file:
    data=file.readlines()
    data=[line.strip() for line in data]
    
    try:
        data_from_file=random.choice(data)
        if not data_from_file:
            raise ValueError("file rong")
    
    except ValueError as e:
        print(f"loi {e}")
    
    else:
        window = Tk()
        window.title("Brian Says...")
        window.config(padx=50, pady=50)

        canvas = Canvas(width=300, height=414)
        background_img = PhotoImage(file="background.png")
        canvas.create_image(150, 207, image=background_img)
        quote_text = canvas.create_text(150, 207, text="Brian Quote Goes HERE", width=300, font=("Arial", 17, "bold"), fill="white")
        canvas.grid(row=0, column=0)

        def get_quote():
            new_quote=random.choice(data)
            canvas.itemconfig(quote_text,text=new_quote)
        
        brian_img = ImageTk.PhotoImage(Image.open("brian.png"))
        brian_button = Button(image=brian_img, highlightthickness=0, command=get_quote)
        brian_button.grid(row=1, column=0)

        window.mainloop()