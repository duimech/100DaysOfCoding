# This program is a pomodoro timer using a graphical interface. 25 mins of work, 5 mins break - repeat 4 times, then 20 mins break
# Author: Ray Bolin
# Date: 2/4/2022
# 100DaysOfCoding

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_timer.config(text="Timer", fg=GREEN)
    lbl_checkmarks.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    # Timer countdown calls count_down function and passes amount of time
    if REPS in range(1, 8, 2):
        lbl_timer.config(text="Work", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
        count_down(WORK_MIN * 60)
    elif REPS in range(2, 7, 2):
        lbl_timer.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Break", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Format the seconds less than 10 seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            checkmarks += "✔"

        lbl_checkmarks.config(text=checkmarks)



# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Window background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="100DaysOfCoding/pomodoroTimer/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(105,140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1,column=1)

# Top Label
lbl_timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
lbl_timer.grid(row=0,column=1)

# Bottom Labels
lbl_checkmarks = Label(text="", font=(FONT_NAME, 25, "normal"), bg=YELLOW, fg=GREEN)
lbl_checkmarks.grid(row=3, column=1)

# Bottom Buttons
lbl_start = Button(text="Start", highlightthickness=0, command=start_timer)
lbl_start.grid(row=2,column=0)

lbl_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
lbl_reset.grid(row=2,column=2)


# Keep the window open
window.mainloop()