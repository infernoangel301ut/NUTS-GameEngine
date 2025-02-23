import os

cmds:dict[str, str] = {
    "help": "Prints this message.",
    "exit": "Exits the program.",
    "generate": "Creates a project. Will be ran in the current terminal's directory.",
    "export": "Exports a project as an executable file. Will be ran in the current terminal's directory."
}

def generateProject(project_name:str) -> None:
    print(f"Checking for existing projects with name '{project_name}' in the current terminal's directory...")
    while os.path.exists(project_name):
        print(f"Project by name '{project_name}' was found, trying '{project_name + "-diff"}'")
        project_name += "-diff"

    print(f"Project by name '{project_name}' is available, creating...")
    os.mkdir(project_name)
    

print("Welcome to NUTS Game Engine manager!\nType \"help\" for a list of commands.\nType \"exit\" to exit the program.\n")

while True:
    command = input("What do you wish to do?: ")
    if command == "help":
        msg = ""
        for i, v in cmds.items(): msg += f"{i} -> {v}\n"
        print(msg)
    elif command == "exit": break
    elif command == "generate": pass
    elif command == "export": pass
    else: print("Unknown command.")

    print()

print("Exiting the program...")