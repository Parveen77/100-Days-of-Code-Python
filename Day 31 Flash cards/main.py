BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import json
import random

#--------------------------Right------------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:    
    data = pandas.read_csv("data/french_words.csv")
finally:
    dict = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    canvas.itemconfigure(language_name, text = "French", fill = "black")
    canvas.itemconfigure(language_word, text = current_card["French"], fill = "black")
    canvas.itemconfigure(card_background, image = card_back_image)
    flip_timer = window.after(3000, func= flip_card)

    
def flip_card():
    canvas.itemconfigure(language_name, text = "English")
    canvas.itemconfigure(language_word, text = current_card["English"])
    canvas.itemconfigure(card_background, image = card_front_image)
#----------------------------wrong answer---------------------------------#
#create a file named words to learn
def is_known():
    dict.remove(current_card)
    data  = pandas.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
#---------------------------UI Design-------------------------------------#

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip_card)
#card back
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file = "./images/card_front.png")
card_back_image = PhotoImage(file = "./images/card_back.png")
card_background = canvas.create_image(400 , 263, image = card_front_image)
language_name = canvas.create_text(400, 150, text="Title", font=("Aerial", 40, "italic"), fill="white")
language_word = canvas.create_text(400, 263, text="word", font=("Aerial", 60, "bold"), fill="white")
canvas.grid(column=0, row=0, columnspan=2)

#card back


#buttons
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1,row=1)
right_button.config(padx=50, highlightthickness=0)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=1)
wrong_button.config(padx=50, highlightthickness=0)

next_card( )





window.mainloop()

