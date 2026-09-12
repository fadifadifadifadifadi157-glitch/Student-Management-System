# Student Management System

A simple **console-based Student Management System** built with
**Python** and **Object-Oriented Programming (OOP)** principles.

The application allows users to manage student records through a
menu-driven command-line interface. Users can add, update, delete, and
display student information.

> **Repository:**
> https://github.com/fadifadifadifadifadi157-glitch/Student-Management-System

## Features

-   Add a new student
-   Prevent duplicate student roll numbers
-   Update an existing student's name and age
-   Delete a student by roll number
-   Display all registered students
-   Interactive command-line menu
-   Uses Python classes and objects to organize student data
-   Handles the basic CRUD operations:
    -   **Create** --- Add Student
    -   **Read** --- Display Students
    -   **Update** --- Update Student
    -   **Delete** --- Delete Student

## Technologies Used

-   **Python 3**
-   **Object-Oriented Programming (OOP)**
-   **Python Dictionary** for in-memory student storage
-   **Command-Line Interface (CLI)** for user interaction

No external libraries or database are required by the current
implementation.

## Project Structure

``` text
Student Management System/
└── main.py
```

### Main Components

#### `Student` Class

The `Student` class represents an individual student.

It stores:

-   `Roll_no` --- Student roll number
-   `Name` --- Student name
-   `Age` --- Student age

The `Display()` method prints the student's information.

#### `School` Class

The `School` class manages the collection of students.

It contains a dictionary:

``` python
self.students = {}
```

The student's roll number is used as the dictionary key.

The class provides the following operations:

  Method            Purpose
  ----------------- -------------------------------------------
  `Add()`           Adds a new student
  `Update()`        Updates an existing student's information
  `delete()`        Deletes a student
  `display_all()`   Displays all students
  `Menu()`          Runs the main application menu

## How It Works

When the program starts, a `School` object is created and its menu is
launched:

``` python
s1 = School()
s1.Menu()
```

The user is presented with five options:

``` text
1. Add Student
2. Update Student
3. Delete Student
4. Display Students
5. Exit
```

### 1. Add Student

The program asks for:

-   Roll number
-   Name
-   Age

Before adding the student, it checks whether the roll number already
exists.

If the roll number is already registered, the program displays:

``` text
Student already Exsists!
```

Otherwise, the student is added successfully.

### 2. Update Student

The user enters a roll number. If the student exists, the program asks
for a new name and age and updates the record.

### 3. Delete Student

The user enters a roll number. If the student exists, the corresponding
record is removed from the dictionary.

### 4. Display Students

All students currently stored in memory are displayed with their name,
roll number, and age.

If there are no students, the program displays:

``` text
No student!
```

### 5. Exit

Selecting option `5` exits the application and displays:

``` text
Thank You!
```

## Installation

### Prerequisites

Install **Python 3** on your computer.

You can verify your Python installation with:

``` bash
python --version
```

or:

``` bash
python3 --version
```

### Clone the Repository

``` bash
git clone https://github.com/fadifadifadifadifadi157-glitch/Student-Management-System.git
```

Move into the project directory:

``` bash
cd Student-Management-System
```

## Run the Program

Run:

``` bash
python main.py
```

If your system uses `python3`:

``` bash
python3 main.py
```

The Student Management System menu will then appear in the terminal.

## Example

``` text
================Students Management System================
1.Add Student
2.Update Student
3.Delete Student
4.Display Students
5.Exit
==========================================================
Enter your choice: 1

Enter the Roll Number: 101
Enter the Name: Ali
Enter the Age: 20
Student Added Successfully!
```

Displaying students:

``` text
----------------------Students List----------------------
Student Name:  Ali
Student Roll Number:  101
Age:  20
---------------------------------------------------------
```

## Data Storage

The current application stores student records in a Python dictionary:

``` python
self.students = {}
```

This means that **student data is stored only in memory while the
program is running**.

There is currently:

-   No MySQL database
-   No SQLite database
-   No JSON/CSV file storage
-   No login/authentication system
-   No permanent data storage

Therefore, all records are lost when the program exits.

## Code Analysis

The project demonstrates several fundamental programming concepts:

### Object-Oriented Programming

The application separates student data and school management
responsibilities into two classes:

``` text
Student
   │
   └── Represents a student

School
   │
   ├── Add
   ├── Update
   ├── Delete
   ├── Display
   └── Menu
```

This makes the program easier to understand and provides a foundation
for extending the system.

### Dictionary-Based Records

Students are stored using their roll number as the key:

``` python
self.students[roll] = student
```

This allows the program to quickly check whether a student exists and
retrieve records by roll number.

### CRUD Operations

The project implements the basic CRUD pattern:

``` text
Create → Add Student
Read   → Display Students
Update → Update Student
Delete → Delete Student
```

## Current Limitations

The current version is intentionally simple and suitable as a
beginner-level Python/OOP project.

Some limitations include:

-   Student data is not persistent.
-   Input validation is limited.
-   Entering a non-numeric age can cause a `ValueError`.
-   Entering a non-numeric menu choice can cause a `ValueError`.
-   There is no search-specific menu option.
-   There is no authentication or authorization.
-   There is no graphical user interface.
-   There is no database integration.
-   There is no automated test suite.

## Possible Future Improvements

The project can be extended with:

-   Persistent storage using **SQLite** or **MySQL**
-   Search students by roll number or name
-   Input validation and exception handling
-   A dedicated `search()` method
-   Student email and contact information
-   Attendance management
-   Course/subject management
-   Grade management
-   Authentication and user roles
-   GUI using Tkinter or PyQt
-   Web interface using Flask, Django, or another framework
-   Automated unit tests
-   Export/import using CSV or JSON

## Learning Objectives

This project is useful for practicing:

-   Python classes and objects
-   Constructors
-   Instance attributes
-   Methods
-   Dictionaries
-   Conditional statements
-   Loops
-   User input
-   CRUD logic
-   Menu-driven programs
-   Basic software organization

## Author

**Student Management System**

GitHub repository:

https://github.com/fadifadifadifadifadi157-glitch/Student-Management-System

## License

No license is currently specified in the provided project/repository
information.
