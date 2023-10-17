
from itertools import permutations, product
from modules.banners_and_style import colorize_text
from time import sleep


def remove_long_strings(input_list, num):

    new_list = [string for string in input_list if len(string) <= num]
    return new_list

def export_file(lst, file_name):
    if lst != None:
        try:
            with open(file_name, 'w') as file:
                for item in lst:
                    file.write(item + '\n')
            print(colorize_text(f'\n[!] File "{file_name}" has been created successfully.', "yellow"))
        except Exception as e:
            print(colorize_text(f'\n[!] Error creating the file: {str(e)}', "red"))      

def delrep(list__):
    new_list = list(dict.fromkeys(list__).keys())
    return new_list

def all_possible_forms(input_string):

    perms = permutations(input_string)
    possible_forms = [''.join(p) for p in perms]

    return possible_forms

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

def generate_combinations_alphabet(minimum, maximum, char_list):
    combinations = []
    
    # Check if the minimum and maximum values are valid
    if minimum < 0 or maximum < 0 or minimum >= len(char_list) or maximum >= len(char_list):
        return combinations
    
    for length in range(minimum, maximum + 1):
        for combination in product(char_list, repeat=length):
            combinations.append(''.join(combination))
    
    return combinations

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