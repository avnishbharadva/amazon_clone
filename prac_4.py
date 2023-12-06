with open("example.txt","r") as f:
    con = f.read()

    lst = []
    for c in con:
        if not c.isalpha():
            lst.append(con.split(c))

    print(lst)