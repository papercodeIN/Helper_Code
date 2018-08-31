__author__ = 'Nakum Urvish'
__Version__ = '0.2'
"""
Script to download images for deeplearning
and also machine learning from imagenet image-url list.
"""

import urllib
import os

print("[+] Enter Folder Name For Your Dataset.")
Folder_Name = raw_input("[+] Folder_Name : ")
print("*" * 60)
print("*" * 60)
def download_image():

    # Put your imagenet dataset link here which contain bunch of url or images
    print("[+] Enter Imagenet Dataset Link To Download Image.")
    images_link = raw_input("[+] Link : ")  
    print("*" * 60) 
    print("*" * 60)
   
    # Split each line and get each image url for download
    image_urls = urllib.urlopen(images_link).read().decode()

    # Set counter for image name
    pic_num = 1
    
    # Create folder to save those images
    if not os.path.exists(Folder_Name):
        os.makedirs(Folder_Name)
	print("*" * 60)
	print("*" * 60)
        print("[+] Data_Set Folder Created.")
	print("*" * 60)
	print("*" * 60)
        
    # Main loop to download each image contain in url
    
    for i in image_urls.split('\n'):
        try:
            urllib.urlretrieve(i, Folder_Name +'/'+ str(pic_num)+".jpg")
            print("[+] Image Download : " + str(pic_num)+".jpg" )
            pic_num += 1
            
        except Exception as e:
            print(str(e))  
	            
    print("[+] Total Images Download : " + str(pic_num))
    print("*" * 60)
    print("*" * 60)
    print("[+] Download Complete.")
    print("*" * 60)
    print("*" * 60)

# initiate the function
download_image()
