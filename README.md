🔹 Project Description

This project is a basic Object-Oriented Python program created to understand how classes, objects, constructors, and methods work together in a real-world scenario.

The goal of this project is not complexity, but clarity and structure — building a strong foundation for larger systems.

🔹 What This Project Does

Creates student profiles using a class

Stores student data as object attributes

Displays student information using object methods

Demonstrates the difference between:

printing inside a method

returning values from a method

🔹 Concepts Practiced

Class and Object

__init__ constructor

Instance variables

Object methods

print() vs return

Multiple object handling

🔹 Project Structure
student_profile_manager.py

🔹 Code Overview
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_info(self):
        print(self.name)
        print(self.roll_number)
        print(self.course)


s1 = Student("Tarun", 7, "Ethical Hacking")
s2 = Student("Ritu", 28, "Full Stack")

s1.display_info()
print("-" * 20)
s2.display_info()

🔹 Output Example
Tarun
7
Ethical Hacking
--------------------
Ritu
28
Full Stack

🔹 Why This Project Matters

Most beginners rush into advanced topics without understanding how objects actually work.

This project focuses on:

Writing clean, readable code

Understanding how data and behavior belong together

Preparing a base for future features like:

file handling

validations

reports

automation

🔹 Learning Status

✔ Day 1 completed

✔ OOP foundation built

➡ Next step: input validation and rules (Day 2)

🔹 Author

Tarun Chaudhary
Python Learner | Building in Silence
GitHub: TarunChaudhary-Dev
