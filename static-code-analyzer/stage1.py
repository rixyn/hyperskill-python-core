""" Hyperskill: Static Code Analyzer
Stage 1/5:  Search for long lines
Difficulty: Challenging
Track:      Python Core
Author:     Rixyn
Completed:  2024-02-29
"""


def check_line_length(file_path):
    """Check if any line in the file exceeds 79 characters."""
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if len(line) > 79:
                print(f"Line {line_number}: S001 Too long")


if __name__ == "__main__":
    file_path = input().strip()
    check_line_length(file_path)
