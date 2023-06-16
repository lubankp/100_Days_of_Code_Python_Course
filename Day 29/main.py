from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- PASSWORD SEARCH ------------------------------- #

def search():
    webside_name = entry_webside.get()
    try:
        with open("./password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message=f"There is no file to open!")
    else:
        if webside_name in data:
            password = data[webside_name]["password"]
            email = data[webside_name]["email"]
            entry_password.delete(0, END)
            entry_password.insert(0, password)
            messagebox.showinfo(title=webside_name, message=f"Email: {email}\n Password: {password}\n")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"There is no such data!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = entry_username.get()
    webside = entry_webside.get()
    password = entry_password.get()
    new_data = {
        webside: {
            "email": email,
            "password": password,
        }
    }

    if len(webside) == 0 or len(password) == 0:
        messagebox.showinfo(title="Info", message=f"At least one field empty!")
    else:
        try:
            with open("./password.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            data = new_data
        finally:
            with open("./password.json", "w") as file:
                json.dump(data, file, indent=4)

                entry_webside.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# Labels

label_webside = Label(text="Webside:")
label_webside.grid(row=1, column=0)

label_username = Label(text="Email/username:")
label_username.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Button

button_search = Button(width=14, text="Search", command=search)
button_search.grid(row=1, column=2)

button_generate = Button(text="Generate Password", command=generate)
button_generate.grid(row=3, column=2)

button_add = Button(width=43, text="Add", command=save)
button_add.grid(row=4, column=1, columnspan=2)

# Entry

entry_webside = Entry(width=32)
entry_webside.grid(row=1, column=1)
entry_webside.focus()

entry_username = Entry(width=50)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "pawel.lubanski.91@gmail.com")

entry_password = Entry(width=32)
entry_password.grid(row=3, column=1)



window.mainloop()