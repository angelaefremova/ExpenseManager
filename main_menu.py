import os

def main_menu():
    menu_layout = """
    —————————————————————————————
    |                           |
    | 1 - Categories            |
    |                           |
    | 2 - Expenses              |
    |                           |
    | 3 - Reports               |
    |                           |
    | 4 - Exit                  |
    |                           |
    —————————————————————————————
                                      """
    os.system('cls')
    print(menu_layout)

    menu_choice = input("Select from the menu: ")
    return menu_choice