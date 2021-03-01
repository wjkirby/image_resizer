import PIL
import os
import os.path
import shutil
from PIL import Image

logo = './ricer-logo.png'
logoIm = Image.open(logo)
logoWidth, logoHeight = logoIm.size
basewidth = 1024
process_images = 'y'

while process_images == 'y':
    filename = input("Enter image name: ")
    first_file = input("Enter first file name: ")
    last_file = input("Enter last file name: ")

    if not os.path.exists('./'+filename):
        os.makedirs('./'+filename)
        os.makedirs('./'+filename+'/resized')

    folder = './imgs'
    move_folder = './'+filename
    resize_folder = './'+filename+'/resized'

    n = 1

    images = os.listdir(folder)
    images.sort()

    for file in images:
        print(file)
        if file >= first_file and file <= last_file:
            file_img = folder+"/"+file
            orig_img = file_img
            print(file)
            img = Image.open(file_img)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth,hsize))
            width, height = img.size
            img.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
            file_img = resize_folder+"/"+filename+"_"+str(n)+".jpg"
            img.save(file_img)
            shutil.move(orig_img, move_folder)
            n = n+1
    process_images = input("Process another? (y or n): ")
    process_images = process_images.lower()
