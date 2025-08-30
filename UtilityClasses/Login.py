def SignUP():
    print("1-Admin")
    print("2-Student")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            myAdmin=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Admins.txt","a+")
            facultyName=input("Enter your Faculty Name:")
            facultyDept=input("Enter your Faculty Dept:")
            facultyID=input("Enter your Faculty ID:")
            myAdmin.write(f"{facultyID}|{facultyName}|{facultyDept}\n")
            print("Successfully SignedUp, Now you can proceed to SignIn")
        case 2:
            myStudent=open("")
SignUP()