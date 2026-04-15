from colorama import Fore, init
init(autoreset=True)
def print_full_name():
    first_name = "Dharshini"
    last_name = "Kumar"
    full_name = first_name + " " + last_name

    return full_name

print(f"Hello, my name is: {Fore.CYAN}{print_full_name()}")