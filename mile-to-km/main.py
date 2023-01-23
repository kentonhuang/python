from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

equal_to = Label(text="is equal to")
equal_to.grid(row=1,column=0)

miles_entry = Entry(width=10)
miles_entry.insert(0, "0")
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_value = Label(text="0")
km_value.grid(row=1, column=1)

def calc():
    value = int(miles_entry.get())
    km = round(value * 1.609344)
    km_value.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(row=2, column=1)

window.mainloop()