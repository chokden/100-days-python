# Hogwarts new student enrollment :D

# ANSI Color codes
green = "\033[32m"
blue = "\033[34m"
default = "\033[0m"  # Resets the color back to normal.
red = "\033[31m"
yellow = "\033[33m"

print("Welcome to Hogwarts school of Magic 🧙🏻")
name = input("Your name Sire : ")
print(
    f""" Choose one of the following House :
         {red}1.Gryffindor
         {blue}2.Ravenclaw
         {yellow}3.Hufflepuff
         {green}4.Slytherin 
         {default} 
      """
)
house = input("Write which house you wish to join: ")
spells = input("What is your favorite spell 🪄 ")
rivals = input("Any name you wish to cast your spell on : ")

print("Crystal ball analyzing .\n.\n.\n.")

print(
    """ Good day {blue}{name}{default},\n {green}Welcome to the world of magic and wizardy!!{default}{yellow}
     My name is Gundor, the house Spirit.{default}""".format(
        name=name, yellow=yellow, blue=blue, green=green, default=default
    )
)


print(
    f"""{yellow}I see that you have chosen the house of {house}, Impressive I must say{default}.{house} is known for its outstanding
achievements in Quidditch. {red}You have quite the taste for powerful magic.\n
Your archnemesis {default}{rivals}{default} may not survice if you cast your spell {green} ~~~ >>> {spells}.
Becareful {name}, {blue}with Great {yellow}power comes {blue}Great responsibilities !!
        """
)


"""
Another way of color coding is with using class: Will come back later on this. 
Sample code :

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

print(fg.YELLOW, "Hello, World !!!, style.RESET_ALL")


print(
    "Good day {blue}{name}{default},\n {green}Welcome to the world of magic and wizardy!!{default}{yellow}My name is Gundor, the house Spirit.{default}".format(
        name=name, yellow=yellow, blue=blue, green=green, default=default
    )
)

Breaking the above line into two lines breaks the code, thus you need to use """ """

"""
