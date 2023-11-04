import math
import random
import time
from termcolor import colored
import ascii_art
from items import *

# 6. **characters.py**: Defines and manages characters in the game.

# Spaceship class to represent main character within storyline.
class Spaceship:
    # Attributes/parameters for the class 'Spaceship' are defined below. 
    def __init__(self, name, xp, maximum_health, maximum_fuel, maximum_speed, maximum_food, maximum_water, current_treasury, maximum_treasury, current_time, maximum_time, maximum_value, inventory=[]):
         self.name = name
         self.xp = xp
         self.level = self.xp_to_level()
         self.current_health = maximum_health
         self.maximum_health = maximum_health
         self.current_fuel = maximum_fuel
         self.maximum_fuel = maximum_fuel
         self.current_speed = maximum_speed
         self.maximum_speed = maximum_speed
         self.current_food = maximum_food
         self.maximum_food = maximum_food
         self.current_water = maximum_water
         self.maximum_water = maximum_water
         self.current_treasury = current_treasury
         self.maximum_treasury = maximum_treasury
         self.current_time = current_time
         self.maximum_time = maximum_time
         self.current_value = maximum_value
         self.maximum_value = maximum_value
         self.inventory = inventory
         self.carrying_mass = 0
         self.total_points = 0
    
    # Call this function to increase attribute value - can be triggered by items, events etc.
    """
    Example usage: <object_name>.increase_attribute("attribute (without prefix - i.e., without current_ or maximum_)", amount) - spaceship_1.increase_attribute("health", 20)
    """    
    def increase_attribute(self, attribute, amount):
        if hasattr(self, ("current_" + attribute)) and amount > 0:
            current_value = getattr(self, ("current_" + attribute))
            maximum_value = getattr(self, ("maximum_" + attribute))
            
            if maximum_value >= (current_value + amount):
                setattr(self, ("current_" + attribute), maximum_value)
            else:
                setattr(self, ("current_" + attribute), current_value + amount)
    
    # Call this function to consume resources periodically in accordance with spatial movement, if spaceship runs out of resources - function returns false -> can link to ship death. 
    """ 
    Example usage: <object_name>.consume_resources(rate_of_fuel_consumption, rate_of_food_consumption, rate_of_water_consumption) - spaceship_1.consume_resources(10, 20, 30)
    
    Suggestions:
    - Can also be used in conjunction with random.randint(range) functions to randomize resource consumption within a certain range. 
    """
    def consume_resources(self, fuel_consumption, food_consumption, water_consumption):
        if fuel_consumption <= self.current_fuel and food_consumption <= self.current_food and water_consumption <= self.current_water:
            self.current_fuel -= fuel_consumption
            self.current_food -= food_consumption
            self.current_water -= water_consumption
            return True
        elif fuel_consumption >= self.current_fuel:
            if self.current_health > fuel_consumption:
                self.current_health -= fuel_consumption
                return True
        elif food_consumption >= self.current_food:
            if self.current_health > food_consumption:
                self.current_health -= food_consumption
                return True
        elif water_consumption >= self.current_water:
            if self.current_health > water_consumption:
                self.current_health -= water_consumption
                return True
        else:
            return False

    # Function to attack the enemy
    def attack(self, enemy):
        randomTime = random.randint(0, 5)
        attackDamage = 25
        time.sleep(0.1)
        choice = input(colored("When the text appears, press enter to attack! (If you understand, press enter): ", color = 'red', attrs = ['bold']))
        if choice == "":
            time.sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n")
            time.sleep(randomTime)
        starttime = time.time()
        value = ("GO")
        print(colored("FIGHT", color = 'red', attrs = ['bold']))
        while value.lower() != "":
            value = input()
            attackTime = round((time.time() - starttime), 2)
            damage_multiplier_mapping = {
                # First integer is the time taken to press enter. second integer is the damage multiplier
                0.1: 4.0, 0.2: 3.7, 0.3: 3.4, 0.4: 3.1, 0.5: 2.8, 0.6: 2.5, 0.7: 2.2, 0.8: 1.9,
                0.9: 1.6, 1.0: 1.3, 1.1: 1.0, 1.2: 0.9, 1.3: 0.8, 1.4: 0.7, 1.5: 0.5,
            }
            if attackTime <= 0:
                # if they just spam the enter button, its cheating
                print("You cheated! You missed the attack")
            else:
                if attackTime > 1.5:
                    # should have penalty if they take to long to react
                    print("You took to long to react and missed your attack window")
                else:
                    for timel, multiplier in damage_multiplier_mapping.items():
                        if attackTime <= timel:
                            damageMultiplier = multiplier
                            # attackDamage is the final variable that will be used to decrease the enemy HP
                            attackDamage *= damageMultiplier
                            if enemy.current_health >= 0:
                                print(f"{colored('You attack and deal ' + str(attackDamage) + ' damage to the ' + enemy.name + '.', color = 'magenta', attrs = ['bold'])}")
                                enemy.take_damage(attackDamage)
                                break
                            else:
                                print(f"{colored(Enemy.name + ' is already dead.', color = 'yellow', attrs = ['bold'])}")
                                break

    # Function to subtract damage from health.
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
    
    # Function to determine if spaceship is still alive.
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    
    # Function to update time that has passed.
    def update_time(self, time_passed):
        self.current_time += time_passed 
    
    # Function to gain xp points.
    def increase_xp(self, xp_amount):
        if xp_amount > 0: 
            self.xp += xp_amount
    
    # Logarithmic function to calculate level. 
    def xp_to_level(self):
        base_xp = 100
        xp_factor = 1.1
        if self.xp < base_xp:
            return 1
        else:
            return (math.ceil(math.log(self.xp/base_xp, xp_factor)) + 1)
    
    # Function to spend xp. 
    def spend_xp(self, xp_amount):
        if xp_amount > 0 and self.xp >= xp_amount:
            self.xp -= xp_amount
            return True
        else:
            return False
    
    # Function to add item to inventory.
    def add_item(self, item):
        self.inventory.append(item)
    
    def use_item(self, item_index):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            # Call the use function of the Item class.
            item.use(self)
            if item.is_disposable == True:  
                del self.inventory[item_index]
            return f"You used {item.name}."
        else:
            return "Please enter a valid item index."

    # Function to determine impact of choices on attribute values. 
    def make_choice(self, choice):
        # Amend attribute values based on good choices within a random range.
        if choice == "good":
            self.increase_attribute("health", random.randint(5, 10))
            self.increase_attribute("fuel", random.randint(10, 20))
            self.increase_attribute("food", random.randint(10, 20))
            self.increase_attribute("water", random.randint(10, 20))
            self.increase_attribute("treasury", random.randint(5, 10))

            # Increase the total points counter for a good choice.
            self.xp += 100
            self.total_points += 5
            return "You made a good choice."

        elif choice == "neutral":
            # Amend attributes based on neutral choices within a random range.
            self.increase_attribute("health", random.randint(-5, -1))
            self.increase_attribute("fuel", random.randint(-10, -2))
            self.increase_attribute("food", random.randint(-10, -2))
            self.increase_attribute("water", random.randint(-10, -2))
            self.increase_attribute("treasury", random.randint(-5, -1))

            # No change in total points counter for a neutral choice.
            self.xp += 100
            return "You made a neutral choice."

        elif choice == "bad":
            # Amend attributes based on bad choices within a random range.
            self.increase_attribute("health", random.randint(-20, -10))
            self.increase_attribute("fuel", random.randint(-30, -15))
            self.increase_attribute("food", random.randint(-30, -15))
            self.increase_attribute("water", random.randint(-30, -15))
            self.increase_attribute("treasury", random.randint(-20, -10))

            # Decrease the total points counter for a bad choice.
            self.xp += 100
            self.total_points -= 5
            return "You made a bad choice."

        else:
            return "Invalid choice."


# Enemy class to represent adversaries within the storyline. 
class Enemy:
    def __init__(self, name, current_health, maximum_health, damage):
        self.name = name
        self.current_health = current_health
        self.maximum_health = maximum_health
        self.damage = damage
        self.current_fuel = 1
        self.maximum_fuel = 1
        self.current_speed = 1
        self.maximum_speed = 1
        self.current_food = 1
        self.maximum_food = 1
        self.current_water = 1
        self.maximum_water = 1
        self.current_treasury = random.randint(5, 100)
        self.maximum_treasury = 1
        self.current_time = 1
        self.maximum_time = 1

    def is_alive(self):
        if self.current_health > 0:
            return True
        return 

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        
    # Enemy attacks the protagonist and causes damage within random range.
    def attack(self, spaceship):
        if self.is_alive():
            enemyAttacks = random.randint(0, 12)

            if enemyAttacks == 0:
                # If random number is 0, they flee
                print(colored("Enemy tried to attack but tripped and died.", color = 'yellow', attrs = ['bold']))
                self.current_health = 0
            elif enemyAttacks in [1, 2, 3, 4, 5, 6, 7, 8]:
                # If random number is 1 to 6 they do a normal attack.
                damage = random.randint(1, self.damage)
                spaceship.take_damage(damage)
                print(f"{colored(self.name + ' attacks and deals ' + str(damage) + ' damage to your spaceship.', color = 'red', attrs = ['bold'])}")
            elif enemyAttacks == 9:
                max_health_percent = self.maximum_health * 0.1
                self.current_health += max_health_percent
                print(f"{colored(self.name + ' heals ' + str(max_health_percent) + ' health points.', color = 'cyan', attrs = ['bold'])}")
            elif enemyAttacks in [10, 11]:
                # If random number is 8 or 9 they miss their attack so make their attack damage 0
                print(colored("Enemy missed their attack.", color = 'green', attrs = ['bold']))
            else:
                # If random number is 12 they do a special attack which does more damage than normal attack, like double damage
                damage = self.damage
                damageMulti = 1.5
                damage *= damageMulti
                spaceship.take_damage(damage)
                print(f"{colored(self.name + ' does a special attack and deals ' + str(damage) + ' damage to your spaceship.', color = 'red', attrs = ['bold'])}")
            if spaceship.current_health <= 0:
                print(colored("You have died. ", color = 'red', attrs = 'bold'))
                spaceship.current_health += math.ceil(spaceship.maximum_health / 2)
                
# Enemy objects defined below:
#name, current health, maximum health, damage
Abyssal_Asteroid = Enemy("Abyssal Asteroid", 500, 500, 10) 

Cosmic_Calamity = Enemy("Cosmic Calamity", 1000, 1000, 20) 

Stellar_Serpent = Enemy("Stellar Serpent", 1500, 1500, 30) 

Galactic_Gorgon = Enemy("Galactic Gorgon", 2000, 2000, 40) 

Nebula_Nemesis = Enemy("Nebula Nemesis", 2500, 2500, 50) 

Astral_Abomination = Enemy("Astral Abomination", 3000, 3000, 60) 

Celestial_Centurion = Enemy("Celestial Centurion", 3500, 3500, 70) 

Starlight_Specter = Enemy("Starlight Specter", 4000, 4000, 80) 

Quantum_Quake = Enemy("Quantum Quake", 4500, 4500, 90) 

Void_Vortex = Enemy("Void Vortex", 5000, 5000, 100)

# Dictionary of all enemies. 
Enemies = {
    "Abyssal Asteroid": Abyssal_Asteroid,
    "Cosmic Calamity": Cosmic_Calamity,
    "Stellar Serpent": Stellar_Serpent,
    "Galactic Gorgon": Galactic_Gorgon,
    "Nebula Nemesis": Nebula_Nemesis,
    "Astral Abomination": Astral_Abomination,
    "Celestial Centurion": Celestial_Centurion,
    "Starlight Specter": Starlight_Specter,
    "Quantum Quake": Quantum_Quake,
    "Void Vortex": Void_Vortex
}

