from tkinter import *
from tkinter import messagebox  #it is another module of code that tkinter did not imported
from random import choice, randint, shuffle
import pyperclip #it copy to clipboard directly by pyperclip.copy(value) eg: line 39


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols +password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    #       OR

    #learn join() #it convert all of the list, dict in a single string
    password = "".join(password_list)

    #insert text in the Entry field
    pass_txt.insert(0,password)


    pyperclip.copy(password)  #it copy to clipboard directly

# ---------------------------- SAVE PASSWORD ------------------------------- #

def dataInserted():
    web_info = web_txt.get()
    email_info = email_txt.get()
    pass_info = pass_txt.get()

    if len(web_info) == 0 or len(email_info) == 0 or len(pass_info) == 0:
        messagebox.showerror(title="Text Empty Error", message="Bro Write something in that empty field")
    else:
        # other methods like showinfo, askyesno
        is_ok = messagebox.askokcancel(title="Alert",
                                       message=f"These are the details entered: \n Web: {web_info} \nEmail: {email_info} \nPassword: {pass_info}")

        if is_ok:
            with open("file.txt", mode='a') as data_file:
                data_file.write(f"\n{web_info} | {email_info} | {pass_info}")
                # This down will delete the data when we save them
                web_txt.delete(0, END)
                email_txt.delete(0, END)
                pass_txt.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)


#Labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

#Entry
web_txt = Entry(width=35)
web_txt.grid(row=1, column=1, columnspan=2)
web_txt.focus()

email_txt = Entry(width=35)
email_txt.grid(row=2, column=1, columnspan=2)
email_txt.insert(0, "priyanshrana@gmail.com")

pass_txt = Entry(width=21)
pass_txt.grid(row=3, column=1)

#Button
generate_btn = Button(text="Generate Pass", width=10, command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=33, command=dataInserted)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()