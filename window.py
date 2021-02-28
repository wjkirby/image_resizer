""" Website image resizer program"""

from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import Label
from tkinter import Listbox
from tkinter import Entry
from tkinter import Button
from tkinter import END
import os
import os.path
import shutil
from PIL import Image

def browseFolders():
    global folder_path
    global folder_selected
    folder_selected = filedialog.askdirectory()+"/"
    folder_path.set(folder_selected)


def browseFile1():
    global file1_path
    global file1_selected
    file1_selected = filedialog.askopenfilename(initialdir=folder_selected)
    file1_selected = os.path.split(file1_selected)[1]
    file1_path.set(file1_selected)


def browseFile2():
    global file2_path
    global file2_selected
    file2_selected = filedialog.askopenfilename(initialdir=folder_selected)
    file2_selected = os.path.split(file2_selected)[1]
    print(file1_selected, file2_selected)
    if file2_selected < file1_selected:
        file2_path.set("Error - file sequense less than file 1")
    else:
        file2_path.set(file2_selected)


def clearEntries():
    global folder_path
    global file1_path
    global file2_path
    global file_name
    folder_path.set("")
    file1_path.set("")
    file2_path.set("")
    file_name.set("")
    file1_selected = ""
    file2_selected = ""
    file_name = ""
    display_box.delete(0, END)


def processImages():
    global file_name
    file_name = file_name_display.get()
    print(file_name)
    display_box.insert(END, "Processing images...")
    return


window = Tk()
#window.geometry("586x320")
window.title("Website Image Processor")

folder_path = StringVar()
file1_path = StringVar()
file2_path = StringVar()
file_name = StringVar()
lbl_bg_color = "gray21"
lbl_fg_color = "white"
logo = './ricer-logo.png'
logoIm = Image.open(logo)
logoWidth, logoHeight = logoIm.size
basewidth = 1024

folder_label = Label(window, text="Base Folder: ", bg=lbl_bg_color, fg=lbl_fg_color)
folder_label.grid(row=0, column=0, ipadx=20)

first_image_label = Label(window, text="Starting Image: ", bg=lbl_bg_color, fg=lbl_fg_color)
first_image_label.grid(row=1, column=0, ipadx=12)

last_image_label = Label(window, text="Ending Image: ", bg=lbl_bg_color, fg=lbl_fg_color)
last_image_label.grid(row=2, column=0, ipadx=15)

file_name_label = Label(window, text="Enter File Name: ", bg=lbl_bg_color, fg=lbl_fg_color)
file_name_label.grid(row=3, column=0, ipadx=6)

folder_display = Entry(window, textvariable=folder_path, width=40)
folder_display.grid(row=0, column=1, pady=5)

file1_display = Entry(window, textvariable=file1_path, width=40)
file1_display.grid(row=1, column=1,pady=5)

file2_display = Entry(window, textvariable=file2_path, width=40)
file2_display.grid(row=2, column=1,pady=5)

file_name_display = Entry(window, textvariable=file_name, width=40)
file_name_display.grid(row=3, column=1,pady=5)

display_box = Listbox(window, width=57)
display_box.grid(row=4, column=0, rowspan=4, columnspan=3, padx=5, pady=5)

folder_button = Button(window, text="Browse Folder", width=12, command=browseFolders)
folder_button.grid(row=0, column=4, padx=5)

first_image_button = Button(window, text="First Image", width=12, command=browseFile1)
first_image_button.grid(row=1, column=4,padx=5)

last_image_button = Button(window, text="Last Image", width=12, command=browseFile2)
last_image_button.grid(row=2, column=4, padx=5)

process_button = Button(window, text="Process Images", width=12, command=processImages)
process_button.grid(row=4, column=4, padx=5)

clear_button = Button(window, text="Clear Entries", width=12, command=clearEntries)
clear_button.grid(row=5, column=4, padx=5)

exit_button = Button(window, text="Exit", width=12, command=window.destroy)
exit_button.grid(row=6, column=4, padx=5)


window.mainloop()
