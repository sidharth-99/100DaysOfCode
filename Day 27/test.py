import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(height=500,width=700)
my_label = tkinter.Label(text="Hello World", font=('Arial',26))
my_label.pack()
# my_label.pack(anchor='ne')
# my_label.pack(side='left')
# my_label.pack(expand=True)

window.mainloop()