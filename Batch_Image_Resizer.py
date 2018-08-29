__author__ = 'Nakum Urvish'
__Version__ = '0.2'
"""
Script to resize all image in current working directory.
And save each image as new file in "Resized_Image" folder.
"""

import os
import glob
import cv2

File_types = ("*.jpg" , "*.png" , "*.jpeg" , "*.bmp")

# Create Folder to store resized image
Folder = "Resized_Image"
if not os.path.exists(Folder):
	os.mkdir(Folder)
	print("[+] Resized_Image Folder Created.")


files_grabbed = []

for file in File_types:
	files_grabbed.extend(glob.glob(file))
	for image in files_grabbed:
		print("[+] Resizing Image : " + image)
		pic = cv2.imread(image, 1)
		pic = cv2.resize(pic, (277,277))
		cv2.imwrite(Folder + '/' + image, pic)

print("[+] Resize Complete.")
	
