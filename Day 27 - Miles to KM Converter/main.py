from tkinter import *


def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Label
is_equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Entry
input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

# Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
