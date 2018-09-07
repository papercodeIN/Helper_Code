__author__ = 'Nakum Urvish'
__Version__ = '0.2'
"""
Script to resize all image in current working directory.
And save each image as new file in "Resized_Image" folder.
"""

import os
import glob
import cv2

#image width and height
Size_width = int(input("Img_Width : "))
Size_Height = int(input("Img_Height : "))

# insert types of files you want to take for resize
File_types = ("*.jpg" , "*.png" , "*.jpeg" , "*.bmp")

files_grabbed = []

# Store list of image
for file in File_types:
	files_grabbed.extend(glob.glob(file))

# Create Folder to store resized image
Folder = "Resized_Image"
if not os.path.exists(Folder):
	os.mkdir(Folder)
	print("[+] Resized_Image Folder Created.")

# Main loop for resize each image
for image in files_grabbed:
	try:
		print("[+] Resizing Image : " + image)
		pic = cv2.imread(image, 1)
		pic = cv2.resize(pic, (Size_width,Size_Height))
		cv2.imwrite(Folder + '/' + image, pic)
	except Exception as e:
		print("[-] Bad Input Image. ")


print("[+] Resize Complete.")
	
