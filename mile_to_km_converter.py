from tkinter import *


def button_clicked():
    new_text = round(float(input.get())*1.60934,2)
    answer.config(text=new_text)


window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# "is equal to" label
my_label = Label(text="is equal to", font=("Arial", 10))
my_label.grid(column=0, row=1)
my_label.config(padx=5, pady=5)

# Answer label
answer = Label(text=0, font=("Arial", 10))
answer.grid(column=1, row=1)
answer.config(padx=5, pady=5)

# Miles label
miles = Label(text="Miles", font=("Arial", 10))
miles.grid(column=2, row=0)
miles.config(padx=5, pady=5)

# km label
km = Label(text="km", font=("Arial", 10))
km.grid(column=2, row=1)
km.config(padx=5, pady=5)

# Calculate Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# User-input
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)


window.mainloop()