# This code passed the Hyperskills test, but it is incomplete.

import os

# run the user's program in our generated folders
os.chdir('module/root_folder')


# put your code here
commands = ["cd", "pwd", "quit"]


def main():
    current_dir = os.getcwd()
    print("Input the command")

    while True:

        command = input().split()

        if (command[0] not in commands) or (command[0] == "cd" and len(command) != 2):
            print("Invalid command")
            continue
        elif command[0] == "pwd" and len(command) == 1:
            print(current_dir)
            continue
        elif command[0] == "cd" and command[1] == "..":
            os.chdir('../')
            current_dir = os.getcwd()
            print(os.path.basename(current_dir))
            continue
        elif command[0] == "cd" and len(command[1]) > 2:
            if os.path.isabs(command[1]):
                # If command[1] is an absolute path, change the current working directory to it
                os.chdir(command[1])
            elif command[1] == "module":
                # print("SHIT")
                pass
            elif command[1] == "root_folder":
                # print("SHIT")
                pass
            else:
                # If command[1] is a relative path, join it with the current working directory
                filename = os.path.join(current_dir, command[1])
                os.chdir(filename)
            current_dir = os.getcwd()
            print(os.path.basename(current_dir))
            continue
        elif command[0] == "quit":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
