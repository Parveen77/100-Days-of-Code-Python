from tkinter import *

window = Tk()
window.title("Miles Converter")
window.minsize(width=300, height=100)
window.config(pady=10)


label1 = Label(text="KM to miles")
label1.grid(column=0, row=1)
label1.config(padx=12)

input = Entry(width=12)
input.grid(column=1, row=0)

label2 = Label(text="KM")
label2.grid(column=2, row=0)


output = Entry(width=12)
output.grid(column=1, row=2)

label3 = Label(text="Miles")
label3.grid(column=2, row=2)


def action():
    km = int(input.get())
    miles = "{:.2f}".format(km * 1.6)
    output.insert(END, string=str(miles))

button = Button(text="Convert", command=action)
button.grid(column=3, row=1)


window.mainloop()


