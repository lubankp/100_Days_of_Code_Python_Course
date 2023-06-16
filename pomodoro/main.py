from tkinter import *
import math
from playsound import playsound
import os

# for playing note.wav file

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
reps = 0
timer = None
current_dir = os.getcwd()
file_path_song = current_dir + '/song.mp3'
file_path_image = current_dir + '/tomato.png'

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    label_name.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text="30:00")
    label_counter.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = 1 * WORK_MIN
    short_brake_sec = 1 * SHORT_BREAK_MIN
    long_brake_sec = 1 * LONG_BREAK_MIN
    reps += 1

    if reps % 8 == 0:
        count_down(long_brake_sec)
        label_name.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        label_name.config(text="Break", fg=PINK)
    elif reps < 9:
        count_down(work_sec)
        label_name.config(text="Work", fg=GREEN)
    else:
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global timer
    min_count = int(count / 60)
    sec_count = count % 60
    f_count = f"{min_count}:{sec_count:02d}"
    canvas.itemconfig(canvas_text, text=f_count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        playsound(file_path_song)
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✓"
        label_counter.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=file_path_image)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="30:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=2, column=2)

# Labels
label_name = Label(text="Timer", font=(FONT_NAME, 32, "bold"))
label_name.grid(row=1, column=2)
label_name.config(padx=20, pady=20, bg=YELLOW, fg=GREEN)

label_counter = Label(text="", font=(FONT_NAME, 20, "bold"))
label_counter.grid(row=4, column=2)
label_counter.config(padx=20, pady=20, bg=YELLOW, fg=GREEN)


# Buttons


button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
button_reset.grid(row=3, column=3)





window.mainloop()