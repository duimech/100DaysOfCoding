# This program is a set of flashcards showing Vietnamese to English translation.
# Author: Ray Bolin
# Date: 2/7/2022
# 100DaysOfCoding

from tkinter import *
import pandas
import random

#--------------------------------- CONSTANTS / VARIABLES---------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE = "Vietnamese"
TRANSLATED_LANGUAGE = "English"
TIMER = 5

try:
    df = pandas.read_csv("100DaysOfCoding/capstoneFlashCards/data/to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("100DaysOfCoding/capstoneFlashCards/data/vietnamese_top_100_words.csv")
finally:
    # Using orient="records" makes it return a list of dictionaries
    word_dictionary = df.to_dict(orient="records")

#--------------------------------- OTHER FUNCTIONS ---------------------------------#

def count_down(count):
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        flip_card(next_card_key)


def next_card():
    window.after_cancel(TIMER)

    global next_card_key
    next_card_key = random.choice(word_dictionary)

    canvas.itemconfig(canvas_language, text=LANGUAGE, fill="black")
    canvas.itemconfig(canvas_word, text=f"{next_card_key[LANGUAGE]}", fill="black")
    canvas.itemconfig(canvas_image, image=canvas_card_front)

    # Wait 5 seconds and flip the card
    count_down(5)


def flip_card(next_card_key):
    canvas.itemconfig(canvas_language, text=TRANSLATED_LANGUAGE, fill="white")
    canvas.itemconfig(canvas_word, text=f"{next_card_key[TRANSLATED_LANGUAGE]}", fill="white")
    canvas.itemconfig(canvas_image, image=canvas_card_back)

    
def delete_key():
    # User knows the word so remove it and then overwrite the to_learn.csv file with the remaining words to learn
    word_dictionary.remove(next_card_key)

    remaining_items = pandas.DataFrame(word_dictionary)
    with open("100DaysOfCoding/capstoneFlashCards/data/to_learn.csv", mode="w") as data_file:
        remaining_items.to_csv(data_file, index=False)

    next_card()

#--------------------------------- UI SETUP ---------------------------------#

# Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card_front = PhotoImage(file="100DaysOfCoding/capstoneFlashCards/images/card_front.png")
canvas_card_back = PhotoImage(file="100DaysOfCoding/capstoneFlashCards/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=canvas_card_front)
canvas_language = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
canvas_word = canvas.create_text(400, 300, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
red_x = PhotoImage(file="100DaysOfCoding/capstoneFlashCards/images/wrong.png")
btn_red_x = Button(image=red_x, highlightthickness=0, command=next_card)
btn_red_x.grid(row=1, column=0)

green_check = PhotoImage(file="100DaysOfCoding/capstoneFlashCards/images/right.png")
btn_green_check = Button(image=green_check, highlightthickness=0, command=delete_key)
btn_green_check.grid(row=1, column=1)


#--------------------------------- RUN PROGRAM ---------------------------------#

# Update the canvas text for Language and Word
next_card()

# Keep Window Open
window.mainloop()