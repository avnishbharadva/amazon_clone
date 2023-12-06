def count_words(file):
    with open(file,"r") as f:

        words = f.read().split()
        print(words)

        ce = 0
        for word in words:
            if word.endswith('e'):
                ce += 1

        print("Total Words Ends with 'e' :",ce)

count_words("example.txt")