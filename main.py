# The script that deletes all files only in specified folder given by the user (will not delete the folder only it's content)

# imports
import os
from os import listdir
from os.path import isfile, join

# file Path that takes user input
while True:
    mypath = input(f"""\u001b[1mPlease note: this action will delete ALL files inside specified folder!\u001b[0m\n
    Specify your files folder:""")
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_num = 0

    if len(files) == 0:
        print(
            f"There is {file_num} files left in the folder!\n***If you want to exit the program press CTRL + C***")
    else:
        try:
            for file in files:
                file_num += 1
                os.remove(mypath + file)
            print(f"Successfully deleted {file_num} file(s)!")
            print(
                f"There is no files left in the folder {mypath}\n***If you want to exit the program press CTRL + C***\n")
        except NameError:
            print("No such file exists, probably already deleted!")
        except PermissionError:
            print(
                f"""File {file} exists but used by another program, please
                    close all other programs that migh be using it!""")
        except FileNotFoundError:
            # Here we are asking if user forgot to include "\",
            # however as part of defensive programming we can make this check programatically
            print(
                r"File not found - perhaps you are missing \ at the end of your destination folder address?")
        except KeyboardInterrupt:
            pass
