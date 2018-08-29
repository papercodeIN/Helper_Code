__author__ = 'Nakum Urvish'
__Version__ = '0.1'
"""
Script to resize all image in current working directory.
And save each image as new file in "Resized_Image" folder.
"""

import os
import glob
import cv2

images = glob.glob('*.jpg')
print(images)

Folder = "Resized_Image"
if not os.path.exists(Folder):
	os.mkdir(Folder)

for image in images:
	pic = cv2.imread(image, 1)
	pic = cv2.resize(pic, (277,277))
	cv2.imwrite(Folder + '/' + image, pic)
