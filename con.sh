echo [!] File should be inside this folder
echo [+] Enter file name with extension in below line

read Name

echo [+] File Name is :  $Name

echo [+] Removing Watermark !!!
sed -e "s/nfi/ /g" $Name > convert.pdf
echo [+] Watermark Removed.

echo [+] Converting PDF pages to Images !!!
pdftoppm convert.pdf $Name -png
echo [+] Images Generated.

echo [+] Removing Unnecessary Files !!!
rm convert.pdf
rm $Name

echo [+] Opertation Done.
