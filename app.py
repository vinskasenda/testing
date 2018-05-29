# -*- coding: utf-8 -*-
import os
import sys
import platform
from xlpy import *

def main_menu():
    clear()
    print(
        "   .::AXIS - By VinsKasenda::." +
        "\nPlease choose the menu you want to start:"
        "\n[1] Purchase Package" + 
        "\n[2] Request OTP Code" +
        "\n[3] Request Password"  +
        "\n[0] Quit"
    )
    choice = str(input(" >> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    print(".::Purchase Package Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    po = str(input("Input your OTP >> "))
    serviceid = str(input("Input your Service ID >> "))
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    else:
        print("Login failed try again")
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    return
        
def menu_2():
    clear()
    print(".::OTP Code Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_3():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
