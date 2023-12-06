no = int(input("Enter no of lines want to read : "))

with open("example.txt","r") as f:
    for _ in range(no):
        print(f.readline(),end="")