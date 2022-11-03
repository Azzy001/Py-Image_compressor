from tkinter import *
import PIL
from PIL import Image
from tkinter.filedialog import *
import os

window = Tk()


def load_img():
    global img
    img_path = askopenfilename()
    img = PIL.Image.open(img_path)
    img_height, img_width = img.size
    img = img.resize((img_height, img_width), PIL.Image.ANTIALIAS)

    # is used to display path on GUI
    img_path = os.getcwd()
    print(img_path)

    # display image path
    path_name = Label(window, text=img_path)
    path_name.place(x=70, y=60)
    
    # green colour for user to know that an image is selected
    if len(img_path) > 1:
        path_name.config(text=img_path, fg="green")


def save_img():
    """This function is used to select a directory on your system to save the compressed image"""
    save_path = asksaveasfilename()
    img.save(save_path)


# title
title = Label(window, text="Image Compressor")
title.place(x=220, y=35)

# no path selected
no_path = Label(window, text="No path selected", fg="red")
no_path.place(x=225, y=60)

# buttons
select_Btn = Button(window, text="Select Image", width=22, height=2, command=load_img)
select_Btn.place(x=90, y=100)

save_Btn = Button(window, text="Save Image", width=22, height=2, command=save_img)
save_Btn.place(x=290, y=100)

# Window configurations
window.title("Arsalan's Image Compressor")
window.geometry("550x250")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()