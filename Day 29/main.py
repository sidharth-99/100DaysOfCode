from tkinter import *
from tkinter import messagebox
import json
import random
# import pyperclip install this to add copy to clipboard for password

# ---------------------------- Search ------------------------------- #
def search():
    website = entry1.get()
    with open('data.json','r') as file:
        data = json.load(file)
        try: 
            message = f'''
                These are the details
                Email - {data[website]['Email']}
                Password - {data[website]['Email']}
                '''
            messagebox.showinfo(title="Passowrd Found!!" , message=message)
        except KeyError:
            messagebox.showinfo(title="Oops" , message="No Passwords found for this website")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def show_password():
    password = generate_password()
    entry3.delete(0,END)
    entry3.insert(END,string=f"{password}")
    # pyperclip.copy(password) to copy in clipboard

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    r_letters = [random.choice(letters) for i in range(nr_letters)]
    r_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    r_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password_list = r_letters+r_numbers+r_symbols
    random.shuffle(password_list)
    password_str = "".join(password_list)

    return password_str

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    
    new_dict = {

        website:{
            'Email':email,
            'Password':password
        }
    }

    message = f'''
    These are the details added
    Website - {website}
    Email - {email}
    Password - {password}
    Is it OK?
    '''
    if len(website)==0 or len(email)==0:
        messagebox.showinfo(title="Oops" , message="Please Make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=entry1, message=message)
    
        if is_ok:
            # try:
            #     open("data.json","r")
            # except FileNotFoundError:
            #     open("data.json", "w")
            # with open("data.json","r") as file:#r for reading
            #     # json.dump(new_dict, file, indent=4) not correct as just appending won't work
            #     data = json.load(file)
            #     data.update(new_dict)

            # with open("data.json","w") as file:
            #     json.dump(data, file, indent=4)
            #     entry1.delete(0,END)
            #     entry3.delete(0,END)
            
            # Earlier code was wrong

                try:
                    with open("data.json","r") as file:#r for reading
                        # json.dump(new_dict, file, indent=4) not correct as just appending won't work
                        data = json.load(file)
                except FileNotFoundError:
                        with open("data.json","w") as file:
                             json.dump(new_dict,file, indent=4)

                else:    
                    data.update(new_dict)

                    with open("data.json","w") as file:
                        json.dump(data, file, indent=4)
                finally:
                    entry1.delete(0,END)
                    entry3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50, bg="White")

canvas = Canvas(width = 200,height = 200,highlightthickness=0, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

label1 = Label(text="Website: ",font=('Courier',12, "bold"), bg="white")
label1.grid(row=1,column=0)

entry1= Entry(width=21)
entry1.grid(row=1,column=1)

label2 = Label(text="Email/Username: ",font=('Courier',12, "bold"), bg="white")
label2.grid(row=2,column=0)

entry2= Entry(width=42)
entry2.insert(END,string="sidharthv24@gmail.com")
entry2.grid(row=2,column=1, columnspan=2)

label3 = Label(text="Password: ",font=('Courier',12, "bold"), bg="white")
label3.grid(row=3,column=0)

entry3= Entry(width=21)
entry3.grid(row=3,column=1)

button1 = Button(text="Generate", command=show_password, width=15, bg="white",font=('Courier',10, "bold"))
button1.grid(row=3, column=2)

button2 = Button(text="Add", command=add_password,width=36, bg="white",font=('Courier',10, "bold"))
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text="Search", bg="white",command=search, width=15,font=('Courier',10, "bold"))
button3.grid(row=1, column=2)

window.mainloop()