__author__ = 'Nakum Urvish'
__Version__ = '0.1'

"""
Script to delete all corrupted image in current working directory.
"""

import os
import glob
from PIL import Image

files_grabbed = []

# insert types of files you want to take for resize
File_types = ("*.jpg" , "*.png" , "*.jpeg" , "*.bmp")

# Store list of image
for file in File_types:
	files_grabbed.extend(glob.glob(file))

# Remove the corrupted image from directory
for image in files_grabbed:
	try:
		i = Image.open(image)
		i.verify()
	except Exception as e:
		print("[+] Image removed : " + image)
		os.remove(image)

	
