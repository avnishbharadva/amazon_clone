import pickle

def createFile():
    with open("book.dat","ab") as f:
        book = {}
        book['BookNo'] = int(input("Enter Book No : "))
        book['Book_Name'] = input("Enter Book Name : ")
        book['Author'] = input("Enter Author : ")
        book['price'] = float(input("Enter Price : "))
        
        pickle.dump(book,f)

def countRec(author):
    with open("book.dat","rb") as f:

        ca = 0        
        try:
            while True:
                book = pickle.load(f)
                if book['Author'] == author:
                    ca += 1
        except:
            pass

        print(f"No of books by author {author} : {ca}")

createFile()

author = input("Enter Author Name to Search : ")
countRec(author)