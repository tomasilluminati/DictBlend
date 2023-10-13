'''
-----------------------------------------
|| DICTBLEND V1.3                     ||
-----------------------------------------

by Tomás Illuminati

DEVELOPED IN PYTHON 3.11.0 64-bit
ENCODING: UTF-8
DATE: OCT 4, 2023

DictBlend is a Python script that provides various functions for social engineering and information gathering. 
It is designed to assist security professionals in assessing and improving security awareness. 
This toolkit includes features like generating permutations of words, conducting a social engineering questionnaire, 
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

                #################################
                ##########  DISCLAIMER ##########
                #################################

This program is provided as-is, with no warranties of any kind. The author and the code provider assume 
ZERO responsibility for any direct or indirect damages that may arise from the use of this program.

By using this program, you acknowledge and accept this disclaimer of liability.

Please ensure that you understand the code and its implications before using it. Always conduct 
thorough testing in a safe environment before implementing this code in a production setting.

'''


import os
import threading
import time
import itertools
from itertools import permutations

# Global Flag for wait_animation
stop_background_task = False



#############################################
################ <Functions> ################
#############################################

# Information and Disclaimer
def info_about():
    os_clear = os_id_clear()
    os.system(os_clear)
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

    print(colorize_text('''
  ____  _          _       _                              __   _     _       _     _ _ _ _         
 |  _ \(_)___  ___| | __ _(_)_ __ ___   ___ _ __    ___  / _| | |   (_) __ _| |__ (_) (_) |_ _   _ 
 | | | | / __|/ __| |/ _` | | '_ ` _ \ / _ \ '__|  / _ \| |_  | |   | |/ _` | '_ \| | | | __| | | |
 | |_| | \__ \ (__| | (_| | | | | | | |  __/ |    | (_) |  _| | |___| | (_| | |_) | | | | |_| |_| |
 |____/|_|___/\___|_|\__,_|_|_| |_| |_|\___|_|     \___/|_|   |_____|_|\__,_|_.__/|_|_|_|\__|\__, |
                                                                                             |___/ 

This program is provided as-is, with no warranties of any kind. The author and the code provider assume 
ZERO responsibility for any direct or indirect damages that may arise from the use of this program.

By using this program, you acknowledge and accept this disclaimer of liability.

Please ensure that you understand the code and its implications before using it. Always conduct 
thorough testing in a safe environment before implementing this code in a production setting.
''', "red"))
    
    print("\nPress ENTER to exit")
    try:
        input() 
    except KeyboardInterrupt:
        pass
    finally:
        main()
# Function that creates a second-plane wait animation.
def wait_animation():
    global stop_background_task
    frames = ["[!] Wait   / ","[!] Wait.  | ","[!] Wait.. \ ","[!] Wait...| "]
    print("\n")
    while not stop_background_task:
        for frame in frames:
            print("\r" + colorize_text(frame, "cyan"), end="")
            time.sleep(0.5)
#Function that removes long string from the list
def remove_long_strings(input_list, num):

    new_list = [string for string in input_list if len(string) <= num]
    return new_list
# Function that combine the words in a list
def word_combinations(lst):
    if len(lst) <= 1:
        return lst

    combinations = []
    for i, word in enumerate(lst):
        remaining_words = lst[:i] + lst[i+1:]
        sub_combinations = word_combinations(remaining_words)
        for sub_combination in sub_combinations:
            combinations.append(word + sub_combination)
    
    combinations += lst  # Add individual words to the combinations list
    return combinations
# Function for the output menu
def export(lst):
    os_clear = os_id_clear()
    os.system(os_clear)
    separator("cyan")
    banner()
    separator("cyan")
    separator("red")
    print(colorize_text("\n                          FILE OUTPUT", "yellow"))
    separator("red")
    file_name = str(input(colorize_text("\n[-] Insert the output file name (without extension): ", "yellow")))
    file_name = file_name + ".txt"
    export_file(lst, file_name)
    separator("red")
# Social Engineering Questionnaire
def questionnaire():

    info = list()

    print(colorize_text("\n[!] Please answer the following questionnaire (Place a [ - ] for non-response)", "cyan"))
    name = str(input(colorize_text("\n[-] Target Name: ", "cyan")))
    lastname = str(input(colorize_text("\n[-] Target Lastname: ", "cyan")))
    nickname = input(colorize_text("\n[-] Target Nickname: ", "cyan"))
    fathername = input(colorize_text("\n[-] Target Father Name: ", "cyan"))
    mothername = input(colorize_text("\n[-] Target Mother Name: ", "cyan"))
    pet_name = input(colorize_text("\n[-] Target Pet Name: ", "cyan"))
    child_name = input(colorize_text("\n[-] Target child name: ", "cyan"))
    id = input(colorize_text("\n[-] Target ID: ","cyan"))
    birthday = input(colorize_text("\n[-] Target Birthday (MMDDYYYY): ", "cyan"))
    other = input(colorize_text("\n[-] Other info separate by (,) without spaces: ", "cyan"))

    other = other.strip()
    other = other.split(",")

    

    info.append(name)
    info.append(lastname)
    info.append(fathername)
    info.append(mothername)
    info.append(nickname)
    info.append(pet_name)
    info.append(child_name)
    info.append(id)
    info.append(birthday)

    for data in other:
        info.append(data)

    info = delrep(info)

    try:
        info.remove("-")
    except:
        pass

    return info
# Function that manage the third app option
def ownWordlist():

    info = list()

    print(colorize_text("\n[!] Please insert info separate by (,) without spaces: ", "cyan"))
    data = input(colorize_text("\n>>> ", "cyan"))

    data = data.strip()
    data = data.split(",")


    for d in data:
        d.strip
        info.append(d)

    info = delrep(info)

    return info
# Function that generate the output file
def export_file(lst, file_name):
    if lst != None:
        try:
            with open(file_name, 'w') as file:
                for item in lst:
                    file.write(item + '\n')
            print(colorize_text(f'\n[!] File "{file_name}" has been created successfully.', "yellow"))
        except Exception as e:
            print(colorize_text(f'\n[!] Error creating the file: {str(e)}', "red"))      
# Function that generates all possible forms from a word
def all_possible_forms(input_string):

    perms = permutations(input_string)


    possible_forms = [''.join(p) for p in perms]

    return possible_forms
# Function that removes repetitions from a list.
def delrep(list__):
    new_list = list(dict.fromkeys(list__).keys())
    return new_list
# Function that manage errors in init_menu
def test_answer_init_menu(answer):
    os_clear = os_id_clear()
    os.system(os_clear)
    try:
        answer = int(answer)
        if answer!=1 and answer!=2 and answer!=3 and answer != 4 and answer != 5:
            os.system(os_clear)
            separator("cyan")
            banner()
            separator("cyan")
            separator("red")
            print(colorize_text("\n               [!] The Answer must be a 1, 2, 3 or 4", "red"))
            separator("red")
            return "error"
        else:
            return answer
    except:
        os.system(os_clear)
        separator("cyan")
        banner()
        separator("cyan")
        separator("red")
        print(colorize_text("\n                 [!] The Answer must be a number", "red"))
        separator("red")
        return "error"
# Function that restart the script
def restart():

    os_clear = os_id_clear()

    response = str(input(colorize_text("\n[!] DO YOU WANT TO RESTART? (y/n)\n\n>>> ", "yellow")))
    response = response.lower()
    if response == "n":
        print(colorize_text("\n[!] SCRIPT FINISHED\n", "cyan"))
    elif response == "y":
        main()
    else:
        os.system(os_clear)
        separator("cyan")
        banner()
        separator("cyan")
        separator("red")
        print(colorize_text("\n                [!] The Answer must be a (Y) or (N)", "red"))
        separator("red")
        restart()
# Function that make alphabet combinations
def generate_combinations_alphabet(minimum, maximum, char_list):
    combinations = []
    
    # Check if the minimum and maximum values are valid
    if minimum < 0 or maximum < 0 or minimum >= len(char_list) or maximum >= len(char_list):
        return combinations
    
    def generate_combinations_for_length(length):
        local_combinations = []
        for combination in itertools.product(char_list, repeat=length):
            local_combinations.append(''.join(combination))
        combinations.extend(local_combinations)
    
    threads = []
    for length in range(minimum, maximum + 1):
        thread = threading.Thread(target=generate_combinations_for_length, args=(length,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return combinations
# Function that manage the generate_combinations_alphabet
def alphabet_long():

    global stop_background_task
    error = True
    min = 0
    max = 0
    os_clear = os_id_clear()
    os.system(os_clear)
    separator("cyan")
    banner()
    separator("cyan")
    list__ = [1,2,3,4,5]
    while error == True:
        try:
            if min == 0 and max == 0:
                min = int(input(colorize_text("\n[-] Choose the minimum lenght (max 5): ", "yellow")))
                max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
                if min in list__ and max in list__:
                    error = False

            else:
                os.system(os_clear)
                separator("cyan")
                banner()
                separator("cyan")
                separator("red")
                print(colorize_text("\n         [!] The Answers must be a numbers between 1 and 5", "red"))
                separator("red")
                min = int(input(colorize_text("\n[-] Choose the minimum lenght (max 5): ", "yellow")))
                max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
                if min in list__ and max in list__:
                    error = False
            
        except ValueError:
            os.system(os_clear)
            separator("cyan")
            banner()
            separator("cyan")
            separator("red")
            print(colorize_text("\n                   [!] The Answer must be a number", "red"))
            separator("red")
            min = int(input(colorize_text("\n[-] Choose the minimum lenght (max 5): ", "yellow")))
            max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
            if min in list__ and max in list__:
                error = False

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    background_thread = threading.Thread(target=wait_animation)
    background_thread.start()
    lst = generate_combinations_alphabet(min,max,alphabet) 
    lst = delrep(lst)
    stop_background_task = True
    background_thread.join()
    stop_background_task = False 
    

    return lst
# Function for coloring the terminal output
def colorize_text(text, color):

    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'cyan': '\033[36m',
        'reset': '\033[0m'
    }
    
    if color in colors:
        return f"{colors[color]}{text}{colors['reset']}"
    else:
        return text
# Function that identifies the OS.
def os_id_clear():
    if os.name == "posix":
        return "clear"
    else:
        return "cls"
# Main Banner
def banner():
    banner = """

██████╗ ██╗ ██████╗████████╗██████╗ ██╗     ███████╗███╗   ██╗██████╗ 
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗
██║  ██║██║██║        ██║   ██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║
██║  ██║██║██║        ██║   ██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║
██████╔╝██║╚██████╗   ██║   ██████╔╝███████╗███████╗██║ ╚████║██████╔╝
╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                                         
        
                                 V1.3
       
                         BY TOMAS ILLUMINATI     

"""
    print(colorize_text(banner, "green"))
    print(colorize_text("   (This tool was created for educational and ethical use only.)   ", "red"))  
# Separator line that allow to change the color
def separator(color): 
    print(colorize_text("\n------------------------------------------------------------------------", color) )
# Menu for select the lenght for the strings
def long_menu():
    os_clear = os_id_clear()
    os.system(os_clear)
    separator("cyan")
    banner()
    separator("cyan")
    print(colorize_text("\n[!] Do you want to set a maximum length for each string in the dictionary?", "yellow"))
    print(colorize_text("\n[!] If you don't do this, the file could exceed 5GB or more", "yellow"))
    separator("cyan")
    print(colorize_text("\n[1] Yes", "yellow"))
    print(colorize_text("\n[2] No", "yellow"))
    answer = input(colorize_text("\n>>> ", "yellow"))
    return answer
# Main Menu
def init_menu():
    print(colorize_text("\n[1] One Word - All Ways", "yellow"))
    print(colorize_text("\n[2] Social Engineering Questionnaire", "yellow"))
    print(colorize_text("\n[3] Generator through strings", "yellow"))
    print(colorize_text("\n[4] Generate alphabet wordlist", "yellow"))
    print(colorize_text("\n[5] Info & About", "yellow"))
    answer = input(colorize_text("\n>>> ", "yellow"))
    return answer

# Main Function
def main():
    
    global stop_background_task
    os_clear = os_id_clear()
    os.system(os_clear)

    separator("cyan")
    banner()
    separator("cyan")

    answer = init_menu()
    answer = test_answer_init_menu(answer)
    
    while answer=="error":
        answer = init_menu()
        answer = test_answer_init_menu(answer)
    
    if answer == 1:
        os.system(os_clear)
        separator("cyan")
        banner()
        separator("cyan")
        wString = str(input(colorize_text("\n[-] Insert only one string: ", "cyan")))
        wString = wString.strip()
        wString = wString.split(" ")
        
        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()
        
        wString = all_possible_forms(wString[0])

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 


        export(wString)
        restart()


    elif answer == 2:
        os.system(os_clear)
        separator("cyan")
        banner()
        separator("cyan")
        wList = questionnaire()

        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()

        wList = word_combinations(wList)

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 

        answer2 = long_menu()
        answer2 = test_answer_init_menu(answer2)
        

        while answer2=="error":
            answer2 = long_menu()
            answer2 = test_answer_init_menu(answer)

        if answer2 == 1:
            os.system(os_clear)
            separator("cyan")
            banner()
            separator("cyan")
            num = int(input(colorize_text("\nSet the maximum char lenght: ", "cyan")))

            background_thread = threading.Thread(target=wait_animation)
            background_thread.start()

            wList = remove_long_strings(wList, num)

            stop_background_task = True
            background_thread.join()
            stop_background_task = False 
            export(wList)
            restart()       

            
        elif answer2 == 2:
            os.system(os_clear)
            separator("cyan")
            banner()
            separator("cyan")
            export(wList)
            restart()


    elif answer == 3:
        os.system(os_clear)
        separator("cyan")
        banner()
        separator("cyan")
        OList = ownWordlist()


        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()

        OList = word_combinations(OList)

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 
        
        export(OList)
        restart()
    

    elif answer == 4:
        aList = alphabet_long()
        export(aList)
        restart()

    elif answer == 5:
        info_about()



if __name__ == "__main__":
    main()