students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    
    student = {"name": name, "marks": marks}
    students.append(student)
    
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found\n")
    else:
        print("Student Records:")
        for s in students:
            print("Name:", s["name"], "| Marks:", s["marks"])
        print()


def search_student():
    name = input("Enter student name to search: ")
    
    for s in students:
        if s["name"] == name:
            print("Student Found")
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            return
    
    print("Student not found\n")


def average_marks():
    if len(students) == 0:
        print("No students available\n")
        return
    
    total = 0
    for s in students:
        total += s["marks"]
    
    avg = total / len(students)
    print("Average Marks:", avg, "\n")


while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Average Marks")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
        
    elif choice == 2:
        display_students()
        
    elif choice == 3:
        search_student()
        
    elif choice == 4:
        average_marks()
        
    elif choice == 5:
        print("Program Ended")
        break
        
    else:
        print("Invalid choice\n")
