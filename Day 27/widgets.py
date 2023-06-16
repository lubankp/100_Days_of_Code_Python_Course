# # Label
#
# my_label = Label(text="I am label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label["text"] = "New Text"
#
# # Entry
#
# input = Entry(width=30)
# input.insert(END, string="Some text to entry")
# input.pack()
#
# # Button
#
# def button_click():
#     in_text = input.get()
#     my_label.config(text=f"{in_text}")
#
# button = Button(text="Click Me", command=button_click)
# button.pack()
#
# # Text
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of text")
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
# def checkbutton_used():
#     print(check_state.get())
#
# check_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
# checkbutton.pack()
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
# radio_state = IntVar()
# radiobutton1 =Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 =Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# # Listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits=["Apple", "Orange", "Pear", "Bannana"]
#
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
#
