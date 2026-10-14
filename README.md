# 📚 Library Management System

A simple Library Management System built using Python. I created this project to practice object-oriented programming, file handling, and working with JSON data.

The project allows an admin to manage books and students to enroll, issue books, and return them. Book and student records are stored in JSON files, so the data can be loaded again when the program runs.

## ✨ Features

### 🔐 Admin
- Add new books to the library.
- Update the available copy count of a book.
- View information about a specific book.
- Display all books stored in the system.
- Delete a book record.

### 🎓 Student
- Register as a new student.
- Generate a unique student ID.
- Issue a book if copies are available.
- Return an issued book.
- View available books and their details.

### 💾 Data Storage
- Stores book records in `Library.json`.
- Stores student records in `Student.json`.
- Saves changes to JSON files when books or student records are updated.

## 🛠️ Technologies Used

- **Python** — Main programming language
- **OOP** — Classes, objects, inheritance, class methods, and static methods
- **JSON** — Storing and retrieving book and student records
- **File Handling** — Reading and writing data using files
- **Built-in Modules** — `json`, `random`, `string`, and `pathlib`

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py
├── Library.json
├── Student.json
└── README.md
```
## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Library-Management-System
```

### 3. Run the program

```bash
python main.py
```

No external Python packages are required because the project uses built-in Python modules.

## 🖥️ How It Works

When the program starts, you can choose between Admin and Student.

- **Admin:** Enter the admin password to access book management options.
- **Student:** Register as a student or use the available options to issue and return books.

The system checks book IDs, student IDs, and available copies before processing book issues and returns.

Book and student data are maintained separately in JSON files.

## 📖 Concepts Practiced

While building this project, I practiced:

- Classes and objects
- Inheritance
- Class methods and static methods
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- File handling
- JSON serialization and deserialization
- Working with records stored in lists of dictionaries

## 🔧 Future Improvements

Some improvements I would like to make next:

- Add stronger validation for user input.
- Prevent duplicate student IDs and book IDs.
- Improve error handling for invalid or corrupted JSON files.
- Store issued books using book IDs instead of only book names.
- Add a proper login system for administrators.
- Add a graphical interface and a database such as SQLite or PostgreSQL.

## 👨‍💻 About

This is a learning project built to strengthen my Python fundamentals and understand how different programming concepts work together in a practical application.

I plan to improve it further as I continue learning Python.

**Feedback and suggestions are welcome!**
