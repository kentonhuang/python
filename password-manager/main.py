from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) < 1 or len(password) < 1 or len(website) < 1:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                # file.write(f"{website} | {email} | {password}\n")
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------ #

def search():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            # file.write(f"{website} | {email} | {password}\n")
            data = json.load(data_file)
            print(data)

        stored_data = data[website]

    except FileNotFoundError:
        messagebox.showinfo(title="No passwords", message="You haven't stored any passwords yet.")
    except KeyError:
        messagebox.showinfo(title="No password found", message=f"No password found for {website}.")
    else:
        email = stored_data["email"]
        password = stored_data["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {email} \nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()