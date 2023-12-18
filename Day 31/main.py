from tkinter import *
import json
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
choice = 0
timer = 0

# ---------------------------- FUNCTIONS ------------------------------- # 
def right_execute():
    global choice
    global df
    window.after_cancel(timer)
    mask = df.index.isin([choice])
    df = df[~mask].reset_index(drop=True)
    df.to_csv('data/unknown_words.csv')
    df = pd.read_csv('data/unknown_words.csv')
    canvas.itemconfig(image_canvas,image=front )
    canvas.itemconfig(language_text,fill="black", text="French")
    canvas.itemconfig(word_text,fill="black", text=df.loc[choice,"French"])
    canvas.grid(row=0,column=1, columnspan=3)
    countdown(3)

def left_execute():
    global choice
    window.after_cancel(timer)
    choice = choice+1
    canvas.itemconfig(image_canvas,image=front )
    canvas.itemconfig(language_text,fill="black", text="French")
    canvas.itemconfig(word_text,fill="black", text=df.loc[choice,"French"])
    canvas.grid(row=0,column=1, columnspan=3)
    countdown(3)

def countdown(count):
    global choice
    global timer

    count-=1
    if count>=0:
        timer = window.after(1000, countdown, count)
    else:
        canvas.itemconfig(image_canvas,image=back )
        canvas.itemconfig(language_text,fill="white", text="English")
        canvas.itemconfig(word_text,fill="white", text=df.loc[choice,"English"])
        canvas.grid(row=0,column=1, columnspan=3)
        right_button.config(command=right_execute)
        wrong_button.config(command=left_execute)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady=50, bg=BACKGROUND_COLOR)
try:
    df = pd.read_csv('data/unknown_words.csv')
except:
    df = pd.read_csv('data/french_words.csv')
choice = random.randint(0,df.shape[0])

canvas = Canvas(width = 800,height = 526,highlightthickness=0, bg=BACKGROUND_COLOR)
back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")

image_canvas = canvas.create_image(400,263,image=front)
language_text = canvas.create_text(400,186,text="French",fill="black", font=(FONT_NAME,35,"italic"))
word_text = canvas.create_text(400,272,text=df.loc[choice,"French"],fill="black", font=(FONT_NAME,45,"bold"))
canvas.grid(row=0,column=1, columnspan=3)


right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

wrong_button = Button(image=wrong,bg=BACKGROUND_COLOR, command=left_execute)
wrong_button.grid(row=1, column=1)

right_button = Button(image=right,bg=BACKGROUND_COLOR, command=right_execute)
right_button.grid(row=1, column=3)
countdown(3)





# label1 = Label(text="Website: ",font=('Courier',12, "bold"), bg="white")
# label1.grid(row=1,column=0)

# entry1= Entry(width=21)
# entry1.grid(row=1,column=1)

# label2 = Label(text="Email/Username: ",font=('Courier',12, "bold"), bg="white")
# label2.grid(row=2,column=0)

# entry2= Entry(width=42)
# entry2.insert(END,string="sidharthv24@gmail.com")
# entry2.grid(row=2,column=1, columnspan=2)

# label3 = Label(text="Password: ",font=('Courier',12, "bold"), bg="white")
# label3.grid(row=3,column=0)

# entry3= Entry(width=21)
# entry3.grid(row=3,column=1)

# button1 = Button(text="Generate", command=show_password, width=15, bg="white",font=('Courier',10, "bold"))
# button1.grid(row=3, column=2)

# button2 = Button(text="Add", command=add_password,width=36, bg="white",font=('Courier',10, "bold"))
# button2.grid(row=4, column=1, columnspan=2)

# button3 = Button(text="Search", bg="white",command=search, width=15,font=('Courier',10, "bold"))
# button3.grid(row=1, column=2)

window.mainloop()