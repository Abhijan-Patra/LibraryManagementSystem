def addBook(id:int,title:str,author:str):
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
    else:
        print("HEHEH")
        myBook.write(f"{id}|{title}|{author}\n")  
    
    myBook.close()

def removeBook(idd:int)->str:
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


def displayBook():
    myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'r')
    allBooks=myBook.readlines()
    for book in allBooks:
        print(book,end="")
def issueBook(id:int):
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
            book=removeBook(id)
            myStudent.write(f"{studentName}|{studentRegNo}|{book}")
            print(f"{book} 1 has been issued succesfully by {studentName}")
    else:
        book=removeBook(id)
        myStudent.write(f"{studentName}|{studentRegNo}|{book}")
        print(f"{book.strip("\n")}  2 has been issued succesfully by {studentName}")
    
    
