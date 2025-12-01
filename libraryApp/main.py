import json

with open("books.json", "r") as file:
    books = json.load(file)


def issueBook():
    print("Issue Book ......")
    try:
        book_id = int(input("Enter the book id: "))
    except:
        print("Invalid input!")
        return
    
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True
            if book["availability"] == True:
                book["availability"] = False
                print(f"Book '{book['title']}' has been issued successfully.")
            else:
                print(f"Book '{book['title']}' is NOT available.")
            break

    if not found:
        print("Book not found!")

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)



def returnBook():
    print("Return Book ......")
    try:
        book_id = int(input("Enter the book id: "))
    except:
        print("Invalid input!")
        return
    
    found = False
    for book in books:
        if book["id"] == book_id:
            found = True
            if book["availability"] == False:
                book["availability"] = True
                print(f"Book '{book['title']}' has been returned successfully.")
            else:
                print("This book was not issued.")
            break

    if not found:
        print("Book not found!")

    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)



def printList():
    print("\n------ All Books ------")
    for book in books:
        print(book)


def fine():
    x = input("Enter Book Holder Name: ")
    print(f"{x}, you have been fined Rs. 1.")


def availableBooks():
    print("\n------ Available Books ------")
    for book in books:
        if book["availability"] == True:
            print(book)



print("------------------------------ Welcome to Book App ------------------------------------")
print("Press 1 to issue a book")
print("Press 2 to return a book")
print("Press 3 to check list of books")
print("Press 4 to fine a person")
print("Press 5 to view available books")

try:
    inp = int(input("Enter the option: "))
except:
    print("Invalid input!")
    exit()

if inp == 1:
    issueBook()
elif inp == 2:
    returnBook()
elif inp == 3:
    printList()
elif inp == 4:
    fine()
elif inp == 5:
    availableBooks()
else:
    print("Invalid option!")
