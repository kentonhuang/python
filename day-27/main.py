from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    text = input.get()
    my_label["text"] = text

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="New Button")
button_2.grid(column=2,row=0)
#Entry

input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
