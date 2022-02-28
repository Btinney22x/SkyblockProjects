# python C:\Users\btinn\OneDrive\Desktop\Projects\python\SkyblockCrafter.py

# pip install requests
# pip install colorama

# imports
import requests
import json

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# variables
COMMON = Fore.WHITE
UNCOMMON = Fore.GREEN + Style.BRIGHT
RARE = Fore.BLUE
EPIC = Fore.MAGENTA
LEGENDARY = Fore.YELLOW
MYTHIC = Fore.MAGENTA + Style.BRIGHT
DIVINE = Fore.CYAN + Style.BRIGHT
SPECIAL = Fore.RED + Style.BRIGHT
VERY_SPECIAL = Fore.RED + Style.BRIGHT


# code
def RarityCheck():
    print(COMMON + "Common")
    print(UNCOMMON + "Uncommon")
    print(RARE + "Rare")
    print(EPIC + "Epic")
    print(LEGENDARY + "Legendary")
    print(MYTHIC + "Mythic")
    print(DIVINE + "Divine")
    print(SPECIAL + "Special")
    print(VERY_SPECIAL + "Very Special")

RarityCheck()