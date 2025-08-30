def addBook(id:int,title:str,author:str):
    myBook=open("/Users/abhijanpatra/Documents/Python/Library Management System/LibraryManagementSystem/Books.txt","a+")
    myBook.write(f"{id}|{title}|{author}")
addBook(101,"Atomic Habits","James Clear")