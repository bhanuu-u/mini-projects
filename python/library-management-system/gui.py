import tkinter as tk
from tkinter import messagebox

from library_managemnet_system import library, Book


# -----------------------------------
# Library
# -----------------------------------

my_library = library()
my_library.load_books()


# -----------------------------------
# Main Window
# -----------------------------------

window = tk.Tk()

window.title("Library Management System")
window.geometry("1000x700")
window.configure(bg="#0F172A")


# -----------------------------------
# Title
# -----------------------------------

title = tk.Label(
    window,
    text="📚 Library Management System",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#0F172A"
)

title.pack(pady=25)


# -----------------------------------
# Search Section
# -----------------------------------

search_frame = tk.Frame(
    window,
    bg="#0F172A"
)

search_frame.pack(pady=5)


search_entry = tk.Entry(
    search_frame,
    width=40,
    font=("Arial", 14),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat"
)

search_entry.pack(
    side="left",
    padx=10,
    ipady=8
)


# -----------------------------------
# Books Container
# -----------------------------------

books_container = tk.Frame(
    window,
    bg="#1E293B",
    width=850,
    height=400
)

books_container.pack(
    pady=20,
    padx=30
)

books_container.pack_propagate(False)


# -----------------------------------
# Canvas
# -----------------------------------

canvas = tk.Canvas(
    books_container,
    bg="#1E293B",
    highlightthickness=0
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)


# -----------------------------------
# Scrollbar
# -----------------------------------

scrollbar = tk.Scrollbar(
    books_container,
    orient="vertical",
    command=canvas.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)


canvas.configure(
    yscrollcommand=scrollbar.set
)


# -----------------------------------
# Frame inside Canvas
# -----------------------------------

books_frame = tk.Frame(
    canvas,
    bg="#1E293B"
)


canvas_window = canvas.create_window(
    (0, 0),
    window=books_frame,
    anchor="nw"
)


# -----------------------------------
# Resize Canvas
# -----------------------------------

def resize_books(event):

    canvas.itemconfig(
        canvas_window,
        width=event.width
    )


canvas.bind(
    "<Configure>",
    resize_books
)


# -----------------------------------
# Update Scroll Region
# -----------------------------------

def update_scroll():

    books_frame.update_idletasks()

    canvas.configure(
        scrollregion=canvas.bbox("all")
    )


# -----------------------------------
# Borrow Book
# -----------------------------------

def borrow_book(bookname):

    result = my_library.borrow_book(bookname)

    if result:
        messagebox.showinfo(
            "Success",
            f"{bookname} has been borrowed."
        )

        display_books()


# -----------------------------------
# Return Book
# -----------------------------------

def return_book(bookname):

    result = my_library.return_book(bookname)

    if result:
        messagebox.showinfo(
            "Success",
            f"{bookname} has been returned."
        )

        display_books()


# -----------------------------------
# Display Books
# -----------------------------------

def display_books(book_list=None):

    # Remove old book cards
    for widget in books_frame.winfo_children():
        widget.destroy()


    if book_list is None:
        book_list = my_library.books


    # No books
    if len(book_list) == 0:

        empty_label = tk.Label(
            books_frame,
            text="No books found",
            font=("Arial", 16, "bold"),
            fg="#CBD5E1",
            bg="#1E293B"
        )

        empty_label.pack(pady=50)

        update_scroll()

        return


    # Create book cards
    for book in book_list:

        book_frame = tk.Frame(
            books_frame,
            bg="#334155",
            padx=15,
            pady=12
        )

        book_frame.pack(
            fill="x",
            padx=15,
            pady=6
        )


        # Book name
        name = tk.Label(
            book_frame,
            text=book.bookname,
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#334155"
        )

        name.pack(
            anchor="w"
        )


        # Author
        author = tk.Label(
            book_frame,
            text=f"Author: {book.author}",
            font=("Arial", 11),
            fg="#CBD5E1",
            bg="#334155"
        )

        author.pack(
            anchor="w",
            pady=3
        )


        # Status
        status = "Available" if book.available else "Borrowed"

        status_color = "#4ADE80" if book.available else "#F87171"


        availability = tk.Label(
            book_frame,
            text=f"Status: {status}",
            font=("Arial", 11, "bold"),
            fg=status_color,
            bg="#334155"
        )

        availability.pack(
            anchor="w",
            pady=3
        )


        
        if book.available:

            action_button = tk.Button(
                book_frame,
                text="Borrow",
                font=("Arial", 10, "bold"),
                bg="#2563EB",
                fg="white",
                activebackground="#1D4ED8",
                activeforeground="white",
                relief="flat",
                padx=15,
                pady=5,
                command=lambda name=book.bookname: borrow_book(name)
            )

        else:

            action_button = tk.Button(
                book_frame,
                text="Return",
                font=("Arial", 10, "bold"),
                bg="#16A34A",
                fg="white",
                activebackground="#15803D",
                activeforeground="white",
                relief="flat",
                padx=15,
                pady=5,
                command=lambda name=book.bookname: return_book(name)
            )


        action_button.pack(
            anchor="e"
        )


    update_scroll()


# -----------------------------------
# Search Book
# -----------------------------------

def search_book():

    search_text = search_entry.get().strip()


    if search_text == "":

        display_books()

        return


    results = []

    for book in my_library.books:

        if search_text.lower() in book.bookname.lower():

            results.append(book)


    display_books(results)


# -----------------------------------
# Add Book
# -----------------------------------

def add_book_window():

    add_window = tk.Toplevel(window)

    add_window.title("Add Book")

    add_window.geometry("400x300")

    add_window.configure(
        bg="#0F172A"
    )


    title = tk.Label(
        add_window,
        text="Add New Book",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0F172A"
    )

    title.pack(pady=20)


    
    name_label = tk.Label(
        add_window,
        text="Book Name",
        font=("Arial", 11),
        fg="white",
        bg="#0F172A"
    )

    name_label.pack()


    name_entry = tk.Entry(
        add_window,
        width=35,
        font=("Arial", 12)
    )

    name_entry.pack(
        pady=8
    )


    
    author_label = tk.Label(
        add_window,
        text="Author",
        font=("Arial", 11),
        fg="white",
        bg="#0F172A"
    )

    author_label.pack()


    author_entry = tk.Entry(
        add_window,
        width=35,
        font=("Arial", 12)
    )

    author_entry.pack(
        pady=8
    )


    def save_new_book():

        bookname = name_entry.get().strip()

        author = author_entry.get().strip()


        if bookname == "" or author == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter both book name and author."
            )

            return


       
        if my_library.search_book(bookname):

            messagebox.showwarning(
                "Book Exists",
                "This book already exists."
            )

            return


        new_book = Book(
            bookname,
            author
        )


        my_library.add_book(new_book)


        messagebox.showinfo(
            "Success",
            "Book has been added successfully."
        )


        add_window.destroy()

        display_books()


    save_button = tk.Button(
        add_window,
        text="Add Book",
        font=("Arial", 11, "bold"),
        bg="#16A34A",
        fg="white",
        activebackground="#15803D",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=7,
        command=save_new_book
    )

    save_button.pack(
        pady=15
    )


# -----------------------------------
# Remove Book
# -----------------------------------

def remove_book_window():

    remove_window = tk.Toplevel(window)

    remove_window.title("Remove Book")

    remove_window.geometry("400x220")

    remove_window.configure(
        bg="#0F172A"
    )


    title = tk.Label(
        remove_window,
        text="Remove Book",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0F172A"
    )

    title.pack(pady=20)


    name_entry = tk.Entry(
        remove_window,
        width=35,
        font=("Arial", 12)
    )

    name_entry.pack(
        pady=10
    )


    def remove_book():

        bookname = name_entry.get().strip()


        if bookname == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter a book name."
            )

            return


        result = my_library.remove_book(bookname)


        if result:

            messagebox.showinfo(
                "Success",
                "Book has been removed."
            )

            remove_window.destroy()

            display_books()

        else:

            messagebox.showerror(
                "Not Found",
                "Book not found."
            )


    remove_button = tk.Button(
        remove_window,
        text="Remove",
        font=("Arial", 11, "bold"),
        bg="#DC2626",
        fg="white",
        activebackground="#B91C1C",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=7,
        command=remove_book
    )

    remove_button.pack(
        pady=10
    )


# -----------------------------------
# Search Button
# -----------------------------------

search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=search_book
)

search_button.pack(
    side="left"
)


# -----------------------------------
# Bottom Buttons
# -----------------------------------

button_frame = tk.Frame(
    window,
    bg="#0F172A"
)

button_frame.pack(
    pady=10
)


# Add button
add_button = tk.Button(
    button_frame,
    text="Add Book",
    font=("Arial", 12, "bold"),
    bg="#16A34A",
    fg="white",
    activebackground="#15803D",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=add_book_window
)

add_button.pack(
    side="left",
    padx=10
)


# Remove button
remove_button = tk.Button(
    button_frame,
    text="Remove Book",
    font=("Arial", 12, "bold"),
    bg="#DC2626",
    fg="white",
    activebackground="#B91C1C",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=remove_book_window
)

remove_button.pack(
    side="left",
    padx=10
)


refresh_button = tk.Button(
    button_frame,
    text="Refresh",
    font=("Arial", 12, "bold"),
    bg="#F59E0B",
    fg="white",
    activebackground="#D97706",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=display_books
)

refresh_button.pack(
    side="left",
    padx=10
)


# -----------------------------------
# Display books when program starts
# -----------------------------------

display_books()


# -----------------------------------
# Start application
# -----------------------------------

window.mainloop()