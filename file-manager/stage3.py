import os
import math

# Required to pass the Hyperskills test:
os.chdir('module/root_folder')


def handle_path(current_dir, path):
    """Return the absolute path based on the current directory and the input path."""
    if os.path.isabs(path):
        return path
    else:
        return os.path.join(current_dir, path)
    

def remove(path):
    """Remove a file or directory."""
    if not os.path.exists(path):
        print("No such file or directory")
        return
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.rmdir(path)
    except OSError as e:
        print(f"Error: {e}")


def create(path, is_file=False):
    """Create a file or directory."""
    try:
        if is_file:
            open(path, "w").close()
        else:
            os.mkdir(path)
    except OSError:
        print("The directory already exists")


def rename(path, new_name):
    """Rename a file or directory."""
    if not os.path.exists(path):
        print("No such file or directory")
        return
    if os.path.exists(new_name):
        print("The file or directory already exists")
        return
    try:
        os.rename(path, new_name)
    except OSError as e:
        print(f"Error: {e}")


def change_dir(path):
    """Change the current working directory."""
    try:
        os.chdir(path)
        return os.getcwd()
    except OSError as e:
        print(f"Error: {e}")
        return None


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
        commands = input().strip().split()
        command = commands[0]

        if command == "quit":
            break
        elif command == "pwd":
            print(current_dir)
        elif command == "cd":
            if len(commands) != 2:
                print("Specify the directory")
            else:
                new_dir = change_dir(handle_path(current_dir, commands[1]))
                if new_dir is not None:
                    current_dir = new_dir
        elif command == "ls":
            if len(commands) == 1:
                list_directory(current_dir)
            elif len(commands) == 2:
                if commands[1] == "-l":
                    list_directory(current_dir, detail=True)
                elif commands[1] == "-lh":
                    list_directory(current_dir, detail=True, human_readable=True)
                else:
                    print("Invalid command")
        elif command == "mkdir":
            if len(commands) == 1:
                print("Specify the name of the directory to be made")
            else:
                for directory in commands[1:]:
                    create(handle_path(current_dir, directory))
        elif command == "rm":
            if len(commands) == 1:
                print("Specify the file or directory")
            else:
                for entry in commands[1:]:
                    remove(handle_path(current_dir, entry))
        elif command == "mv":
            if len(commands) != 3:
                print("Specify the current name of the file or directory and the new name")
            else:
                rename(handle_path(current_dir, commands[1]), handle_path(current_dir, commands[2]))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()