from tkinter import *
from math import floor


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLACK = "#000000"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Inter"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_SEC = WORK_MIN * 60
# SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
# LONG_BREAK_SEC = LONG_BREAK_MIN * 60
WORK_SEC = 15
SHORT_BREAK_SEC = 15
LONG_BREAK_SEC = 15
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startTimer():
    global reps
    
    reps+=1      
    
    if reps%8==0:
        countDown(LONG_BREAK_SEC)
        titleLabel.config(text="Long Break", fg=RED)
        timerLabel["text"] = "LBREAK"
    elif reps%2==0:
        countDown(SHORT_BREAK_SEC)
        titleLabel.config(text="Short Break", fg=PINK)
    else:
        countDown(WORK_SEC)
        titleLabel.config(text="Work", fg=GREEN)
    
      

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    
    minutes = floor(count/60)
    seconds = count%60
    
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    
    canvas.itemconfig(timerText, text=f"00:{minutes}:{seconds}")
    
    if count > 0:
        window.after(1000, countDown, count-1)
    else:
        startTimer()
        marks = ""
        workSessions = floor(reps/2)
        for _ in range(workSessions):
            marks += "✓"
        checkLabel.config(text=f"{marks} Completed Sessions: {workSessions}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro GUI Project")
window.config(padx=100, pady=100, bg=YELLOW)


titleLabel = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
titleLabel.grid(column=1, row=0)

startBtn = Button(text="Start", highlightthickness=0, command=startTimer)
startBtn.grid(column=0, row=3)

resetBtn = Button(text="Reset", highlightthickness=0)
resetBtn.grid(column=2, row=3)

checkLabel = Label(bg=YELLOW, fg=BLACK, highlightthickness=0)
checkLabel.grid(column=1, row=5)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)


window.mainloop()