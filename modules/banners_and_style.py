from os import system, name as nm




def colorize_text(text, color, format=None):
    color = color.lower()
    if format != None:
        format = format.lower()

    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'new': '\033[1m',
        'reset': '\033[0m'
    }

    formats = {
        'bold': '\033[1m',
        'faint': '\033[2m',
        'italic': '\033[3m',
        'blink': '\033[5m',
    }

    if format != None:
        if color in colors:
            if format in formats:
                return f"{colors[color]}{formats[format]}{text}{colors['reset']}"
            else:
                return text
    elif format == None:
        if color in colors:
            return f"{colors[color]}{text}{colors['reset']}"
        else:
            return text
    else:
        return text
    
def os_id():
    if nm == "posix":
        return "clear"
    else:
        return "cls"

def clear_screen():
    system(os_id())


def init_banner():
    clear_screen()
    main_banner()
    separator("cyan")


def main_banner():
    banner = """

██████╗ ██╗ ██████╗████████╗██████╗ ██╗     ███████╗███╗   ██╗██████╗ 
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗
██║  ██║██║██║        ██║   ██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║
██║  ██║██║██║        ██║   ██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║
██████╔╝██║╚██████╗   ██║   ██████╔╝███████╗███████╗██║ ╚████║██████╔╝
╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                                         
        
                                 V2.0
       
                         BY TOMAS ILLUMINATI     

"""
    print(colorize_text(banner, "green"))
    print(colorize_text("   (This tool was created for educational and ethical use only.)   ", "red"))  

def I_and_A_banner():
    print(colorize_text('''
   ____     ___                    __       __             __ 
  /  _/__  / _/__    ___ ____  ___/ / ___ _/ /  ___  __ __/ /_
 _/ // _ \/ _/ _ \  / _ `/ _ \/ _  / / _ `/ _ \/ _ \/ // / __/
/___/_//_/_/ \___/  \_,_/_//_/\_,_/  \_,_/_.__/\___/\_,_/\__/ 
                                                            
''', "red"))
    
    print(colorize_text('''
DictBlend is a Python script that provides various functions for social engineering and dictionary creation. 
It is designed to assist security professionals in assessing and improving security awareness. 
This toolkit includes features like generating permutations of words, 
conducting a social engineering questionnaire, 
exporting results to a file, and generating an alphabet wordlist.

Usage:
- Run the script by executing the following command:
  Example: python3 dictBlend.py

- Select an option from the menu:
  1. One Word - All Ways: Generates all possible forms of a single word.
  2. Social Engineering Questionnaire: Conducts a questionnaire to gather information.
  3. Generator from own words: Generates combinations from user-provided words.
  4. Generate alphabet wordlist: Generates combinations of the alphabet.

- Follow the prompts and input the required information.

- For option 1, the script will generate and export all possible forms of the input word.
- For option 2, the script will conduct a questionnaire and export the collected data.
- For option 3, the script will generate combinations from user-provided words and export them.
- For option 4, the script will generate combinations of the alphabet.

Note:
- This toolkit is created for educational and ethical use only.
- It includes functions for word permutation, data collection, and file export.
- Output files are created in the current working directory.
- Input options are validated to prevent errors and guide the user.

''', "white"))

def separator(color): 
    print(colorize_text("\n------------------------------------------------------------------------", color) )

