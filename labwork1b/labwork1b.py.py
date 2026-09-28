students = []
courses = []


def input_students():
    count = int(input("Enter the number of students: "))

    for i in range(count):
        print(f"\nStudent {i + 1}")
        student_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob,
            "marks": {}
        }

        students.append(student)


def input_courses():
    count = int(input("Enter the number of courses: "))

    for i in range(count):
        print(f"\nCourse {i + 1}")
        course_id = input("Course ID: ")
        name = input("Course name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)


def list_courses():
    if not courses:
        print("There are no courses yet.")
        return

    print("\nCourse list:")
    for course in courses:
        print(course["id"], "-", course["name"])


def list_students():
    if not students:
        print("There are no students yet.")
        return

    print("\nStudent list:")
    for student in students:
        print(student["id"], "-", student["name"], "-", student["dob"])


def input_marks():
    if not students or not courses:
        print("Please enter students and courses first.")
        return

    list_courses()
    course_id = input("Enter the course ID: ")

    selected_course = None
    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    for student in students:
        mark = float(input(f"Enter the mark for {student['name']}: "))
        student["marks"][course_id] = mark


def show_marks():
    if not courses:
        print("There are no courses yet.")
        return

    list_courses()
    course_id = input("Enter the course ID: ")

    selected_course = None
    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print(f"\nMarks for {selected_course['name']}:")
    for student in students:
        if course_id in student["marks"]:
            print(student["name"], ":", student["marks"][course_id])
        else:
            print(student["name"], ": no mark entered")


while True:
    print("\n--- STUDENT MARK MANAGEMENT ---")
    print("1. Enter students")
    print("2. Enter courses")
    print("3. Enter marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks for a course")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        list_students()
    elif choice == "5":
        list_courses()
    elif choice == "6":
        show_marks()
    elif choice == "0":
        print("Program ended.")
        break
    else:
        print("Invalid option.")