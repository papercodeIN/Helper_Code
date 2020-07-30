# This code remove waetrmark from pdf files and convert pages of PDF files into image and remove pdf files.
# If you dont want to remove pdf file after conversion then comment 22,23,24 line from this code.

import os

# Enter File name to execute operation
print ("[!] File should be inside this folder")
filename = input("Complete File Name : ")

# Print File name
print ("[+] File is : %s" %filename)

# Remove Watermark from pdf
print ("[+] Removing Watermark !!!")
os.system('sed -e "s/nfi/ /g" %s > convert.pdf' %filename)

# Convert PDF page to Image
print ("[+] Converting PDF pages to Images !!!")
os.system("pdftoppm convert.pdf %s -png" %filename)

# Remove Unnecessary Files
print ("[+] Removing Unnecessary Files !!!")
os.system("rm convert.pdf")
os.system("rm %s" %filename)

# Operation Done
print ("[+] Conversion Done")
