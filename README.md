# Student Management System (Python)

A console-based student and course management system developed as a university course project.
The application allows managing students, courses, and completed course records using
file-based data storage.

## Features
- Add new students with validated personal information
- Search students by first, middle, or last name
- Search courses by name or instructor
- Add or update course completions with grades and dates
- Display a full academic record for a student
- Input validation for dates, grades, and identifiers

## How the System Works
The system stores data in text files:
- `students.txt` — student records
- `courses.txt` — course information
- `passed.txt` — completed courses and grades

All data is read, validated, processed, and written back using Python file handling.

## Technologies Used
- Python 3
- File I/O
- Data validation
- Standard library modules (`datetime`, `random`)

## Project Structure
student-management-system/
├── Main.py
├── students.txt
├── courses.txt
├── passed.txt
└── README.md

## What I Learned
- Designing menu-driven console applications
- Validating user input to prevent invalid data
- Working with persistent file-based storage
- Updating existing records safely
- Structuring a larger Python script into logical functions
