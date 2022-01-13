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
def banner():
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

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Code
def main():
    clearcmd()
    banner()

main()
