with open("example.txt") as f:
    con = f.read()

    lc = []
    for c in con:
        lc.append(c)

    # print(lc)

    uc = list(set(lc))
    # print(uc)

    luc = []
    lud = []
    for c in uc:
        if c.isalpha():
            luc.append(c)
        if c.isdigit():
            lud.append(c)

    # print(luc)
    # print('a'.isdigit())
    # print(lud)

    f = {}
    for c in luc:
        f[c] = con.count(c)

    fd = {}
    for d in lud:
        fd[d] = con.count(d)
    print("Character Frequency :",f)
    print("Digit Frequency :",fd)