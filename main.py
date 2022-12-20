from tkinter import *



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Inter"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro GUI Project")
window.config(padx=100, pady=100, bg=YELLOW)


timerLabel = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timerLabel.grid(column=1, row=0)

startBtn = Button(text="Start", highlightthickness=0)
startBtn.grid(column=0, row=3)

resetBtn = Button(text="Reset", highlightthickness=0)
resetBtn.grid(column=2, row=3)

checkBtn = Label(text="✓", bg=YELLOW, fg=GREEN, highlightthickness=0)
checkBtn.grid(column=1, row=5)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="Pomodoro GUI Project/tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)





window.mainloop()