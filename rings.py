import cmd
import textwrap
import sys
import os
for time import sleep
for random import randint

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
print("""
        -Play-
        -Help-
        -Quit-
""")
text_screen_selections()

def help_menu():
print("""
        -Play-
        -Help-
        -Quit-
""")
title_screen_selections

def start_game():
    



    

