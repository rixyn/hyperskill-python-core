import re


class Student:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f"Student(first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"


def is_valid_name(name):
    if len(name) < 2:
        return None
    pattern = r"^[A-Za-z]+([-' ][A-Za-z]+)*$"
    return re.match(pattern, name) is not None


def is_valid_email(email):
    # pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"
    pattern = r"^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{1,}$"
    return re.match(pattern, email) is not None


def process_student_credentials(credentials):

    parts = credentials.split()

    if len(parts) <= 2:
        return "Incorrect credentials"

    first_name = parts[0]
    parts.remove(first_name)

    email = parts[-1]
    parts.remove(email)

    last_name = ' '.join(parts)

    if not is_valid_name(first_name):
        return "Incorrect first name."
    if not is_valid_name(last_name):
        return "Incorrect last name."
    if not is_valid_email(email):
        return "Incorrect email."

    return Student(first_name, last_name, email)


def main():

    students = []
    student_count = 0

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
                    print(f"Total {student_count} students have been added.")
                    break
                student = process_student_credentials(credentials)
                if isinstance(student, Student):
                    students.append(student)
                    student_count += 1
                    print("The student has been added.")
                else:
                    print(student)
        elif command == "":
            print("No input")
        elif command == "back":
            print("Enter 'exit' to exit the program")
        else:
            print("Unknown command!")


if __name__ == "__main__":
    # Run the example inputs in the question.
    main()
