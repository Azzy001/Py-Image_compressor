from tkinter import *
import PIL
from PIL import Image
from tkinter.filedialog import *

window = Tk()


def load_img():
    global img
    img_path = askopenfilename()
    img = PIL.Image.open(img_path)
    img_height, img_width = img.size
    img = img.resize((img_height, img_width), PIL.Image.ANTIALIAS)


def save_img():
    save_path = asksaveasfilename()
    img.save(save_path + "_compressed.JPG")


# title
title = Label(window, text="Image Compressor")
title.place(x=170, y=35)


# buttons
select_Btn = Button(window, text="Select Image", width=15, height=2, command=load_img)
select_Btn.place(x=100, y=80)

save_Btn = Button(window, text="Save Image", width=15, height=2, command=save_img)
save_Btn.place(x=240, y=80)


# Window configurations
window.title("Arsalan's Image Compressor")
window.geometry("450x300")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()