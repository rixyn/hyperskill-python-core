import re

# Global variables
next_student_id = 10000
students = {}
emails = set()
# Course requirements for completion
course_requirements = {"Python": 600,
                       "DSA": 400, "Databases": 480, "Flask": 550}


# Student class definition
class Student:
    def __init__(self, student_id, first_name, last_name, email):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.scores = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
        self.enrolled_courses = set()

    def update_scores(self, course, points):
        if points > 0:
            self.enrolled_courses.add(course)
        self.scores[course] += points

    def __repr__(self):
        return f"Student(ID={self.student_id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"


# Validation functions


def is_valid_name(name):
    if len(name) < 2:
        return False
    pattern = r"^[A-Za-z]+([-' ][A-Za-z]+)*$"
    return re.match(pattern, name) is not None


def is_valid_email(email):
    pattern = r"^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None

# Function to process student credentials


def process_student_credentials(credentials):
    parts = credentials.split()

    if len(parts) < 3:
        return "Incorrect credentials"

    first_name = parts[0]
    email = parts[-1]
    last_name = ' '.join(parts[1:-1])

    if not is_valid_name(first_name):
        return "Incorrect first name"
    if not is_valid_name(last_name):
        return "Incorrect last name"
    if not is_valid_email(email):
        return "Incorrect email"

    return add_student(first_name, last_name, email)

# Function to add a student


def add_student(first_name, last_name, email):
    global next_student_id
    if email in emails:
        return "This email is already taken."
    student = Student(next_student_id, first_name, last_name, email)
    students[next_student_id] = student
    emails.add(email)
    student_id = next_student_id
    next_student_id += 1
    return f"The student has been added."

# Function to list all students


def list_students():
    if not students:
        print("No students found.")
    else:
        print("Students:")
        for student_id in sorted(students.keys()):
            print(student_id)

# Function to add points to a student's course


def add_points():
    print("Enter student ID and points or 'back' to return: ")
    while True:
        input_data = input().strip()
        if input_data.lower() == 'back':
            break

        parts = input_data.split()
        if len(parts) != 5 or not all(part.isdigit() for part in parts[1:]):
            print("Incorrect points format.")
            continue

        student_id, *points = map(int, parts)
        if student_id not in students:
            print(f"No student is found for id={student_id}.")
            continue

        courses = ["Python", "DSA", "Databases", "Flask"]
        for course, point in zip(courses, points):
            students[student_id].update_scores(course, point)
        print("Points updated.")


def find_student():
    print("Enter student ID or 'back' to return: ")
    while True:
        student_id_input = input().strip()
        if student_id_input.lower() == 'back':
            break

        if not student_id_input.isdigit() or int(student_id_input) not in students:
            print(f"No student is found for id={student_id_input}.")
            continue

        student = students[int(student_id_input)]
        scores = "; ".join(f"{course}={score}" for course,
                           score in student.scores.items())
        print(f"{student_id_input} points: {scores}")


def calculate_course_statistics():
    stats = {"enrollment": {}, "activity": {}, "average_score": {}}
    course_names = ["Python", "DSA", "Databases", "Flask"]

    for course in course_names:
        enrolled_students = [
            s for s in students.values() if course in s.enrolled_courses]
        total_points = sum(s.scores[course] for s in enrolled_students)
        total_submissions = sum(
            1 for s in enrolled_students if s.scores[course] > 0)

        stats["enrollment"][course] = len(enrolled_students)
        stats["activity"][course] = total_submissions
        stats["average_score"][course] = (
            total_points / total_submissions if total_submissions else 0)

    return stats


def display_course_statistics():
    stats = calculate_course_statistics()
    most_popular, least_popular = find_most_and_least_popular(
        stats["enrollment"])
    highest_activity, lowest_activity = find_highest_and_lowest_activity(
        stats["activity"])
    easiest_course, hardest_course = find_easiest_and_hardest_course(
        stats["average_score"])

    print("Type the name of a course to see details or 'back' to quit:")
    print("Most popular:", ", ".join(most_popular) or "n/a")
    print("Least popular:", ", ".join(least_popular) or "n/a")
    print("Highest activity:", ", ".join(highest_activity) or "n/a")
    print("Lowest activity:", ", ".join(lowest_activity) or "n/a")
    print("Easiest course:", ", ".join(easiest_course) or "n/a")
    print("Hardest course:", ", ".join(hardest_course) or "n/a")


def display_course_details(course_name, stats):
    print(course_name)
    print("id\t\tpoints\t\tcompleted")
    for student_id, student in students.items():
        if course_name in student.enrolled_courses:
            points = student.scores[course_name]
            completed = points / course_requirements[course_name] * 100
            print(f"{student_id}\t\t{points}\t\t{round(completed, 1)}%")


def find_most_and_least_popular(enrollment_stats):
    max_enrollment = max(enrollment_stats.values(), default=0)
    min_enrollment = min(enrollment_stats.values(), default=0)

    most_popular = [course for course,
                    count in enrollment_stats.items() if count == max_enrollment]
    least_popular = [course for course,
                     count in enrollment_stats.items() if count == min_enrollment]

    return most_popular, least_popular


def find_highest_and_lowest_activity(activity_stats):
    max_activity = max(activity_stats.values(), default=0)
    min_activity = min(activity_stats.values(), default=0)

    highest_activity = [course for course,
                        count in activity_stats.items() if count == max_activity]
    lowest_activity = [course for course,
                       count in activity_stats.items() if count == min_activity]

    return highest_activity, lowest_activity


def find_easiest_and_hardest_course(average_score_stats):
    max_average_score = max(average_score_stats.values(), default=0)
    min_average_score = min(average_score_stats.values(), default=0)

    easiest_course = [course for course,
                      avg in average_score_stats.items() if avg == max_average_score]
    hardest_course = [course for course,
                      avg in average_score_stats.items() if avg == min_average_score]

    return easiest_course, hardest_course


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
        elif command == "list":
            list_students()
        elif command == "add points":
            add_points()
        elif command == "find":
            find_student()
        elif command == "statistics":
            display_course_statistics()
            while True:
                course_input = input().strip()
                if course_input.lower() == 'back':
                    break
                elif course_input in ["Python", "DSA", "Databases", "Flask"]:
                    display_course_details(course_input)
                else:
                    print("Unknown course.")
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
