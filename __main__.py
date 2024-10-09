import sys
from CLI.main_menu import cli
from GUI.main_window import main_window

if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        match args[0]:
            case 'gui':
                main_window()
            case 'cli':
                cli()
            case _:
                print("Please enter a valid option")
                print("gui -> run the program graphically")
                print("cli -> run the program in the terminal")
                exit(1)
    else:
        main_window()