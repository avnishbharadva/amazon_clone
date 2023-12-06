with open("example.txt","a+") as f:
    f.write("\nnew appended data")

    f.seek(0)

    con = f.read()
    print(con)