def check_length(line):
    """S001: Check if line exceeds 79 characters."""
    return 'S001 Too long' if len(line.rstrip()) > 79 else ''


def check_indentation(line):
    """S002: Check if indentation is a multiple of four."""
    stripped_line = line.lstrip()
    indent = len(line) - len(stripped_line)
    return 'S002 Indentation is not a multiple of four' if indent % 4 != 0 and stripped_line else ''


def check_semicolon(line):
    """S003: Check for unnecessary semicolon outside of comments."""
    return 'S003 Unnecessary semicolon' if ';' in line.split('#')[0] else ''


def check_inline_comment_space(line):
    """S004: Check for less than two spaces before inline comment."""
    if '#' in line:
        parts = line.split('#', 1)
        if len(parts[0]) - len(parts[0].rstrip()) < 2 and parts[0].strip():
            return 'S004 At least two spaces required before inline comments'
    return ''


def check_todo_in_comments(line):
    """S005: Check for TODO in comments (case-insensitive)."""
    if '#' in line and 'todo' in line.split('#')[1].lower():
        return 'S005 TODO found'
    return ''


def check_blank_lines(empty_line_count, stripped_line):
    """S006: Check for more than two blank lines preceding a code line."""
    return 'S006 More than two blank lines used before this line' if empty_line_count > 2 and stripped_line else ''


def check_python_style(file_path):
    """Check Python file for various PEP8 style issues using separate functions for each check."""
    with open(file_path, 'r') as file:
        empty_line_count = 0
        for line_number, line in enumerate(file, start=1):
            issues = [
                check_length(line),
                check_indentation(line),
                check_semicolon(line),
                check_inline_comment_space(line),
                check_todo_in_comments(line),
                check_blank_lines(empty_line_count, line.lstrip())
            ]

            # Update empty line count or reset it
            if line.strip() == '':
                empty_line_count += 1
            else:
                empty_line_count = 0

            # Filter out empty results and print issues
            issues = list(filter(None, issues))
            for issue in issues:
                print(f"Line {line_number}: {issue}")


if __name__ == "__main__":
    file_path = input("Enter the path to the Python file: ").strip()
    check_python_style(file_path)
