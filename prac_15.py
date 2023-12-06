import os

def check_file(file):
    if os.path.exists(file):
        print("File Exists")
    else:
        print("File doesn't exists")

file = input("Enter FIle Name : ")
check_file(file)