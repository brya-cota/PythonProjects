'''
Brya Cota
4/14/26
CSC101
This program is a comprehensive student management system where institutions can manage students, their courses,
and related information. In this program I'll demonstrate how to define and manage multiple attributes and methods,
use class relationships (object composition), instantiate multiple objects and store them in collections and access,
update, and display object data through methods.
'''

# Implement a Course class that represents information about a course.
# Attributes: course name, course code, credits
class Course:
    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

    # __str__(self) #returns a readable course string (e.g., "CSC101 - Intro to Python (3 credits)")'''
    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.credits} credits)"


# Implement a Student class that represents student information.
# Attributes: name, student ID, list of enrolled courses
class Student:
    # __init__(self, name, student_id)
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    # enroll(self, course) - adds a course
    def enroll(self, course):
        # Adding course to enrolled_courses[] list
        self.enrolled_courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    # drop(self, course) - removes a course IF it exists
    def drop(self, course):
        # Dropping course from enrolled_courses[] list
        self.enrolled_courses.remove(course)
        print(f"{self.name} dropped {course.course_name}")

    # display_info(self) – prints student details and a list of courses
    def display_info(self):
        print(f"Student Name: {self.name} "
              f"\nStudent ID: {self.student_id} "
              f"\nEnrolled Courses: ")
        for course in self.enrolled_courses:
            print(f"- {course}")



# Create 3 course objects
course1 = Course("Python", "CSC101", 3)
course2 = Course("Calculus II", "MAT241", 3)
course3 = Course("Math", "MAT227", 4)


# Create 2 student objects
student1 = Student("Alice Johnson", "S12345")
student2 = Student("Bob Martinez", "S67890")

# Enroll each student in at least 2 courses
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course3)
student2.enroll(course1)

print("")

# Display student information
student1.display_info()
print("")
student2.display_info()

# Dropping course from student 1
print("")
student1.drop(course2)
print("")

# Display after dropping a course
student1.display_info()