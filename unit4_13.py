with open("example.txt","r") as f:
    con = f.read()

    words = con.split()
    print(words) 

    for w in words:
        if '@' in w and '.' in w:
            print(w)