from tkinter import *

counter = 0


def disappear_text():
    textbox.delete(1.0, END)
    textbox.insert(END, "")


def check_disappear():
    global counter, text
    if text == textbox.get(1.0, END):
        if counter == 5:
            window.after(1000, disappear_text)
            counter -= 1
        window.after(1000, check_disappear)
        counter += 1
    else:
        window.after(1000, check_disappear)
        text = textbox.get(1.0, END)
        counter = 0


window = Tk()
window.title("Disappearing Text App")
window.minsize(500, 500)
window.config(background='black')

title = Label(window, text="Welcome to Disappearing Text Writing App.", font=('Arial', 20, 'bold'), bg='black', fg='white')
title.grid(row=0, column=1)

info_label = Label(window, text="Your text will disappear after 5 seconds of inactivity", font=('Arial', 14), bg='black',
                   fg='white')
info_label.grid(row=1, column=1)

text = ''
textbox = Text(height=15, width=100, font=('Arial', 14), highlightthickness=1, bg='#FFE6C7')
textbox.focus()
textbox.grid(row=3, column=1, padx=20, pady=20)

window.after(1000, check_disappear)
window.mainloop()
