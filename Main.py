
from LibraryManagementSystem.UtilityClasses.Books import Books
from LibraryManagementSystem.UtilityClasses.Login import Login
book=Books()
login=Login()
print("Welcome to Library Management System")
print("1.Sign Up")
print("2.Sign In")
choice=int(input())
match choice:
    case 1:
        login.SignUP()
    case 2:
        login.SignIN()
print(login.permission)
if login.permission:
    print("1-Admin")
    print("2-Student")
    choice=int(input())
    match choice:
        case 1:
            print("1-Add Book")
            print("2-Remove Book")
            print("3-Issue Book")
            print("4-Return Book")
            print("5-Search Book")
            print("6-Display Book")
            print("7-Show Students")
            choice=int(input())
            match choice:
                case 1:
                    bookId=int(input("Enter Book ID: "))
                    bookTitle=input("Enter Book Title: ")
                    bookAuthor=input("Enter Book Author: ")
                    book.addBook(bookId,bookTitle,bookAuthor)
                case 2:
                    bookId=int(input("Enter Book ID: "))
                    print(f"{book.removeBook(bookId)} has been removed")
                case 3:
                    bookId=int(input("Enter Book ID: "))
                    book.issueBook(bookId)
                case 4:
                    bookId=int(input("Enter Book ID: "))
                    book.returnBook(bookId)
                case 5:
                    bookTitle=input("Enter Book Title: ")
                    print(book.searchBook(bookTitle))
                case 6:
                    book.displayBook()
                case 7:
                    book.showStudents()
        case 2:
            print("1-Issue Book")
            print("2-Return Book")
            print("3-Search Book")
            print("4-Display Book")
            choice=int(input())
            match choice:
                case 1:
                    bookId = int(input("Enter Book ID: "))
                    Books.issueBook(bookId)
                case 2:
                    bookId = int(input("Enter Book ID: "))
                    book.returnBook(bookId)
                case 3:
                    bookTitle=input("Enter Book Title: ")
                    print(book.searchBook(bookTitle))
                case 4:
                    book.displayBook()
