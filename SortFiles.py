import os
import shutil

from tkinter import filedialog

from tkinter import *


root = Tk()

root.withdraw()

folder_selected = filedialog.askdirectory()

os.chdir(folder_selected)

folder = ["Vidéo", "Gif", "Image", "Icon"]
for f in folder:
    if not os.path.exists(f):
        os.makedirs(f)

for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)
    match file_extension:
        case (".png" | ".jpg"):
            shutil.move(file, "Image")

        case ".gif":
            shutil.move(file, "Gif")

        case ".mp4":
            shutil.move(file, "Vidéo")

        case ".ico":
            shutil.move(file, "Icon")
