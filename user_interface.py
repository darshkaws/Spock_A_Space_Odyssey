from game_engine import *
import characters
from story import *
from game_parser import normalize_input
import sys
from time import sleep
from game_data import *
from termcolor import colored
import pyfiglet 
from locations import locations


# 5. **user_interface.py**: Handles the user interface, including text display, menus, and prompts.

def typewriter_effect(text, color, attrs = None):
    for char in text:
        time.sleep(0.01)
        print(colored(char, color=color, attrs=attrs), end='', flush=True)
    print()

# Display's location
def display_location(location):
    result = colored(pyfiglet.figlet_format(location["name"].upper(), font="banner3-D"), color="magenta", attrs=['bold']) 
    print(result) 
    # print("\n" + colored(location["name"].upper(), color="red") + "\n")
    text_effect1 = (location["description"] + "\n")
    typewriter_effect(text_effect1, color='cyan', attrs=['bold'])
    
    if "lore" in location:
        print("")
        text_effect2 = (location["lore"] + "\n")
        typewriter_effect(text_effect2, color='magenta', attrs=['bold'])


# Function to print exit.
def print_exit(direction, leads_to):
    colored_direction = colored(direction.upper(), 'green')
    colored_leads_to = colored(leads_to, 'yellow')
    print(f"{colored('GO', attrs=['bold'])} {colored_direction} to {colored_leads_to}.")
    
# Function to print exit_leads_to using current_room exits. 
def exit_leads_to(exits, direction):
    return locations[exits[direction]]["name"]

# Function to print list of items. 
def list_of_items(items):
    
    length = len(items)
    x = 0
    item_list = ""


    while x < length:
        item_list += str(items[x].name)
        if x < (length - 1):
            item_list += ", "
        x += 1

    return item_list

# Adds to start and end of list of comma separated items.
def print_room_items(location):

    items = list_of_items(location["items"])
    if len(items) > 0: 
        text_effect = (f"The following items: {items} reside here.\n")
        for char in text_effect:
            sleep(0.01)
            print(char, end='', flush=True)

# Function to determine and store selected choice.
def select_choice(choices):
    choice_type = random.choice(["good", "bad", "neutral"])
    selected_choices = (choices[choice_type])
    return choice_type, selected_choices

# Function to print game menu. 
from termcolor import colored

def print_menu(exits, choices, room_items, inv_items):
    print(colored("\nYou can:", "cyan", attrs=['bold']))

    if choices != None:
        choice_type, selected_choices = select_choice(choices)

        for selected_choice in selected_choices:
            action = selected_choice["action"]
            if action == "GO":
                print(f"{colored('GO', attrs=['bold'])} {colored(selected_choice['location'].upper(), 'green')} to {colored(selected_choice['description'], 'yellow')}")
            elif action == "TAKE":
                print(f"{colored('TAKE', attrs=['bold'])} {colored(selected_choice['item'].name.upper(), 'cyan')} to {colored(selected_choice['description'], 'green')}")    
            elif action == "DROP":
                print(f"{colored('DROP', attrs=['bold'])} {colored(selected_choice['item'].name.upper(), 'cyan')} to {colored(selected_choice['description'], 'green')}")    
            elif action == "USE":
                if "defeat" or "attack" in selected_choice['description'].lower():
                    print(f"{colored('USE', attrs=['bold'])} {colored(selected_choice['item'].name.upper(), 'cyan')} ON {colored(selected_choice['enemy'].name.upper(), 'red')} to {colored(selected_choice['description'], 'magenta')}")
                else:
                    print(f"{colored('USE', attrs=['bold'])} {colored(selected_choice['item'].name.upper(), 'cyan')} to {colored(selected_choice['description'], 'green')}")

    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    
    for room_item in room_items:
        print(f"{colored('TAKE', attrs=['bold'])} {colored(room_item.name.upper(), 'magenta')} to take {colored(room_item.name, 'green')}.")
    
    for inventory_item in inv_items:
        print(f"{colored('DROP', attrs=['bold'])} {colored(inventory_item.name.upper(), 'cyan')} to drop your {colored(inventory_item.name, 'green')}.")
    
    for inventory_item in inv_items:
        print(f"{colored('USE', attrs=['bold'])} {colored(inventory_item.name.upper(), 'red')} or {colored('USE', attrs = ['bold'])} {colored(inventory_item.name.upper(), 'red')} on <ENEMY> to use your {colored(inventory_item.name, 'green')}.")

    print(colored(f"{colored('DISPLAY', attrs=['bold'])} SHOP or {colored('DISPLAY', attrs=['bold'])} STATS or {colored('DISPLAY', attrs=['bold'])} INVENTORY or {colored('DISPLAY', attrs=['bold'])} ENEMIES.", "magenta"))
    print(colored(f"{colored('BUY', attrs=['bold'])} ITEM <NAME> to buy an item from the shop.", "cyan"))
    print(colored(f"{colored('QUIT', attrs=['bold'])} to end your odyssey.\n", "red"))
    print(colored("Where shall your odyssey take you, intrepid explorer?", "yellow", attrs=['bold']))

def menu(exits, choices, room_items, inv_items, current_location):
    # Call function to display menu.
    if current_location["name"] in ['library', 'castle', 'garden', 'marketplace']:
        print_menu(exits, None, room_items, inv_items)
        
    else:
        print_menu(exits, choices, room_items, inv_items)

    # Read player's input.
    user_input = input("> ")
    if user_input == "":
        clear_screen()
        return ""
        
    # Normalize the input.
    normalized_user_input = normalize_input(user_input)
    clear_screen()
    return normalized_user_input
