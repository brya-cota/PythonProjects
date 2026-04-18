'''
Brya Cota
3/30/26
This program is to practice and create basic functions that take parameters and return values.
'''
import math

def display_grade(student_name, subject, grade):
    print("\nStudent Name:", student_name, "\nSubject:", subject, "\nGrade:", grade)

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

def convert_to_uppercase(text):
    text = text.upper()
    return text

student = input("Please enter your name: ").title()
sub = input("Please enter your subject: ").title()
letter_grade = input("Please enter your grade: ").title()
display_grade(student, sub, letter_grade)

print("\nThe area of the circle is:", calculate_circle_area(10))

print("Text converted to uppercase:", convert_to_uppercase("zoey"))
