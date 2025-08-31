# Mini Library Management System with JSON Storage

import json
import os

FILE_NAME = "library.json"

# Load existing book data
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save book data
def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

# Add a new book
def add_book():
    books = load_books()
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    book = {"Book ID": book_id, 
            "Title": title, 
            "Author": author, 
            "Quantity": quantity
            }
    books.append(book)
    save_books(books)
    print("Book added successfully!\n")

# View all books
def view_books():
    books = load_books()
    if not books:
        print(" No books found.\n")
        return
    print("\n Available Books:")
    for book in books:
        print(book)
    print()

# Borrow a book
def borrow_book():
    books = load_books()
    book_id = input("Enter Book ID to borrow: ")
    for book in books:
        if book["Book ID"] == book_id:
            if book["Quantity"] > 0:
                book["Quantity"] -= 1
                save_books(books)
                print(" Book borrowed successfully!\n")
            else:
                print(" Book not available.\n")
            return
    print("Book not found.\n")

# Return a book
def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["Book ID"] == book_id:
            book["Quantity"] += 1
            save_books(books)
            print("Book returned successfully!\n")
            return
    print("Book not found.\n")

# Main menu
def main():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
