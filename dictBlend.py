from modules.banners_and_style import *
from modules.main_functions import *
from modules.menus import *
import threading

stop_background_task = False

def wait_animation():
    global stop_background_task
    frames = ["[!] Wait   / ","[!] Wait.  | ","[!] Wait.. \ ","[!] Wait...| "]
    print("\n")
    while not stop_background_task:
        for frame in frames:
            print("\r" + colorize_text(frame, "cyan"), end="")
            sleep(0.5)


def restart(flag=0):

    if flag == 0:
        init_banner()
        response = str(input(colorize_text("\n[!] DO YOU WANT TO RESTART? (y/n)\n\n>>> ", "yellow")))
        response = response.lower()
        if response == "n":
            print(colorize_text("\n[!] SCRIPT FINISHED\n", "cyan"))
        elif response == "y":
            main()
        else:
            restart(flag=1)
    else:
        init_banner()
        restart_error()
        response = str(input(colorize_text("\n[!] DO YOU WANT TO RESTART? (y/n)\n\n>>> ", "yellow")))
        response = response.lower()
        if response == "n":
            print(colorize_text("\n[!] SCRIPT FINISHED\n", "cyan"))
        elif response == "y":
            main()
        else:
            restart(flag=1)
        

def main():
    init_banner()
    answer = init_menu()
    answer = test_answer_init_menu(answer)

    while answer!=0 and answer!=1 and answer!=2 and answer!=3 and answer!=4 and answer!=5:
        answer = init_menu()
        answer = test_answer_init_menu(answer)

    if answer == 0:
        init_banner()
        OneString = str(input(colorize_text("\n[-] Insert only one string: ", "cyan")))

        


        OneString = OneString.strip().split(" ")

        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()


        OneString = all_possible_forms(OneString[0])

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 

        filename = export()
        export_file(OneString,filename)
        restart()


    elif answer == 1:
        init_banner()
        info = questionnaire()
        
        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()

        info = word_combinations(info)

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 

        init_banner()
        longmenu = long_menu_test()

        while longmenu != 1 and longmenu != 2:
            init_banner()
            longmenu = long_menu_test()

        if longmenu == 1:
            init_banner()
            num = max_char_lenght()
            info = remove_long_strings(info,num)
        else:
            pass

        filename = export()
        export_file(info,filename)
        restart()


    elif answer == 2:
        init_banner()
        data = ownWordlist()

        background_thread = threading.Thread(target=wait_animation)
        background_thread.start()

        data = word_combinations(data)

        stop_background_task = True
        background_thread.join()
        stop_background_task = False 

        filename = export()
        export_file(data,filename)
        restart()



    elif answer == 3:
        init_banner()

        alphabet = alphabet_menu()

        filename = export()
        
        export_file(alphabet,filename)
        restart()


    elif answer == 4:
        I_and_A_banner()
        print("\nPress ENTER to Exit")
        input()
        main()
    elif answer == 5:
        exit()
        
        
    

if __name__ == "__main__":
    main()