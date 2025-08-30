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

def removeBook(idd:int):
    myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'r')
    allData=myBook.readlines()
    myBook.close()
    myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt",'w')
    for i in allData:
        if int(i.strip('\n').split("|")[0])!=idd:
            myBook.write(i)
    myBook.close()


removeBook(102)