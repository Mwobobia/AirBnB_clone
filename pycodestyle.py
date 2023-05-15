import cmd
import sys


class AirbnbConsole(cmd.Cmd):
    intro = 'Welcome to the Airbnb Console! Type help or ? to list commands.\n'
    prompt = '(airbnb) '

    def do_exit(self, arg):
        'Exit Airbnb console.'
        print('Exiting Airbnb console...')
        sys.exit()

    def help_exit(self):
        'Print help for exit command.'
        print('exit - Exit the Airbnb console.')

    def do_list(self, arg):
        'List all Airbnb properties.'
        if arg:
            print(f'Listing properties for {arg}...')
        else:
            print('Listing all properties...')

    def help_list(self):
        'Print help for list command.'
        print('list - List all Airbnb properties.')
        print('Usage: list [city]')

    def default(self, arg):
        'Print an error message for invalid commands.'
        print(f'Invalid command: {arg}. Type help or ? to list commands.')


if __name__ == '__main__':
    AirbnbConsole().cmdloop()
