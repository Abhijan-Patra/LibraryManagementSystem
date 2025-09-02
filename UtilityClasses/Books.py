class Books:

    def addBook(self,id:int,title:str,author:str):

        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt","a+")
        myBook.seek(0)
        allBooks=myBook.readlines()
        absent=False
        if len(allBooks)>0:
            for i in allBooks:
                if i!="\n":
                    print(i,end="")
                    if title.lower()!=i.split("|")[1].lower():
                        pass
                    else:
                        absent=False
                        break
            else:
                absent=True
            if absent:
                myBook.write(f"{id}|{title}|{author}\n")
                print("Successfully added the book!!")
        else:
            myBook.write(f"{id}|{title}|{author}\n")
            print("Successfully added the book!!")

        myBook.close()

    def removeBook(self,idd:int)->str:
        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'r')
        allData=myBook.readlines()
        myBook.close()
        book=""
        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'w')
        for i in allData:
            if int(i.strip('\n').split("|")[0])!=idd:
                myBook.write(i)
            else:
                book=i
        myBook.close()
        return book


    def displayBook(self,):
        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'r')
        allBooks=myBook.readlines()
        for book in allBooks:
            print(book,end="")
    def issueBook(self,id:int):
        b = Books()
        studentName=input("Enter the Name of the Student: ")
        studentRegNo=input("Enter the RegNo of the Student: ")
        myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Student.txt",'a+')
        myStudent.seek(0)
        allStudents=myStudent.readlines()
        bookIssued=True
        book=""
        print(allStudents)
        if len(allStudents)>0:
            for student in allStudents:
                if student=='\n':
                    continue
                if studentRegNo == student.split("|")[1]:
                    if int(student.strip("\n").split('|')[2])!=id:
                       pass
                    else:
                       bookIssued=True
                       break
                else:
                    pass
            else:
                bookIssued=False
            if bookIssued==False:
                book=b.removeBook(id)
                myStudent.write(f"{studentName}|{studentRegNo}|{book}")
                print(f"{book} 1 has been issued succesfully by {studentName}")
        else:
            book=b.removeBook(id)
            myStudent.write(f"{studentName}|{studentRegNo}|{book}")
            print(f"{book.strip("\n")}  2 has been issued succesfully by {studentName}")
        myStudent.close()
    def showStudents(self,):
        myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Student.txt","r")
        allStudents=myStudent.readlines()
        for student in allStudents:
            print(student.strip("\n"))
        myStudent.close()
    def returnBook(self,id:int):
        studentRegNo=input("Enter the Student Reg No.: ")
        myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Student.txt",'r')
        allStudents=myStudent.readlines()
        myStudent.close()
        myStudent=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Student.txt",'w')
        bookReturned=False
        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'a+')
        print(allStudents)
        book=""
        for student in allStudents:
            if student=="\n":continue
            if studentRegNo==student.strip("\n").split("|")[1]:
                print(student.strip("\n").split("|")[1])
                if id == int(student.strip("\n").split("|")[2]):
                    bookReturned=True
                    for i in student.split("|")[2:]:
                        book=book+i+"|"
                    myBook.write(book.strip("|"))
                else:
                    bookReturned=False
                    myStudent.write(student)
            else:
                bookReturned=False
                myStudent.write(student)
        myStudent.close()
        myBook.close()

    def searchBook(self,title:str)->str:
        myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'r')
        allBooks=myBook.readlines()
        myBook.close()
        found=False
        for book in allBooks:
            if book.strip("\n").split("|")[1].lower()==title.lower():
                found=True
                return book.strip("\n").split("|")[0]
        if found==False:
            return "Not Found"