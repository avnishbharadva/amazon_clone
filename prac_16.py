import pickle

def add_rec():
    with open("employee.dat","ab") as f:
        employee = {}
        employee['empcode'] = int(input("Enter Employee Code : "))
        employee['empname'] = input("Enter Name : ")
        employee['salary'] = int(input("Enter Salary : "))

        pickle.dump(employee,f)
        print("Data Inserted...")

def count_rec():
    with open("employee.dat","rb") as f:
        try:
            print("Employee details whose salary is more than 30000")
            while True:
                emp = pickle.load(f)
                if emp['salary'] > 30000:
                    print(emp)
        except EOFError:
            pass

add_rec()
count_rec()