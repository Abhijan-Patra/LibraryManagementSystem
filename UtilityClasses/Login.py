from LibraryManagementSystem import Main
def SignUP():
    print("1-Admin")
    print("2-Student")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            myAdmin=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Admins.txt","a+")
            facultyName=input("Enter your Faculty Name(UserName):")
            facultyID=input("Enter your Faculty ID:")
            facultyDept = input("Enter your Faculty Dept:")
            myAdmin.write(f"{facultyID}|{facultyName}|{facultyDept}\n")
            print("Successfully SignedUp, Now you can proceed to SignIn (name=username and ID as password")
            myAdmin.close()
        case 2:
            myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/StudentsLogin.txt","a+")
            StudentName=input("Enter your Student Name:")
            StudentID=input("Enter your Student ID:")
            myStudent.write(f"{StudentID}|{StudentName}\n")
            myStudent.close()

def SignIN():
    print("1-Admin")
    print("2-Student")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            b=True
            while b:
                myAdmin = open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Admins.txt","r+")
                userName=input("Enter your Username:")
                password = input("Enter your Password:")
                myAdmin.seek(0)
                allAdmins=myAdmin.readlines()

                for admin in allAdmins:
                    if admin.split("|")[1]==userName:
                        if admin.split("|")[0]==password:
                            Main.permission=True
                            print("Successfully SignedIn!!")
                            b=False
                            break
                        else:
                            print("Wrong Password Login Again(n to exit)")
                            if input()=='n':
                                b=False
                            break
                else:
                    print("Couldn't Login(n to exit)")
                    if input()=='n':b=False
            myAdmin.close()
        case 2:
            b=True
            while b:
                myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/StudentsLogin.txt","r")
                username=input("Enter your User Name:")
                password=input("Enter your Password:")
                myStudent.seek(0)
                allStudents = myStudent.readlines()
                for student in allStudents:
                    if student.strip("\n").split("|")[1]==username:
                        if student.split("|")[0]==password:
                            Main.permission=True
                            print("Successfully SignedIn!!")
                            b=False
                            break
                        else:
                            print("Wrong Password Login Again(n to exit)")
                            if input()=='n':b=False
                            break
                else:
                    print("Couldn't Login(n to exit)")
                    if input()=='n':b=False
            myStudent.close()
SignIN()
