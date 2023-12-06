with open("example.txt","r") as f:
    con = f.read()

    ln = len(con.split('\n'))
    print("No of Lines :",ln)

    uw = len(set(con.split()))
    print("No of Unique Words :",uw)