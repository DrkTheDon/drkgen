#!/usr/bin/python3

#####################################################
## DarkGenerator (DrkGen)                          ##
## A useful tool to generate giftcards.            ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################


# Imports
import json
import time
import pyfade
import random
from colorama import Fore, Style, init
import os
import requests
import discord
from datetime import datetime
import subprocess
import sys

# Global Variables
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "drk#1337"

# Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def back():
    input(f"{Fore.YELLOW}Press enter to go back.")

def options():
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   V. 0.9 Alpha (January 13th 2022)
  ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
  ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
  ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
  ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║
  ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                        
                                                                          """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Generators
    [2] Coming soon

    [3] Settings
    [4] Quit
    
    
    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        generators()
    elif USER_OPTION == "2":
        pass
    elif USER_OPTION == "3":
        pass
    elif USER_OPTION == "4":
        clearcmd()
        quit()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        options()

def generators():
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red, """
   V. 0.9 Alpha (January 13th 2022)
  ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗
  ██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║
  ██║  ██║██████╔╝█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║
  ██║  ██║██╔══██╗██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║
  ██████╔╝██║  ██║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                        
                                                                          """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Amazon Giftcard Generator
    [2] Netflix Giftcard Generator
    [3] Roblox Giftcard Generator
    [4] Apple Giftcard Generator
    [5] Steam Giftcard Generator
    [6] Google Play Giftcard Generaotr
    [7] Spotfiy Giftcard Generator

    [8] Info
    [9] Go back
    
    
    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        amazon()
    elif USER_OPTION == "2":
        pass
    elif USER_OPTION == "3":
        pass
    elif USER_OPTION == "4":
        pass
    elif USER_OPTION == "5":
        pass
    elif USER_OPTION == "6":
        pass
    elif USER_OPTION == "7":
        pass
    elif USER_OPTION == "8":
        pass
    elif USER_OPTION == "9":
        clearcmd()
        options()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        generators()

def amazon():
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_red,"""
     DRK GEN (V.0.9)
     █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
    ███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                   
    """))
    print(f"""{Fore.LIGHTWHITE_EX}     [ Made by {Fore.YELLOW}drk#1337 {Fore.LIGHTWHITE_EX}]{Fore.GREEN} DRK GENERATOR PROJECT
  {Fore.LIGHTWHITE_EX}
  """)
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Setting Up...")
    time.sleep(1)
    print(f"\nAmazon Giftcard Format is: {Fore.YELLOW}XXXX-XXXXXX-XXXXX\n")
    howmany = input(f"{Fore.RED}{curtime} {Fore.BLUE}[?] How many tokens do you want to generate, THIS WILL REMOVE PREVIOUS GIFTCARDS: ")

    with open("./generated/amazon.txt", "w+") as file:
        for i in range(int(howmany)):
            firstrandom = ''.join(random.choice(CHARACTERS) for i in range(int(4)))
            secondrandom = ''.join(random.choice(CHARACTERS) for i in range(int(6)))
            thirdrandom = ''.join(random.choice(CHARACTERS) for i in range(int(5)))

            result = firstrandom + "-" + secondrandom + "-" + thirdrandom 
            file.write(result)
            file.write("\n")
    print(f"{Fore.RED}{curtime} {Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Generating..")
    time.sleep(1)
    file.close()
    print(f"{Fore.RED}{curtime} {Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Successfully generated {Fore.YELLOW}{howmany}{Fore.LIGHTWHITE_EX} Giftcards")
    back()
    generators()
     
# Main Code
def main():
    clearcmd()
    options()

main()
