import os
#import wget
#from wget import bar_thermometer
count = 0

# Path to URL File.
link_path = "/home/parrot/dw.txt"


# Count number of URL available in file
with open(link_path, 'r') as file:
    for URL in file:
        count += 1

count = int(count)
print("INFO     [+]File Path:" , link_path)

# Number of URL available in file
print("INFO     [+]Total Number Of URL in File are:" , int(count))

counter = 0
# Download file from each URl
with open(link_path, 'r') as file:
	for i in range (1,count):
	    for url in file and path in open(file_path , 'r') :
	    	counter += 1
	    	print("\nINFO     [+]Downloading...%s " %counter + "of %r" %count )
	    	os.system('wget -c -q --show-progress %s' %url)
#	    	wget.download(url)	    	
#	    	wget.download(url, bar_thermometer(i, int(count)))

print("\nINFO     [+]Download Complete.")
