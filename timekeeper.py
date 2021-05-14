import os
import pathlib
import reports, printers
import clicmd as cmd
from datetime import date

def main():
    # Event handling function
    # Clear terminal, greet and await input from the user
    clear = lambda: os.system('cls')
    clear()

    print(printers.init_message)

    while True:
        print("")
        user_input = input("> ")
        print("")
        if user_input in cmd.available_commands:
            if user_input == "report":
                available_selections = ["today", "weekly", "monthly", "day"]

                while True:
                    print(printers.date_selection)
                    user_date_selection = input("> ")

                    if user_date_selection not in available_selections:
                        print("Incorrect option selected...")

                    elif user_date_selection == "day":
                        print(printers.specific_date)
                        while True:
                            try:
                                user_specific_date = input("> ")
                                cmd.available_commands[user_input](
                                    reports.read_report(
                                        json_data_file=f'{pathlib.Path(__file__).parent.absolute()}\\reports\\{user_specific_date}.json'
                                        )
                                    )
                            except FileNotFoundError:
                                print(f'File with the date "{user_specific_date}" does not exist...')
                                break

                    elif user_date_selection == "today":
                        try:
                            cmd.available_commands[user_input](
                                reports.read_report(
                                    json_data_file=f'{pathlib.Path(__file__).parent.absolute()}\\reports\\{str(date.today())}.json'
                                    )
                                )
                        except FileNotFoundError:
                            print("No such file exists...")
                        break

                    elif user_date_selection == "weekly":
                        print(printers.weekly_start_date)
                        while True:
                            user_start_date = input("> ")
                            cmd.available_commands[user_input](
                                reports.weekly_print(user_start_date)
                            )
                            break
                    break

            else:
                cmd.available_commands[user_input]()
        else:
            print("Unknown Command...")

if __name__ == '__main__':
    main()
