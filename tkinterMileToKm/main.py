# This program is a mile to kilometer converter. This is my first program using tkinter.
# Author: Ray Bolin
# Date: 2/2/2022
# 100DaysOfCoding

from tkinter import *

def button_click():
    miles = float(input.get())
    km = miles * 1.609
    lbl_answer.config(text=km)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# Labels
lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2, row=0)
lbl_equalto = Label(text="is equal to")
lbl_equalto.grid(column=0, row=1)
lbl_km = Label(text="Km")
lbl_km.grid(column=2, row=1)
lbl_answer = Label(text="0")
lbl_answer.grid(column=1, row=1)

# Buttons
btn_calculate = Button(text="Calculate", command=button_click)
btn_calculate.grid(column=1, row=2)


# Entry (Input)
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()