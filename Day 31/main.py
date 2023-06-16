# Imports

from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"


random_card = {}

#-------------------------If words_to_learn-------------------------------#

def take_data():

    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv")
    finally:
        return data.to_dict(orient="records")


# ----------------------------- Turn Card --------------------------#
def turn_card():
    canvas_card.itemconfig(canvas_image, image=back_img)
    canvas_card.itemconfig(canvas_text, text=random_card["English"], fill="white")
    canvas_card.itemconfig(canvas_text_lg, text="English", fill="white")

# ----------------------------- Next Card --------------------------#
def next_card():
    global random_card
    global data_dict
    global flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(data_dict)
    canvas_card.itemconfig(canvas_text, text=random_card["French"], fill="black")
    canvas_card.itemconfig(canvas_text_lg, text="French", fill="black")
    canvas_card.itemconfig(canvas_image, image=front_img)

    flip_timer = window.after(3000, turn_card)

# ---------------------------- Wrong clicked  ------------------------- #
def wrong_clicked():
    next_card()



# ---------------------------- Right clicked  ------------------------- #
def right_clicked():
    data_dict.remove(random_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, turn_card)

# Canvas front
canvas_card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas_card.create_image(400, 263, image=front_img)
canvas_text_lg = canvas_card.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
canvas_text = canvas_card.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas_card.grid(row=1, column=1, columnspan=2)

back_img = PhotoImage(file="./images/card_back.png")


# Canvas right

right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_clicked)
button_right.grid(row=2, column=2)


# Canvas NOK
wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_clicked)
button_wrong.grid(row=2, column=1)

data_dict = take_data()
next_card()



window.mainloop()