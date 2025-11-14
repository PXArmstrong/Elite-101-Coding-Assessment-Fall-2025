from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_books_veiw():
    #Displays a list of all the available books with their details
    print("==- All Available Books -==")
    for book in library_books:
        if book["available"]:
            print(f"ID:{book['id']},Title:{book['title']},Author:{book['author']}")
#Prints out all the books that are marked as available
# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
def book_search(search):
    search=search.lower()
    result=[]
    for book in library_books:
        if(search in book["author"].lower() or search in book["genre"].lower()):
            result.append(book)
    return result
#looks through the dictionary for the keyword in author or genre by lower casing it.
def display_search(result):
    if not result:
        print("No books found matching your search.")
        return
    
    print(f"Search Results({len(result)}books found)")
    for book in result:
        status=" Availble" if book["available"] else " Checked Out"
        print(f"ID: {book['id']}, Title: {book['title']},Author: {book['author']},Status:{status}")
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def book_checkout(book_id):
    for book in library_books:
        if book["id"]==book_id:
            if book["available"]:
                book["available"]=False
                #Making it unavailable
                due_date=datetime.now()+timedelta(days=14)
                book["due_date"]=due_date.strftime("%Y-%m-%d")
                #Set due date to 2 weeks from today
                book["checkouts"]+=1
                #Checkout Counter
                print(f"Sucessfully checked out'{book['title']}'.Due date: {book['due_date']}")
                return True
            else:
                print(f"Sorry,'{book['title']}' is already checked out.")
                return False
    print(f"Book with ID '{book_id}' not found")
    return False
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def book_return(book_id):
    for book in library_books:
        if book["id"]==book_id:
            if not book["available"]:
                book["availbale"]=True
                book["due_date"]=None
                print(f"Sucessfully returned '{book['title']}'.")
                return True
            else:
                print(f"book with ID'{book['title']}' not found.")
                return False
    print(f"Book with Id '{book_id}' not found")
    return False    

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def books_overdue():
    today=datetime.now().date()
    overdue_books= []

    for book in library_books:
        if not book["available"] and book["due_date"]:
            due_date=datetime.strptime(book["due_date"],"%Y-%m-%d").date()
            if due_date<today:
                overdue_books.append(book)
    
    if not overdue_books:
        print("No overdue books found.")
        return
    
    print("OVERDUE BOOKS")
    for book in overdue_books:
        print(f"ID: {book['id']}, Title: {book['title']}, Due Date: {book['due_date']}")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    available_books_veiw()
    print("  ")
    result=book_search("Fantasy")
    display_search(result)
    print(" ")
    result=book_search("Rick")
    display_search(result)
    print(" ")
    book_checkout("B1")
    print(" ")
    books_overdue()