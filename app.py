
import os

# File to store the library data
LIBRARY_FILE = "library.txt"

# Function to load the library from a file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = eval(file.read())  # Safely evaluate the string as a Python list
        return library
    return []

# Function to save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        file.write(str(library))

# Function to display the menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_status == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status,
    }
    library.append(book)
    print("Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!")
            break
    if not found:
        print("Book not found in the library.")

# Function to search for a book
def search_book(library):
    while True:
        print("Search by:")
        print("1. Title")
        print("2. Author")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice not in ["1", "2"]:
            print("Invalid choice. Please enter 1 or 2.")
            continue  # Prompt the user again

        if choice == "1":
            search_term = input("Enter the title: ").strip().lower()
            matching_books = [book for book in library if search_term in book["title"].lower()]
        elif choice == "2":
            search_term = input("Enter the author: ").strip().lower()
            matching_books = [book for book in library if search_term in book["author"].lower()]

        if matching_books:
            print("Matching Books:")
            for i, book in enumerate(matching_books, 1):
                read_status = "Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        else:
            print("No matching books found.")
        break  # Exit the loop after displaying results

# Function to display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
        return

    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return

    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
    

# import streamlit as st

# class PersonalLibraryManager:
#     def __init__(self):
#         self.library = []

#     # Add a book
#     def add_book(self, title, author, publication_year, genre, read_status):
#         book = {
#             "title": title,
#             "author": author,
#             "publication_year": publication_year,
#             "genre": genre,
#             "read_status": read_status
#         }
#         self.library.append(book)
#         st.success("Book added successfully!")

#     # Remove a book
#     def remove_book(self, title_to_remove):
#         # Check if the book exists in the library
#         found_books = [book for book in self.library if book['title'].lower() == title_to_remove.lower()]
#         if found_books:
#             self.library = [book for book in self.library if book['title'].lower() != title_to_remove.lower()]
#             st.success(f"Book '{title_to_remove}' removed successfully!")
#         else:
#             st.error(f"No book found with the title '{title_to_remove}'.")

#     # Search for a book
#     def search_book(self, search_type, search_value):
#         if search_type == "Title":
#             matching_books = [book for book in self.library if search_value.lower() in book['title'].lower()]
#         else:
#             matching_books = [book for book in self.library if search_value.lower() in book['author'].lower()]
        
#         return matching_books

#     # Display all books
#     def display_books(self):
#         if not self.library:
#             st.warning("Your library is empty.")
#         else:
#             st.write("Your Library:")
#             for idx, book in enumerate(self.library, 1):
#                 read_status = "Read" if book["read_status"] else "Unread"
#                 st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")

#     # Display statistics
#     def display_statistics(self):
#         total_books = len(self.library)
#         if total_books == 0:
#             st.warning("No books in the library.")
#             return
        
#         read_books = sum(1 for book in self.library if book["read_status"])
#         percentage_read = (read_books / total_books) * 100

#         st.write(f"Total books: {total_books}")
#         st.write(f"Percentage read: {percentage_read:.2f}%")

# def main():
#     st.title("Personal Library Manager")
    
#     # Create an instance of the library manager
#     library_manager = PersonalLibraryManager()

#     # Sidebar Menu for selecting actions
#     menu = ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics"]
#     choice = st.sidebar.selectbox("Select an option", menu)

#     if choice == "Add a book":
#         st.subheader("Add a New Book")
#         title = st.text_input("Book Title")
#         author = st.text_input("Author")
#         publication_year = st.number_input("Publication Year", min_value=1000, max_value=2100, step=1)
#         genre = st.text_input("Genre")
#         read_status = st.radio("Have you read this book?", ("Yes", "No"))
        
#         if st.button("Add Book"):
#             library_manager.add_book(title, author, publication_year, genre, read_status == "Yes")

#     elif choice == "Remove a book":
#         st.subheader("Remove a Book")
#         title_to_remove = st.text_input("Enter the title of the book to remove")

#         if st.button("Remove Book"):
#             library_manager.remove_book(title_to_remove)

#     elif choice == "Search for a book":
#         st.subheader("Search for a Book")
#         search_type = st.selectbox("Search by", ["Title", "Author"])
#         search_value = st.text_input(f"Enter the {search_type.lower()} to search")
        
#         if st.button("Search Book"):
#             matching_books = library_manager.search_book(search_type, search_value)
#             if matching_books:
#                 for idx, book in enumerate(matching_books, 1):
#                     read_status = "Read" if book["read_status"] else "Unread"
#                     st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")
#             else:
#                 st.error(f"No books found matching {search_value}")

#     elif choice == "Display all books":
#         st.subheader("All Books")
#         library_manager.display_books()

#     elif choice == "Display statistics":
#         st.subheader("Library Statistics")
#         library_manager.display_statistics()

# if __name__ == "__main__":
#     main()
