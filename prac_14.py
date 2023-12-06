import pickle

def add_rec():
    with open("student.dat","ab") as f:
        student = {}
        student['add_no'] = int(input("Enter Addmission Number : "))
        student['Name'] = input("Enter Name : ")
        student['Percentage'] = float(input("Enter Percentage : "))

        pickle.dump(student,f)
        print("Data Inserted...")

def count_rec():
    with open("student.dat","rb") as f:
        print("Details of Student whose percentage is above 75")
        cs = 0
        try:
            while True:
                student = pickle.load(f)
                if student['Percentage'] > 75:
                    print(student)
                    cs += 1
        except EOFError:
            pass

        print("Total No of Students whose percentage is above 75 :",cs)

add_rec()
count_rec()