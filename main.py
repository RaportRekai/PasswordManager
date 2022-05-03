from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
FONT1= "Courier"
FONT2= " Futura"
PINK = "#9bdeac"
RED = "#D81B60"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    pass_entry.delete(0, 'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0,password)
    del password
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    password = pass_entry.get()
    username = user_entry.get()
    website = web_entry.get()
    new_data = {website:{"email": username, "password": password}}
    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="ERROR", message="Field Empty")
    else:
        try:
            with open("passwords.json","r") as f:
                data1 = json.load(f)
                data1.update(new_data)
                with open("passwords.json", "w") as F:
                    json.dump(data1, F, indent=4)
        except JSONDecodeError:
            with open("passwords.json","w") as f:
                json.dump(new_data, f, indent=4)



        pass_entry.delete(0,'end')
        web_entry.delete(0,'end')
def search():
    flg = 0
    try:
        with open("passwords.json","r") as f:
            name1 = web_entry.get()
            data = json.load(f)
            for dat in data:
                if dat == name1:
                    passw = data[dat]["password"]
                    messagebox.showinfo(title="Password",message=f"Your password is: {passw}")
                    flg =1
            if flg == 0:
                messagebox.showinfo(title="Password", message="Sorry Password Not Found")
    except JSONDecodeError:
        messagebox.showinfo(title="Password", message="Sorry Password Not Found")
    except FileNotFoundError:
        messagebox.showinfo(title="Password", message="Sorry NO Data File Found")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20,bg=PINK)
temp = Label(window,text="",bg = PINK)
temp.grid(row =0,column =0 )
canvas = Canvas(window,width =200 ,height =200, bg=PINK,highlightthickness=0 )
canvas.grid(row = 0,column =1)
img = PhotoImage(file = "logo.png")
canvas.create_image(110, 110, image=img)
website= Label(window, text="Website:",font=(FONT2,11,"bold"),bg=PINK,fg=RED)
website.grid(row=1,column=0)
web_search = Button(text="Search",font=(FONT2,11,"bold"),bg=PINK,fg=RED,command = search)
web_search.grid(row=1, column=2)
web_entry = Entry(window,width=43)
web_entry.grid(row=1,column=1,sticky='w' )
web_entry.focus()
user = Label(window, text="Emaill/Username:",font=(FONT2,11,"bold"),bg=PINK,fg=RED)
user.grid(row=2, column=0)
user_entry = Entry(window,width=43)
user_entry.grid(row=2,column=1 ,columnspan=2,sticky='w')
user_entry.insert(0,"danmanibinu@gmail.com")
passw = Label(window, text="Password:",font=(FONT2,11,"bold"),bg=PINK,fg=RED)
passw.grid(row=3, column=0)
pass_entry = Entry(window,width=23)
pass_entry.grid(row=3,column=1,sticky='w' )
gen_pass = Button(window, text="Generate Password",bg=PINK,font=(FONT2,8,"bold"),fg=RED,width=15,command = generate)
gen_pass.grid(row=3, column=1,sticky='e',columnspan=2)
add = Button(window,text="Add",font=(FONT2,11,"bold"),bg=PINK,fg=RED,width=28,command = save)
add.grid(row=4,column=1,columnspan=2,sticky='w')

window.mainloop()