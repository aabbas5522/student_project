from student_app.models.student import Student
from student_app.reports.student_report import display_report
from student_app.services.calculator import calculate_grade
from student_app.utils.validation import validate_marks, validate_name
from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
import json
from student_app.logger import logger

def load_student():
    with open("../data/student.json", "r") as file:
        student = json.load(file)

    return student

def main():
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print()

    student = load_student()

    print("Student Information")
    print("-------------------")

    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester: {student['semester']}")
    print(f"Marks: {student['marks']}")
    
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name")
        logger.warning("Empty student name entered")
        return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered")
        print("Error: Marks must be a number.")
        exit()
    
    if not validate_marks(marks):
        print("Invalid marks")
        return

    grade = calculate_grade(marks)
    student = Student(name, marks, grade)
    display_report(student)


if __name__ == "__main__":
    main()
