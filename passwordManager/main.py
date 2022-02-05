# This program is a graphical password manager and password generator. 
# Author: Ray Bolin
# Date: 2/4/2022
# 100DaysOfCoding

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    in_password.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # List comprehension for letters, numbers, and symbols
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    # Combine all the lists into a single list
    password_list = password_letters + password_numbers + password_symbols

    # Make the password list random
    random.shuffle(password_list)

    # Convert the elements in the list into a string with no characters/spacing
    password = "".join(password_list)

    # Place new password into the input box for the password
    in_password.insert(0, password)

    # Copy the new password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = in_website.get()
    email = in_email_username.get()
    password = in_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Fill in all of the fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm the details:\n \n Website: {website}\nEmail: {email}\n Password: {password}")

        if is_ok:
            with open("100DaysOfCoding/passwordManager/data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password} \n")

            in_website.delete(0,END)
            in_password.delete(0,END)

            messagebox.showinfo(title="Confirmation", message="The password has been added successfully.")

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, highlightthickness=0)

# Window background
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="100DaysOfCoding/passwordManager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)
in_website = Entry(width=45)
in_website.focus()
in_website.grid(row=1, column=1, columnspan=2)

# Email and Username 
lbl_email_username = Label(text="Email/Username:")
lbl_email_username.grid(row=2, column=0)
in_email_username = Entry(width=45)
in_email_username.insert(0, "email@domain.com")
in_email_username.grid(row=2, column=1, columnspan=2)

# Password
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)
in_password = Entry(width=25)
in_password.grid(row=3, column=1)
btn_password = Button(text="Generate Password", command=gen_password)
btn_password.grid(row=3, column=2)

# Add
btn_add = Button(text="Add", width=42, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)


window.mainloop()