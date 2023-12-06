with open('example.txt','r') as f:
    con = f.readlines()

    no = int(input("Enter how many lines want to read from last : "))

    print(con[-no:]) 