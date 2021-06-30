from PIL import Image, ImageGrab, ImageTk
import tkinter as tk

im2 = ImageGrab.grab(bbox=None)

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

image = im2.resize((screen_width, screen_height), Image.ANTIALIAS)

screenGeometry = str(screen_width) + "x" + str(screen_height)

print(screenGeometry)

# window = tk.Tk()
window.title('UselessScreensaver')
window.geometry(screenGeometry)
window.config(bg='yellow')

img = ImageTk.PhotoImage(image)

label = tk.Label(
    window,
    image=img
)

label.place(x=0, y=0)


window.mainloop()