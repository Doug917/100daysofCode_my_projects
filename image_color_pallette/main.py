from pallette_generator import pallette_generator
from tkinter import *
from tkinter import messagebox
import cv2




def display_color_pallette():
    filename = path_entry.get()

    # Get image file.
    img = cv2.imread(filename)
    top_colors = pallette_generator(img)

    canvas.itemconfig(rectangle1, fill='#'+top_colors[0], outline='#'+top_colors[0])

    canvas.itemconfig(rectangle2, fill='#'+top_colors[1], outline='#'+top_colors[1])

    canvas.itemconfig(rectangle3, fill='#'+top_colors[2], outline='#'+top_colors[2])

    canvas.itemconfig(rectangle4, fill='#'+top_colors[3], outline='#'+top_colors[3])

    canvas.itemconfig(rectangle5, fill='#'+top_colors[4], outline='#'+top_colors[4])

    
# ---------------------------- START THE APP ------------------------------- #
window = Tk()
window.title("Color Pallette Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=400, highlightthickness=0)
canvas.grid(row=0, column=1)

# ---------------------------- UI SETUP ------------------------------- #
# Label
website_label = Label(text="Image File Path: ", font=("Calibri", 12, "normal"))
website_label.grid(row=1, column=0)

# Image file path entry
path_entry = Entry(width=100)
path_entry.focus()
path_entry.grid(row=1, column=1)

# rectangles
rectangle1 = canvas.create_rectangle(-50, 100, 50, 150)

rectangle2 = canvas.create_rectangle(-50, 150, 50, 200)

rectangle3 = canvas.create_rectangle(-50, 200, 50, 250)

rectangle4 = canvas.create_rectangle(-50, 250, 50, 300)

rectangle5 = canvas.create_rectangle(-50, 300, 50, 350)


# Button to generate color pallette
pw_button = Button(text="Generate Color Pallette", command=display_color_pallette)
pw_button.grid(row=1,column=2)

window.mainloop()

