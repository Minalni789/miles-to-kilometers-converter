from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(row=0, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=1)

result_label = Label(text="0")
result_label.grid(row=1, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=3)


def button_click():
    result = float(entry.get()) * 1.609
    final_result = round(result, 2)
    result_label.config(text=final_result)


button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=2)


window.mainloop()
