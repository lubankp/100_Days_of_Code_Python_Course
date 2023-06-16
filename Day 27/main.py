from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Label

my_label_1 = Label(text="Miles", font=("Arial", 16))
my_label_1.grid(row=1, column=3)
my_label_1.config(padx=20, pady=20)

my_label_2 = Label(text="Km", font=("Arial", 16))
my_label_2.grid(row=2, column=3)
my_label_2.config(padx=20, pady=20)

my_label_3 = Label(text="is equal to", font=("Arial", 16))
my_label_3.grid(row=2, column=1)
my_label_3.config(padx=20, pady=20)

my_label_4 = Label(text="0", font=("Arial", 16))
my_label_4.grid(row=2, column=2)
my_label_4.config(padx=20, pady=20)

# Entry

input = Entry(width=10, font=("Arial", 16))
input.insert(END, string="0")
input.grid(row=1, column=2)

# Button

def button_click():
    val_miles = input.get()
    val_km = round(float(val_miles) * 1.609, 2)
    my_label_4.config(text=f"{val_km}")

button = Button(text="Calculate", command=button_click, font=("Arial", 16))
button.grid(row=3, column=2)

window.mainloop()