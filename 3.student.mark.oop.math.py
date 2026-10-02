"""Student mark management - Practical Work 3.

Requires NumPy. On Windows, install ``windows-curses`` to enable the decorated
terminal menu; otherwise the program uses the text menu.
"""

import math
import sys

import numpy as np

try:
    import curses
except ImportError:  # curses is not included with standard Python on Windows
    curses = None


students = []
courses = []


def input_students():
    try:
        count = int(input("Enter the number of students: "))
        if count < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    for i in range(count):
        print(f"\nStudent {i + 1}")
        student_id = input("Student ID: ").strip()
        name = input("Student name: ").strip()
        dob = input("Date of birth: ").strip()
        students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})


def input_courses():
    try:
        count = int(input("Enter the number of courses: "))
        if count < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    for i in range(count):
        print(f"\nCourse {i + 1}")
        course_id = input("Course ID: ").strip()
        name = input("Course name: ").strip()
        try:
            credits = float(input("Course credits: "))
            if credits <= 0:
                raise ValueError
        except ValueError:
            print("Credits must be a positive number. Course skipped.")
            continue
        courses.append({"id": course_id, "name": name, "credits": credits})


def list_courses():
    if not courses:
        print("There are no courses yet.")
        return
    print("\nCourse list:")
    for course in courses:
        print(f"{course['id']} - {course['name']} ({course['credits']:g} credits)")


def list_students():
    if not students:
        print("There are no students yet.")
        return
    print("\nStudent list:")
    for student in students:
        print(f"{student['id']} - {student['name']} - {student['dob']}")


def find_course(course_id):
    return next((course for course in courses if course["id"] == course_id), None)


def input_marks():
    if not students or not courses:
        print("Please enter students and courses first.")
        return
    list_courses()
    course_id = input("Enter the course ID: ").strip()
    if find_course(course_id) is None:
        print("Course not found.")
        return

    for student in students:
        try:
            raw_mark = float(input(f"Enter the mark for {student['name']}: "))
            if not 0 <= raw_mark <= 100:
                raise ValueError
        except ValueError:
            print("Mark must be a number from 0 to 100. This student's mark was skipped.")
            continue
        # Round down to one decimal place, as required by the lab.
        student["marks"][course_id] = math.floor(raw_mark * 10) / 10


def show_marks():
    if not students:
        print("There are no students yet.")
        return
    if not courses:
        print("There are no courses yet.")
        return
    list_courses()
    course_id = input("Enter the course ID: ").strip()
    selected_course = find_course(course_id)
    if selected_course is None:
        print("Course not found.")
        return
    print(f"\nMarks for {selected_course['name']}:")
    for student in students:
        mark = student["marks"].get(course_id)
        print(f"{student['name']}: {mark:.1f}" if mark is not None else f"{student['name']}: no mark entered")


def average_gpa(student):
    """Return the credit-weighted average mark, or None if no marks exist."""
    marked_courses = [course for course in courses if course["id"] in student["marks"]]
    if not marked_courses:
        return None
    marks = np.array([student["marks"][course["id"]] for course in marked_courses], dtype=float)
    credits = np.array([course["credits"] for course in marked_courses], dtype=float)
    return float(np.average(marks, weights=credits))


def show_student_gpas():
    if not students:
        print("There are no students yet.")
        return
    print("\nCredit-weighted average marks:")
    for student in students:
        average = average_gpa(student)
        value = f"{average:.2f}" if average is not None else "no marks entered"
        print(f"{student['name']}: {value}")


def sort_students_by_gpa():
    # Students without marks are placed after students with a calculated average.
    students.sort(key=lambda student: (average_gpa(student) is not None,
                                       average_gpa(student) if average_gpa(student) is not None else 0),
                  reverse=True)
    print("Student list sorted by average mark (highest first).")
    list_students()


MENU = [
    ("1", "Enter students", input_students),
    ("2", "Enter courses", input_courses),
    ("3", "Enter marks", input_marks),
    ("4", "List students", list_students),
    ("5", "List courses", list_courses),
    ("6", "Show marks for a course", show_marks),
    ("7", "Show average GPA for students", show_student_gpas),
    ("8", "Sort students by GPA descending", sort_students_by_gpa),
]


def text_menu():
    while True:
        print("\n--- STUDENT MARK MANAGEMENT ---")
        for key, label, _ in MENU:
            print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Program ended.")
            break
        action = next((action for key, _, action in MENU if key == choice), None)
        if action is None:
            print("Invalid option.")
        else:
            action()


def curses_menu(screen):
    curses.curs_set(0)
    while True:
        screen.clear()
        height, width = screen.getmaxyx()
        title = " STUDENT MARK MANAGEMENT "
        screen.addstr(1, max(0, (width - len(title)) // 2), title, curses.A_BOLD)
        for row, (key, label, _) in enumerate(MENU, start=3):
            if row < height - 3:
                screen.addstr(row, 3, f"{key}. {label}")
        if height > 3:
            screen.addstr(height - 2, 3, "0. Exit    Choose an option: ")
        screen.refresh()
        choice = screen.getstr(height - 2, min(width - 1, 31), 8).decode("utf-8", "ignore").strip()
        if choice == "0":
            break
        action = next((action for key, _, action in MENU if key == choice), None)
        if action is None:
            screen.addstr(height - 1, 3, "Invalid option. Press any key.")
            screen.getch()
            continue
        # Let standard input/output handle the data-entry prompts, then redraw curses.
        curses.endwin()
        action()
        input("\nPress Enter to return to the menu...")
        screen = curses.initscr()
        curses.curs_set(0)


def main():
    if curses is None or not sys.stdin.isatty() or not sys.stdout.isatty():
        text_menu()
        return
    try:
        curses.wrapper(curses_menu)
    except curses.error:
        print("Terminal UI is unavailable; switching to the text menu.")
        text_menu()


if __name__ == "__main__":
    main()
