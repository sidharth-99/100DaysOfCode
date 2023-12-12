from tkinter import *

window =  Tk()
window.title("My first GUI")
window.minsize(height=500,width=700)
my_label = Label(text='Hello World', font=('Arial',26))
my_label.pack()

my_label["text"] = 'Heyy'#can be used to change like this

# Button

button = Button(text='Hey')
button.pack()

def clicked():
    label =  Label(text='Got clicked', font=('Arial',26))
    label.pack()
    # print("i got clicked")

def existing_click():
    my_label.config(text=input.get())
    my_label.place(x=0,y=10)#Place can be used to define the correct layout
    # my_label.grid(row=2,column=10)#won'rt change the layout as there is noo components before it, basically grid is used to make each component in each grid
    #also will throw error as pack, place and grid cannot be intermixed

# button2 = Button(text ="click me",anchor='center', command=clicked)
# button2.pack()

button2 = Button(text ="click me",anchor='center', command=existing_click)
button2.pack()

# Entry
input = Entry()
input.pack()


window.mainloop()