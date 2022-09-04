import os

string_to_remove = input(str("Enter String to remove from File Name:"))

try:
        for filename in os.listdir():
            if f"{string_to_remove}" in filename:
                new_name = filename.replace(f"{string_to_remove}", "")
                os.rename(filename,new_name)
                print("! Change : " + filename + " >>> " + new_name)
            else:
                pass
finally:
    pass