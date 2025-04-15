import sys


def main():

    while True:
        # sys.stdout.write("$ ")
        # Wait for user input
        command = input("$ ")

        element = ("exit", "echo", "type")
        
        if "exit" == command[0:4]:
            break
        elif "echo" == command[0:4]:
            print(command[5:])
        elif "type" == command[0:4]:
            found = False
            for item in element:
                if item == command[5:]:
                    print(f"{item} is a shell builtin")
                    found = True
                    break
            if not found:        
                print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
