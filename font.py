import os
import pyfiglet
from termcolor import colored

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
NOCOLOR = "\033[0m"

# Fonts List (5 random fonts jo hum use karenge)
fonts = ["slant", "big", "block", "bubble", "starwars"]

# Loop taake tool band na ho
while True:
    os.system("clear")

    print(CYAN + "=========================================" + NOCOLOR)
    print(RED + "  YT-MURSLEEN VIP TOOL TEXT TO ASCII  " + NOCOLOR)
    print(YELLOW + "      👑 YT-MURSLEEN CHEATS 👑        " + NOCOLOR)
    print(CYAN + "=========================================" + NOCOLOR)

    # User se input lo
    text = input(GREEN + "Enter your text (or type 'exit' to quit): " + NOCOLOR).strip()

    # Exit Condition
    if text.lower() == "exit":
        print(YELLOW + "\nExiting... Thanks for using YT-MURSLEEN VIP TOOL!" + NOCOLOR)
        break

    # Check karo agar input khaali hai
    if not text:
        print(RED + "[ERROR] Text khali nahi hona chahiye!" + NOCOLOR)
        input("\nPress Enter to try again...")
        continue

    # Output ASCII Designs (Automatically 5 Designs)
    print("\n" + BLUE + "========= [ ASCII ART ] =========" + NOCOLOR)
    for font in fonts:
        print(PURPLE + f"\n[ {font.upper()} FONT ]" + NOCOLOR)
        ascii_art = pyfiglet.figlet_format(text, font=font)
        print(colored(ascii_art, "cyan"))

    input("\nPress Enter to convert another text...")