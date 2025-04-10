from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40,"italic")
WORD_FONT = ("Ariel", 60, "bold")

#-----------------------WORD RETRIEVAL------------------------#

words = pandas.read_csv("./data/french_words.csv")
words_dict = words.to_dict(orient="records")
def next_card():
    sample_dict = random.choice(words_dict)
    french_word = sample_dict["French"]
    card_canvas.itemconfig(language_text, text="French")
    card_canvas.itemconfig(word_text, text=french_word)








#----------------------------UI-------------------------------#
window = Tk()
window.title("Flashcard Game")
window.config(background=BACKGROUND_COLOR, height=600, width=900, padx=50,pady=50)
card_canvas = Canvas(window, height=550, width=810, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
card_canvas.create_image(400, 270, image=card_img)
language_text = card_canvas.create_text(400,150, text="Language", font=LANGUAGE_FONT)
word_text = card_canvas.create_text(400,263, text="Word", font=WORD_FONT)
card_canvas.config(background=BACKGROUND_COLOR)
card_canvas.grid(column=0, row=0, columnspan=2)
x_img = PhotoImage(file="./images/wrong.png")
x_btn = Button(image=x_img, highlightthickness=0, command=next_card)
x_btn.grid(column=0, row=1, pady=25)
chk_img = PhotoImage(file="./images/right.png")
chk_btn = Button(image=chk_img, highlightthickness=0, command=next_card)
chk_btn.grid(column=1, row=1, pady=25)

next_card()


window.mainloop()