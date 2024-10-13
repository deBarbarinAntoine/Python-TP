from CLI import TP1_1, TP1_2, TP1_3, TP1_4
from Utils.Classes import MenuCLI, Colors


def cli():
    print('-' * 31)
    print(f"{Colors.BOLD}Welcome to Antoine's Python TP!{Colors.END}")
    print('-' * 31)
    menu = MenuCLI.new(
        'TP1.1 Temperature Converter', 'TP1.2 Sum and Product of Even Numbers', 'TP1.3 Welcome Message Generator', 'TP1.4 Mental Arithmetic',
        title='Main Menu'
    )
    match menu.run():
        case 0:
            print("Bye!")
            exit(0)
        case 1:
            TP1_1.cli()
        case 2:
            TP1_2.cli()
        case 3:
            TP1_3.cli()
        case 4:
            TP1_4.cli()