from datetime import date, timedelta


# List of books
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "available": True
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "available": True
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "available": True
    }
]


# Borrowing records
borrowing_records = []


# Add a new book
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")


# Search for a book
def search_book():
    search_title = input("Enter the title of the book to search: ")

    for book in books:
        if book["title"].lower() == search_title.lower():

            print(
                f"Book found: {book['title']} by {book['author']}. "
                f"Available: {book['available']}"
            )

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Unavailable")

            return

    print("Book not found.")


# Borrow a book
def borrow_book():
    borrow_title = input("Enter the title of the book to borrow: ")

    for book in books:
        if book["title"].lower() == borrow_title.lower():

            if book["available"]:
                borrower = input("Enter borrower name: ")

                borrow_date = date.today()
                due_date = borrow_date + timedelta(days=7)

                book["available"] = False
                book["borrower"] = borrower
                book["borrow_date"] = borrow_date
                book["due_date"] = due_date

                # Create borrowing record
                record = {
                    "title": book["title"],
                    "borrower": borrower,
                    "borrow_date": borrow_date,
                    "due_date": due_date,
                    "status": "Borrowed",
                    "return_date": None
                }

                borrowing_records.append(record)

                print(
                    f"You have borrowed '{book['title']}' "
                    f"by {book['author']}."
                )
                print(f"Borrower: {borrower}")
                print(f"Borrow date: {borrow_date}")
                print(f"Due date: {due_date}")

            else:
                print(
                    f"Sorry, '{book['title']}' is currently unavailable."
                )

            return

    print("Book not found.")


# Return a book
def return_book():
    return_title = input("Enter the title of the book to return: ")

    for book in books:
        if book["title"].lower() == return_title.lower():

            if not book["available"]:
                book["available"] = True

                # Update the borrowing record
                for record in borrowing_records:
                    if (
                        record["title"].lower() == book["title"].lower()
                        and record["status"] == "Borrowed"
                    ):
                        record["status"] = "Returned"
                        record["return_date"] = date.today()
                        break

                print(f"You have returned '{book['title']}'.")

            else:
                print(f"'{book['title']}' is already available.")

            return

    print("Book not found.")


# Find overdue books
def overdue_books():
    today = date.today()
    found_overdue = False

    for book in books:
        if not book["available"]:

            if today > book["due_date"]:
                print(
                    f"Overdue: '{book['title']}' "
                    f"borrowed by {book['borrower']}."
                )
                print(f"Due date: {book['due_date']}")

                found_overdue = True

    if not found_overdue:
        print("No overdue books.")


# Display library summary
def library_summary():
    total_books = len(books)
    borrowed_books = 0
    available_books = 0

    for book in books:
        if book["available"]:
            available_books += 1
        else:
            borrowed_books += 1

    print("\n===== LIBRARY SUMMARY =====")
    print(f"Total books: {total_books}")
    print(f"Available books: {available_books}")
    print(f"Borrowed books: {borrowed_books}")


# Display borrowing records
def view_borrowing_records():
    if not borrowing_records:
        print("No borrowing records found.")
        return

    print("\n===== BORROWING RECORDS =====")

    for record in borrowing_records:
        print(f"Book: {record['title']}")
        print(f"Borrower: {record['borrower']}")
        print(f"Borrow date: {record['borrow_date']}")
        print(f"Due date: {record['due_date']}")
        print(f"Status: {record['status']}")

        if record["return_date"] is not None:
            print(f"Return date: {record['return_date']}")

        print("-----------------------------")


# Save borrowing records to a text file
def save_records_to_file():
    with open("borrowing_records.txt", "w") as file:

        if not borrowing_records:
            file.write("No borrowing records found.\n")
            print("Borrowing records saved to borrowing_records.txt")
            return

        file.write("===== LIBRARY BORROWING RECORDS =====\n\n")

        for record in borrowing_records:
            file.write(f"Book: {record['title']}\n")
            file.write(f"Borrower: {record['borrower']}\n")
            file.write(f"Borrow date: {record['borrow_date']}\n")
            file.write(f"Due date: {record['due_date']}\n")
            file.write(f"Status: {record['status']}\n")

            if record["return_date"] is not None:
                file.write(f"Return date: {record['return_date']}\n")

            file.write("-----------------------------\n")

    print("Borrowing records saved to borrowing_records.txt")


# Main menu
while True:
    print("\n===== MINI LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Library Summary")
    print("6. View Overdue Books")
    print("7. View Borrowing Records")
    print("8. Save Borrowing Records")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        library_summary()

    elif choice == "6":
        overdue_books()

    elif choice == "7":
        view_borrowing_records()

    elif choice == "8":
        save_records_to_file()

    elif choice == "9":
        save_records_to_file()
        print("Thank you for using the Mini Library Management System.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")