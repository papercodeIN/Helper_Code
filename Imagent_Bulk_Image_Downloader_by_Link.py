import urllib
import cv2
import numpy as np
import os


Folder_Name = "Data_Set"

def download_image():

    # Put your imagenet dataset link here which contain bunch of url or images
    images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03245889'   
   
    # Split each line and get each image url for download
    image_urls = urllib.urlopen(images_link).read().decode()

    # Set counter for image name
    pic_num = 1
    
    # Create folder to save those images
    if not os.path.exists(Folder_Name):
        os.makedirs(Folder_Name)
        print("[+] Data_Set Folder Created.")
        
    # Main loop to download each image contain in url
    
    for i in image_urls.split('\n'):
        try:
            urllib.urlretrieve(i, Folder_Name +'/'+ str(pic_num)+".jpg")
            print("[+] Image Download : " + str(pic_num)+".jpg" )
            pic_num += 1
            
        except Exception as e:
            print(str(e))  
	            
    print("[+] Total Images Download : " + str(pic_num))

# initiate the function
download_image()
