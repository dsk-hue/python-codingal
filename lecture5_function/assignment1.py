from colorama import Fore, init
init(autoreset=True)
def triangle(base, height):
    return (base*height)/2
def rectangle(length, width):
    return length*width
def square(side):
    return side**2
def circle(radius):
    return 3.14*(radius**2)
keep_going=True
while keep_going:
    print(f"""To find the area of a {Fore.CYAN}triangle{Fore.GREEN}, enter {Fore.CYAN}1{Fore.GREEN}.
          To find the area of a {Fore.BLACK}rectangle{Fore.GREEN}, enter {Fore.BLACK}2{Fore.GREEN}.
          To find the area of a {Fore.RED}square{Fore.GREEN}, enter {Fore.RED}3{Fore.GREEN}.
          To find the area of a {Fore.LIGHTMAGENTA_EX}circle{Fore.GREEN}, enter {Fore.LIGHTMAGENTA_EX}4{Fore.GREEN}.""")
    break
keep_going=False
user_shape = int(input("Enter your number!"))
if user_shape not in [1, 2, 3, 4]:
    print("""Sorry, please pick a number from 1 to 4. 
          1 is a {Fore.CYAN}triangle{Fore.GREEN}, 
          2 is a {Fore.BLACK}rectangle{Fore.GREEN}, 
          3 is a {Fore.RED}square{Fore.GREEN},
          and 4 is a {Fore.LIGHTMAGENTA_EX}circle{Fore.GREEN}.""")
    keep_going=True
if int == 1:
    print("You have selected the {Fore.CYAN}triangle{Fore.GREEN}!")
    base = int(input("Enter the base of the triangle!"))
    height = int(input("Enter the height of the triangle!"))
    print(f"The area of the triangle is {triangle(base, height)}")