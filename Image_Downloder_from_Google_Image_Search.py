__author__ = 'Nakum Urvish'
__Version__ = '0.1'
"""
Script to download bunch of image which appers in google seach results
and make a dataset of those images for machine-learning and deep-learning.

And it will store the image into after making a folder name "downloads" in current working directory.

Note:  Sample Code Taken From "https://github.com/hardikvasa/google-images-download"
"""

#importing the library
from google_images_download import google_images_download   

#class instantiation
response = google_images_download.googleimagesdownload()   

#creating list of arguments
arguments = {"keywords":"Drone","limit":20,"print_urls":True}   

#passing the arguments to the function
paths = response.download(arguments)   

#printing absolute paths of the downloaded images
print(paths)   
