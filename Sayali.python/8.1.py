student_names = []
student_grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    student_names.append(name)
    student_grades.append(grade)
    print("Student added successfully!")

def update_grade():
    name = input("Enter the name of the student to update: ")
    if name in student_names:
        index = student_names.index(name)
        new_grade = float(input("Enter the new grade: "))
        student_grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found!")

def remove_student():
    name = input("Enter the name of the student to remove: ")
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print("Student removed successfully!")
    else:
        print("Student not found!")

def calculate_average():
    if student_grades:
        average = sum(student_grades) / len(student_grades)
        print(f"Average grade of the class is: {average:.2f}")
    else:
        print("No grades available to calculate average.")

def display_extremes():
    if student_grades:
        highest = max(student_grades)
        lowest = min(student_grades)
        print(f"Highest grade in class: {highest}")
        print(f"Lowest grade in class: {lowest}")
    else:
        print("No grades available to show highest/lowest.")

while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Show Highest and Lowest Grade")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        calculate_average()
    elif choice == '5':
        display_extremes()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

