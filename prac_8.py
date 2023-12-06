with open("example.txt","r") as f:
    con = f.read()

    with open("newdemo.txt","w") as fw:
        fw.write(con)

    print("data copied successfully")