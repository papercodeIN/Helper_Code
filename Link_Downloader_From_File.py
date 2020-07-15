import os

# You can use this one too.
#import wget

count = 0

# Path to URL File.
# text file should only contain URL which can be downloadable.
file_path = "/folder/file.txt"


# Count number of URL available in file
with open(file_path, 'r') as file:
    for URL in file:
        count += 1

count = int(count)
print("INFO     [+]File Path:" , file_path)

# Number of URL available in file
print("INFO     [+]Total Number Of URL in File are:" , int(count))

# Download filr from each URl
with open(file_path, 'r') as file:
	for i in range (1,count):
	    for url in file:
	    	print("INFO     [+]Downloading...        ")
	    	os.system('wget -c -q --show-progress %s'%url)
#	    	wget.download(url, bar_thermometer(i, int(count)))

print("INFO     [+]Download Complete.")
