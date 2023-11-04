from user_interface import *
from ascii_art import *
from termcolor import colored
from story import *
from locations import *
from characters import *
import threading
from game_engine import execute_command, execute_go

# **main.py**: The game's entry point, responsible for initialization, the game loop, and control flow. 

# Create a shared threading.Event to signal when input is received.
input_received = threading.Event()

# Function to get user input with a timeout.
def input_with_timeout(prompt, timeout, countdown_timer):

    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)
        input_received.set()  # Set the event when input is received.
    
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    countdown_thread = threading.Thread(target=countdown_timer)
    countdown_thread.daemon = True
    countdown_thread.start()
    
    input_thread.join(timeout)
    countdown_thread.join()
    
    return user_input[0]

def countdown_timer():
    start_time2 = time.time() + 5
    remaining_time = start_time2 - time.time()
    while remaining_time >= 0 and not input_received.is_set():
        clear_screen()
        print(colored(f"Press Enter to skip the introduction, {remaining_time:.1f} seconds left.", color="green", attrs=['bold']))
        time.sleep(1)  # Wait for 1 second.
        remaining_time -= 1

def main():
    current_location = locations["Azeroth"]

    start_time = time.time()
    game_state = False

    # Display the introduction and allow the user to skip with Enter key.
    while not game_state:
        if time.time() - start_time <= 4:
            animator(filenames, delay=0.25, repeat=5)
        else:
            # Check for Enter key press to skip the introduction.
            user_input = input_with_timeout("", 5, countdown_timer)  # Allow 5 seconds to press Enter.
            if user_input == "":
                clear_screen()
                game_state = True
            else:
                # Continue with the introduction.
                introduction()
                start_time = time.time()

    while game_state:
        current_exits = current_location["exits"]
        if 'choices' in current_location:
            current_choices = current_location["choices"]
        else: 
            current_choices = None
        current_items = current_location["items"]
        display_location(current_location)
        user_command = menu(current_exits, current_choices, current_items, pathfinder.inventory, current_location)

        # Implementing execute_go in main.py to avoid circular import errors. 
        if user_command == "":
            continue
        elif len(user_command) >= 1:
            if user_command[0] == "go":
                start_time2 = time.time()
                journey_time = (2000/pathfinder.current_speed)
                if len(user_command) == 2:
                    if user_command[1] not in filler_locations:
                        current_location = locations[execute_go(user_command[1], current_exits, current_location)]
                        pathfinder.current_time += 1
                        pathfinder.is_alive = pathfinder.consume_resources(random.randint(1, 50), random.randint (1, 50), random.randint (1, 50))
                        if pathfinder.is_alive == False:
                            if pathfinder.current_health <= 0:
                                print(colored("You have died. ", color = 'red', attrs = 'bold'))
                                pathfinder.current_health += math.ceil(pathfinder.maximum_health / 2)
                    else:
                        current_location = current_location[execute_go(user_command[1], current_exits, current_location)]
                        pathfinder.current_time += 1
                        pathfinder.is_alive = pathfinder.consume_resources(random.randint(1, 50), random.randint (1, 50), random.randint (1, 50))
                        if pathfinder.is_alive == False:
                            if pathfinder.current_health <= 0:
                                print(colored("You have died. ", color = 'red', attrs = 'bold'))
                                pathfinder.current_health += math.ceil(pathfinder.maximum_health / 2)
                else:
                    print("GO where?")
                    # Calculate time spent in transition
                transition_time = time.time() - start_time2

                # Check if it's time to trigger the animation
                if transition_time <= journey_time:
                    animator(filenames, delay=0.25, repeat=int(journey_time/1.5))
        
        # Main game iteration is contingent uoon user_command variable, if user_input == "quit", loop ends. 
        game_state = execute_command(user_command, current_location)
        
        # Function to check if game_time == end_time, if game maximimum time is reached - ending is determined based on the player's points.
        def is_end():
            game_end_time = pathfinder.maximum_time
            if pathfinder.current_time == pathfinder.maximum_time:
                start_time1 = time.time()
                if time.time() - start_time1 <= 4:
                    animator(filenames, delay=0.25, repeat=5)
                max_points = game_end_time * 5
                good_ending = max_points / 3
                neutral_ending = max_points / 5
                color_list = ['magenta', 'cyan', 'blue']
                if pathfinder.total_points >= good_ending:
                    typewriter_effect1(endings['good_ending'], color_list)
                elif pathfinder.total_points >= neutral_ending:
                    typewriter_effect1(endings['neutral_ending'], color_list)
                else:
                    typewriter_effect1(endings['bad_ending'], color_list)
                time.sleep(1)
                clear_screen()
                typewriter_effect1(credits['game_credits'], color_list)
                time.sleep(1)
                print(colored(game_over, color = 'magenta', attrs = ['bold']))
                time.sleep(5)
                return False
            return True
        
        game_end_time = pathfinder.maximum_time
        if game_end_time == pathfinder.current_time:
            game_state = is_end()

if __name__ == "__main__":
    main()