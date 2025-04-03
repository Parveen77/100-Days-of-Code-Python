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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60 
    long_break_secs = LONG_BREAK_MIN * 60
    

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        title.config(text="Work", fg=GREEN)
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min < 10:
        count_min = f"0{count_min}"
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔️"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)
#window.minsize(width=500, height=500)


tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
canvas.create_image(100 , 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30), fill="white")
canvas.grid(column=1, row=1)

title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text="")
checkmark.grid(column=1, row=3)


window.mainloop()