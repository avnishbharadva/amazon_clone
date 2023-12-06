with open('example.txt','r') as file:
    content = file.read()
    print(content.upper())

    nc = len(content.split("\n"))
    print("No of Lines : ",nc)

    cv = 0
    for c in content:
        if c in "aeiouAEIOU":
            cv += 1

    print("No of Vowels : ",cv) 
    
    cw = len(content.split())
    print("No of Words : ",cw)