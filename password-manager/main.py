import customtkinter
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    import string
    password = ''
    for i in range(8):
        password += random.choice(string.ascii_letters + string.digits)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    if website_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '':
        messagebox.showinfo(title='Error', message='Please fill all the fields')
    else:
        is_ok = messagebox.askyesno(title=website_entry.get(),
                                    message=f"These are the details entered:\nEmail:{username_entry.get()} \n Password:{password_entry.get()}\n Do you want to save this password?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(
                    website_entry.get() + ' || ' + username_entry.get() + ' || ' + password_entry.get() + '\n')
                clear()


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode('default')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.config(padx=20, pady=20, bg='black')
app.title('Password Manager')
canvas = Canvas(width=300, height=300, bg='black', border=0, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=photo)
canvas.grid(row=0, column=1)

website = customtkinter.CTkLabel(app, text='Website:', fg='white')
website.grid(row=1, column=0)
username = customtkinter.CTkLabel(app, text='Website/Username:', fg='white')
username.grid(row=2, column=0)
password = customtkinter.CTkLabel(app, text='Password:', fg='white')
password.grid(row=3, column=0)

website_entry = customtkinter.CTkEntry(master=app, width=350, fg_color='white', border_width=0, text_color='black')
website_entry.grid(row=1, column=1, columnspan=2, pady=10)
website_entry.focus()
username_entry = customtkinter.CTkEntry(master=app, width=350, fg_color='white', border_width=0, text_color='black')
username_entry.grid(row=2, column=1, columnspan=2, pady=10)
username_entry.insert(0, 'Enter Your Email Here' )
password_entry = customtkinter.CTkEntry(master=app, width=210, fg_color='white', border_width=0, text_color='black')
password_entry.grid(row=3, column=1)

generate_button = customtkinter.CTkButton(app, text='Generate Password', border_width=0, command=password_generator)
generate_button.grid(row=3, column=2, pady=10)
add_button = customtkinter.CTkButton(app, text='Add', width=350, border_width=0, command=add)
add_button.grid(row=4, column=1, columnspan=2)

app.mainloop()
