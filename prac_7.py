f = open("example.txt","r")

if f.closed:
    print("File is closed")
else:
    print("file is open")

f.close()

if f.closed:
    print("File is closed")
else:
    print("file is open")