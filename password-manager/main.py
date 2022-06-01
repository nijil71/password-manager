import customtkinter
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, END)
    import random
    import string
    password_random = ''
    for i in range(8):
        password_random += random.choice(string.ascii_letters + string.digits)
    password_entry.insert(0, password_random)
    pyperclip.copy(password_random)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == '' or username == '' or password == '':
        messagebox.showinfo(title='Error', message='Please fill all the fields')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            clear()


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='NO DATA FOUND')
    else:
        if website in data:
            password = data[website]['password']
            username= data[website]['username']
            messagebox.showinfo(title='Details',message=f'Email: {username}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message='Please add a password')





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

website_entry = customtkinter.CTkEntry(master=app, width=210, fg_color='white', border_width=0, text_color='black')
website_entry.grid(row=1, column=1, pady=10)
website_entry.focus()
username_entry = customtkinter.CTkEntry(master=app, width=350, fg_color='white', border_width=0, text_color='black')
username_entry.grid(row=2, column=1, columnspan=2, pady=10)
username_entry.insert(0, 'Enter Your Email Here')
password_entry = customtkinter.CTkEntry(master=app, width=210, fg_color='white', border_width=0, text_color='black')
password_entry.grid(row=3, column=1)

generate_button = customtkinter.CTkButton(app, text='Generate Password', border_width=0, command=password_generator)
generate_button.grid(row=3, column=2, pady=10)
add_button = customtkinter.CTkButton(app, text='Add', width=350, border_width=0, command=add)
add_button.grid(row=4, column=1, columnspan=2)
search_button = customtkinter.CTkButton(app, text='Search', border_width=0, command=find_password)
search_button.grid(row=1, column=2)


app.mainloop()
