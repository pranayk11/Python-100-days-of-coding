from tkinter import *
import random
import csv

BACKGROUND = "#FFB4B4"
words_data = []
showed_words = []
user_words = []
display = ""
wpm_count = 0
cpm_count = 0


def countdown(count):
    """Timer function"""
    if count > 0:
        window.after_id = window.after(1000, countdown, count-1)
    else:
        window.after_id = None
    if count < 10:
        count = f"0{count}"
    if count == "00":
        compare()
        restart_button['state'] = 'normal'
        window.bind("<Return>", start)
    timer_text.config(text=f"{count}")


def start_timer():
    """Starts the timer"""
    if window.after_id is not None:
        window.after_cancel(window.after_id)
    countdown(60)


def user_type(event):
    """Adds user typed words to the list
    If user types all the words on the screen, random_words gets called"""
    user_words.append(entry_box.get().title().strip())
    entry_box.delete(0, 'end')
    if len(user_words) % 8 == 0:
        random_words()


# Import words list
with open('words.csv', encoding='utf-8-sig') as data_file:
    data = csv.reader(data_file)
    for row in data:
        words_data.append("".join(row))


def random_words():
    """Generates Random words"""
    global display
    display = ""
    for i in range(8):
        display_word = random.choice(words_data)
        showed_words.append(display_word)
        display += (display_word + ' ')
    canvas.itemconfig(word_show, text=display)


def restart():
    """Resets the values and restart the timer """
    global showed_words, user_words, wpm_count, cpm_count
    showed_words = []
    user_words = []
    wpm_count = 0
    cpm_count = 0
    wpm_value.config(text=wpm_count)
    cpm_value.config(text=cpm_count)
    entry_box.config(state='normal')
    start_timer()
    random_words()


def start(event):
    """Starts the Typing test"""
    global showed_words, user_words, wpm_count, cpm_count
    showed_words = []
    user_words = []
    cpm_count = 0
    wpm_count = 0
    wpm_value.config(text=wpm_count)
    cpm_value.config(text=cpm_count)
    entry_box.config(state='normal')
    start_timer()
    random_words()
    window.unbind('<Return>')


def compare():
    """Counts CPM and WPM"""
    global wpm_count, cpm_count
    entry_box.config(state='disabled')
    for i in user_words:
        if i in showed_words:
            wpm_count += 1
            cpm_count += 1
    wpm_value.config(text=wpm_count)
    cpm_value.config(text=cpm_count)
    print(f"user_type: {user_words}")
    print(f"display_words: {showed_words}")


window = Tk()
window.title("Typing Speed Test")
window.config(bg=BACKGROUND, padx=50, pady=20)
window.after_id = None

canvas = Canvas(window, width=400, height=265, bg=BACKGROUND, highlightthickness=0)
canvas.grid(columnspan=6, column=1, row=2)
word_show = canvas.create_text(200, 132, text="Press space bar after each word\n\nPress Enter to start",
                               font=("Courier", 14, 'bold'), width=250, justify='center')

cpm_label = Label(text='Corrected CPM:', font=("Arial", 12), bg=BACKGROUND)
cpm_label.grid(row=1, column=1)
cpm_value = Label(text="?", font=("Arial", 12), bg=BACKGROUND)
cpm_value.grid(row=1, column=2)

wpm_label = Label(text="WPM:", font=("Arial", 12), bg=BACKGROUND)
wpm_label.grid(row=1, column=3)
wpm_value = Label(text="?", font=("Arial", 12), bg=BACKGROUND)
wpm_value.grid(row=1, column=4)

timer_label = Label(text='Time left:', font=("Arial", 12), bg=BACKGROUND)
timer_label.grid(row=1, column=5)
timer_text = Label(text='60', font=("Arial", 12), bg=BACKGROUND)
timer_text.grid(row=1, column=6)

entry_box = Entry(window, bg="#FDF7C3", bd=0, font=("Arial", 12), justify='center', width=30)
entry_box.focus()
entry_box.grid(row=3, column=1, columnspan=6, pady=20)
window.bind('<space>', user_type)
window.bind('<Return>', start)

restart_button = Button(text="Restart", highlightthickness=0, bg="#B2A4FF", font=("Arial", 12), command=restart)
restart_button.grid(row=4, column=3)

window.mainloop()
