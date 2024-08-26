from colorama import Fore, Back, Style

def print_info(text:str):
    print(Fore.GREEN + "INFO" + Fore.WHITE + f":\t {text}")

def print_warning(text:str):
    print(Fore.YELLOW + "WARNING" + Fore.WHITE + f":\t {text}")

def print_error(text:str):
    print(Fore.RED + "ERROR" + Fore.WHITE + f":\t {text}")