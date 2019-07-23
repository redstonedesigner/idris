from colorama import init
init()
from colorama import Fore, Back, Style

def info(message):
    print(Fore.CYAN+"[INFO] "+Fore.RESET+message)

def success(message):
    print(Fore.GREEN+"[SUCCESS] "+Fore.RESET+message)

def warn(message):
    print(Fore.YELLOW+"[WARN] "+Fore.RESET+message)

def error(message):
    print(Fore.RED+"[ERROR] "+Fore.RESET+message)
