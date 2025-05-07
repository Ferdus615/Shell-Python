import sys
import shutil

def main():

    while True:
        # sys.stdout.write("$ ")
        # Wait for user input
        command = input("$ ")
        cmdprt = command.split()

        built_in_cmd = ("exit", "echo", "type")
        
        if "exit" == cmdprt[0]:
            break
        elif "echo" == cmdprt[0]:
            print(command[5:])
        elif "type" == cmdprt[0]:
            if cmdprt[1] in built_in_cmd:
                print(f"{cmdprt[1]} is a shell built in")
            elif path := shutil.which(cmdprt[1]):
                print(f"{cmdprt[1]} is {path}")
            else:
                print(f"{cmdprt[1]}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
