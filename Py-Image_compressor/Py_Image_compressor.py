from tkinter import *
import PIL
from PIL import Image
from tkinter.filedialog import *

window = Tk()

def load_img():
    pass


def save_img():
    pass


title = Label(window, text="Image Compressor")
title.place(x=170, y=30)

select_Btn = Button(window, text="Select Image", width=15, height=2)
select_Btn.place(x=100, y=80)

save_Btn = Button(window, text="Save Image", width=15, height=2)
save_Btn.place(x=240, y=80)


# Window configurations
window.title("Arsalan's Image Compressor")
window.geometry("450x300")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()