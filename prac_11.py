# lst = [1,"avnish",56.78,"end"]

with open("writelstdemo.txt","w") as f:

    f.writelines(["python","avnish","end"])
    # for i in lst:
    #     f.write(str(i))
    print("List write sucessfully")