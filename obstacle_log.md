# Obstacle Log - Mini Library Management System

## 1. Book data was resetting after restarting the program

### Problem
Books added during one program run disappeared when the program was restarted.

### Solution
The book list is currently stored in Python memory. A sample data file was created separately, and borrowing records are saved to a text file for persistence.

---

## 2. Preventing unavailable books from being borrowed

### Problem
A book that was already borrowed should not be available to another user.

### Solution
An `available` field was added to every book. When a book is borrowed, its value changes to `False`. The program checks this value before allowing a new borrowing.

---

## 3. Calculating the due date

### Problem
The system needed to automatically calculate when a borrowed book should be returned.

### Solution
Python's `datetime` module was used. The due date is calculated as 7 days after the borrowing date.

---

## 4. Testing overdue books

### Problem
Waiting seven days to test the overdue functionality was not practical.

### Solution
A temporary due date in the past was used during testing. After confirming that overdue books were detected correctly, the normal 7-day due date was restored.

---

## 5. Keeping borrowing information

### Problem
The system needed to keep information about who borrowed each book.

### Solution
A `borrowing_records` list was created. Each borrowing stores the book title, borrower name, borrowing date, and due date.

---

## 6. Creating a user-friendly interface

### Problem
Calling each function separately was inconvenient.

### Solution
A menu-driven interface using a `while` loop and numbered options was created. Users can select the required library operation from the menu.

---

## 7. Saving borrowing records

### Problem
Borrowing records would normally disappear when the program stopped.

### Solution
A function was created to save the borrowing records to `borrowing_records.txt`, providing a persistent log outside the running program.