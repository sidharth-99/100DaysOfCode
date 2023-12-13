from tkinter import *
import time
import math

##Change the timings to actually use the program
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
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'''00:00''')
    label.config(text="Timer",fg=GREEN)
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_symbol
    reps+=1
    if reps%8==0:
       label.config(text="Break",fg=RED)
       countdown(5 ) 
    elif reps%2==0:
        label.config(text="Break",fg=PINK)
        countdown(4 )
    else: 
        countdown(5 )
        label.config(text="Work",fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    minute = math.floor(count/60)
    second = count%60
    global timer

    # if second == 0:
    #     second = "00"
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f'''{minute}:{second}''')
    count-=1
    if count>=0:
        timer = window.after(1000,countdown,count)
    else:
        start_timer()
        marks=""
        for i in range(math.floor(reps/2)):
            marks+="✔"
            check.config(text=marks)

    
    # time.sleep(1)
    # label.config(text=f"{i}")  #time.sleep doesn't work as we are inside mainloop and since it's event driven, 
    # sleeping would just wouldn't update the values 


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady=50, bg=YELLOW)
check="✔"

label = Label(text="Timer",font=(FONT_NAME,50,"bold"),bg=YELLOW, fg=GREEN)
label.grid(row=0,column=1)

canvas = Canvas(width = 200,height = 250,bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,125,image=tomato_img)
timer_text = canvas.create_text(100,140,text='00:00',fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

# start_button = Button(text="Start", highlightthickness=0, command=countdown(5)) didn't work maybe cuz after func
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3,column=1)

window.mainloop()