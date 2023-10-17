from modules.banners_and_style import *
from modules.main_functions import *


def init_menu():
    
    print(colorize_text("\n[0] One Word - All Ways", "yellow"))
    print(colorize_text("\n[1] Social Engineering Questionnaire", "yellow"))
    print(colorize_text("\n[2] Generator through strings", "yellow"))
    print(colorize_text("\n[3] Generate alphabet wordlist", "yellow"))
    print(colorize_text("\n[4] Info & About", "yellow"))
    print(colorize_text("\n[5] Exit", "yellow"))
    answer = input(colorize_text("\n>>> ", "yellow"))
    return answer

def long_menu():
    print(colorize_text("\n[!] Do you want to set a maximum length for each string in the dictionary?", "yellow"))
    print(colorize_text("\n[!] If you don't do this, the file could exceed 5GB or more", "yellow"))
    separator("cyan")
    print(colorize_text("\n[1] Yes", "yellow"))
    print(colorize_text("\n[2] No", "yellow"))
    answer = input(colorize_text("\n>>> ", "yellow"))
    return answer


def test_answer_init_menu(answer):
    clear_screen()
    try:
        answer = int(answer)
        if answer!=0 and answer!=1 and answer!=2 and answer!=3 and answer != 4 and answer != 5:
            init_banner()
            separator("cyan")
            separator("red")
            print(colorize_text("\n               [!] The Answer must be a 0, 1, 2, 3 or 4", "red"))
            separator("red")
            return 9
        else:
            return answer
    except:
        init_banner()
        separator("cyan")
        separator("red")
        print(colorize_text("\n                 [!] The Answer must be a number", "red"))
        separator("red")
        return 9
    

def restart_error():
    separator("red")
    print(colorize_text("\n                [!] The Answer must be a (Y) or (N)", "red"))
    separator("red")


def export():
    init_banner()
    separator("red")
    print(colorize_text("\n                          FILE OUTPUT", "yellow"))
    separator("red")
    file_name = str(input(colorize_text("\n[-] Insert the output file name (without extension): ", "yellow")))
    file_name = file_name + ".txt"
    return file_name


def alphabet_menu():

    error = True
    min = 0
    max = 0
    init_banner()
    list__ = [1,2,3,4,5]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while error == True:
        try:
            if min == 0 and max == 0:
                min = int(input(colorize_text("\n[-] Choose the minimum lenght (min 1 and max 5): ", "yellow")))
                max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
                if min in list__ and max in list__:
                    error = False

            else:
                init_banner()
                separator("red")
                print(colorize_text("\n         [!] The Answers must be a numbers between 1 and 5", "red"))
                separator("red")
                min = int(input(colorize_text("\n[-] Choose the minimum lenght (min 1 and max 5: ", "yellow")))
                max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
                if min in list__ and max in list__:
                    error = False
            
        except ValueError:
            init_banner()
            separator("red")
            print(colorize_text("\n                   [!] The Answer must be a number", "red"))
            separator("red")
            min = int(input(colorize_text("\n[-] Choose the minimum lenght (min 1 and max 5): ", "yellow")))
            max = int(input(colorize_text("\n[-] Choose the maximum lenght (max 5): ", "yellow")))
            if min in list__ and max in list__:
                error = False
    

    list_final = generate_combinations_alphabet(min,max,alphabet)
    return list_final

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


def long_menu_test():
    answer = long_menu()
    try:
        answer = int(answer)
        if answer == 1 or answer == 2:
            return answer
        else:
            init_banner()
            separator("red")
            print(colorize_text("\n                   [!] The Answer must be 1 or 2", "red"))
            separator("red")
            return long_menu_test()  
            
    except ValueError:  
        init_banner()
        separator("red")
        print(colorize_text("\n                   [!]The Answer must be a number", "red"))
        separator("red")
        return long_menu_test()  

            
def max_char_lenght():
    num = input(colorize_text("\nSet the maximum char lenght: ", "cyan"))
    try:
        num = int(num)
        return num
    except:
        init_banner()
        separator("red")
        print(colorize_text("\n                   [!] The Answer must be a number", "red"))
        separator("red")
        max_char_lenght()
