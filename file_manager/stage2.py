import os
import math

# Required to pass the Hyperskills test:
# os.chdir('module/root_folder')

def format_size(size):
    """Format the size into a human-readable format."""
    if size < 1024:
        return f"{size}B"
    elif size < 1024**2:
        return f"{math.ceil(size / 1024)}KB"
    elif size < 1024**3:
        return f"{math.ceil(size / 1024**2)}MB"
    else:
        return f"{math.ceil(size / 1024**3)}GB"

def list_directory(path, detail=False, human_readable=False):
    """List the contents of a directory, with directories first."""
    try:
        entries = os.listdir(path)
        dirs = [d for d in entries if os.path.isdir(os.path.join(path, d))]
        files = [f for f in entries if os.path.isfile(os.path.join(path, f))]

        for d in dirs:
            print(d)
        for f in files:
            if detail:
                size = os.stat(os.path.join(path, f)).st_size
                if human_readable:
                    size = format_size(size)
                print(f"{f} {size}")
            else:
                print(f)
    except OSError as e:
        print(f"Error: {e}")

def main():
    current_dir = os.getcwd()

    while True:
        command = input().strip()
        if command == "quit":
            break
        elif command == "pwd":
            print(current_dir)
        elif command.startswith("cd"):
            _, path = command.split(maxsplit=1)
            try:
                os.chdir(path)
                current_dir = os.getcwd()
                print(os.path.basename(current_dir))
            except OSError as e:
                print(f"Error: {e}")
        elif command == "ls":
            list_directory(current_dir)
        elif command == "ls -l":
            list_directory(current_dir, detail=True)
        elif command == "ls -lh":
            list_directory(current_dir, detail=True, human_readable=True)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
