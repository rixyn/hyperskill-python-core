print("Learning Progress Tracker")

while True:
    command = input().lower().strip()
    if command == "exit":
        print("Bye!")
        break
    elif command == "":
        print("No input")
        continue
    else:
        print("Unknown command!")
    