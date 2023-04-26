from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


def openfilename():
    # open file dialog box to select image
    # The dialogue box has title "Open"
    filename = filedialog.askopenfilename(title="Select a file", filetype=(('jpeg files', '*.jpg'), ("all files", "*.*")))
    if filename:
        image = Image.open(filename).convert("RGBA")
        watermark_image = Image.open("images/watermark.jpg").convert("RGBA")

        # Size watermark relative to the size of base image
        watermark_mask = watermark_image.convert("RGBA")

        # Set position to lower right corner
        position = (image.size[0] - watermark_image.size[0],
                    image.size[1] - watermark_image.size[1])

        transparent = Image.new("RGBA", image.size, (0, 0, 0, 0))
        transparent.paste(image, (0, 0))
        transparent.paste(watermark_mask, position, mask=watermark_mask)
        transparent.show()

        # Save Watermarked Photo
        finished_img = transparent.convert("RGB")
        finished_img_name = filename[:-4] + "WM.jpg"
        finished_img.save(finished_img_name)

        success_text.set(f"Success! File successfully saved.")


def quit_window():
    window.destroy()


window = Tk()
window.title("Image WaterMarking App")

canvas = Canvas(width=600, height=500, background='#FFB4B4')
canvas.grid(rowspan=4, columnspan=3)

# LOGO
logo = Image.open("images/logo.png")
logo = logo.resize((200, 200))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instruction Label
instruction_label = Label(text="Select photo to watermark.", font=('Arial', 14, 'bold'), bg="#ffb4b4")
instruction_label.grid(column=1, row=1)

# Browse Dialog Button
browse_text = StringVar()
browse_button = Button(command=openfilename, textvariable=browse_text, font='Arial', bg="#20bebe", fg='white',
                       height=2, width=15, highlightthickness=0)
browse_text.set("Browse")
browse_button.grid(column=0, row=2)

# Success Message
success_text = StringVar()
success_text.set(" ")
success_label = Label(textvariable=success_text, bg="#ffb4b4", font=("Arial", 12, "bold"))
success_label.grid(column=1, row=3)

# Cancel Button
cancel_button = Button(command=quit_window, text="Quit", font='Arial', bg="#20bebe", fg="white", height=2,
                       width=15, highlightthickness=0)
cancel_button.grid(column=2, row=2)


window.mainloop()
