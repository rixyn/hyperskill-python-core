import re


class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.scores = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}

    def __repr__(self):
        return f"Student(ID={self.student_id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"


# Global variables for students and emails
next_student_id = 10000
students = {}
emails = set()


def is_valid_name(name):
    if len(name) < 2:
        return False
    pattern = r"^[A-Za-z]+([-' ][A-Za-z]+)*$"
    return re.match(pattern, name) is not None


def is_valid_email(email):
    pattern = r"^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{1,}$"
    return re.match(pattern, email) is not None


def process_student_credentials(credentials):
    parts = credentials.split()

    if len(parts) < 3:
        return "Incorrect credentials"

    first_name = parts[0]
    email = parts[-1]
    last_name = ' '.join(parts[1:-1])

    if not is_valid_name(first_name) or not is_valid_name(last_name):
        return "Incorrect name"
    if not is_valid_email(email):
        return "Incorrect email"
    
    return add_student(first_name, last_name, email)


def add_student(first_name, last_name, email):
    global next_student_id
    if email in emails:
        return "This email is already taken."
    student = Student(next_student_id, first_name, last_name, email)
    students[next_student_id] = student
    emails.add(email)
    student_id = next_student_id
    next_student_id += 1
    # return f"The student has been added with id {student_id}."
    return f"The student has been added."


def list_students():
    if not students:
        print("No students found.")
    else:
        print("Students:")
        for student_id in sorted(students.keys()):
            print(student_id)


def add_points():
    print("Enter student ID and points or 'back' to return: ")
    while True:
        input_data = input().strip()
        if input_data.lower() == 'back':
            break

        parts = input_data.split()
        if len(parts) != 5 or not all(part.isdigit() for part in parts):
            print("Incorrect points format.")
            continue

        student_id, *points = map(int, parts)
        if student_id not in students:
            print(f"No student is found for id={student_id}.")
            continue

        if any(p < 0 for p in points):
            print("Incorrect points format.")
            continue

        courses = ["Python", "DSA", "Databases", "Flask"]
        for course, point in zip(courses, points):
            students[student_id].scores[course] += point
        print("Points updated.")


def find_student():
    print("Enter student ID or 'back' to return: ")
    while True:
        student_id = input().strip()
        if student_id.lower() == 'back':
            break

        if not student_id.isdigit() or int(student_id) not in students:
            print(f"No student is found for id={student_id}.")
            continue

        student = students[int(student_id)]
        scores = "; ".join(f"{course}={score}" for course, score in student.scores.items())
        print(f"{student_id} points: {scores}")


def main():
    print("Learning Progress Tracker")

    while True:
        command = input().lower().strip()
        if command == "exit":
            print("Bye!")
            break
        elif command == "add students":
            print("Enter student credentials or 'back' to return: ")
            while True:
                credentials = input().strip()
                if credentials.lower() == 'back':
                    print(f"Total {len(students)} students have been added.")
                    break
                response = process_student_credentials(credentials)
                print(response)
        elif command == "add points":
            add_points()
        elif command == "find":
            find_student()
        elif command == "list":
            list_students()
        elif command == "":
            print("No input")
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
