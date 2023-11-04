from items import *
import random
import math
from characters import *
from game_data import *
import story


# 8. **locations.py**: Represents game locations with descriptions and interactable objects.

# Import list of all items and enemies. 
all_items = list((Items.values()))
all_enemies = list((Enemies.values()))

# Function to generate random sample of random number of items.
def generate_random_items():
    return random.sample(all_items, random.randint(1, (int(len(all_items)/3))))

def generate_random_items2():
    return random.sample(all_items, random.randint(5, (int(len(all_items)/3))))
    
# Function to generate random sample of random number of enemies.    
def generate_random_enemies():
    return random.sample(all_enemies, random.randint(1, int((len(all_enemies)/2))))

def generate_choice(description, action, character_inventory, planet_inventory, enemy=None, location=None):
    location = location or random.choice(['library', 'castle', 'garden', 'marketplace'])
    
    if action == "TAKE":
        # Take the item from the planet's inventory.
        item = random.choice(planet_inventory)
    elif action in ["USE", "GIVE", "DROP"]:
        # Use, give, or drop an item from the character's inventory.
        if character_inventory:
            item = random.choice(character_inventory)
        else:
            # If the character doesn't have an item in their inventory, select a random one.
            item = random.choice(all_items)
    else:
        item = None

    if enemy is None:
        enemy = random.choice(all_enemies)
    
    # Create the item description string
    item_description = item.name if item is not None else "no item"

    return {"description": description.format(item=item_description, enemy=enemy.name, location=location), "action": action, "item": item, "enemy": enemy, "location": location}


    
# Planets, the choices and their locations examined:
planet_inventory = generate_random_items()

planet_azeroth = {
    "name": "Azeroth",
    "description": "Azeroth, the first planet of the Awakening, known for its ancient libraries. It's here that the epic of 'Hero vs. Dark Lord' is told.",
    "lore": story.epic_tales["Hero vs. Dark Lord"],
    "exits": {"north": "Landing Pad", "east": "Zygar", "south": "Forest-of-the-Dead", "west": "Vulcan"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Use the {item} to defeat the {enemy}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Give the {item} to the old scholar.", "DROP", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Steal the {item} from the library.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Use the {item} to attack the old scholar.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Study the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Take a tour of the {location}.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_Zygar = {
    "name": "Zygar",
    "description": "Zygar, the second planet of the Awakening, a land of brave warriors. The epic of 'Dragon Slayer' is told in this realm.",
    "lore": story.epic_tales["Dragon Slayer"],
    "exits": {"southeast": "Garden", "southwest": "Earth", "northwest": "Azeroth"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Defeat the {enemy} using the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Give the {item} to a wounded warrior for support.", "DROP", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Take the {item} from the armory without permission.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Attack a fellow warrior with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Study the {item} closely.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Go on a tour of the {location} to explore the culture of Zygar.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_Garden = {
    "name": "Garden",
    "description": "Garden, the third planet of the Awakening, a place of enchanting flora and ancient harmony rituals. The epic of 'Prince and Princess' is woven in this land.",
    "exits": {"southeast": "Eclipsis", "southwest": "Earth", "northwest": "Zygar"},
    "lore": story.epic_tales["Prince and Princess"],
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Defeat the {enemy} using the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Give the {item} to a botanist for support.", "DROP", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Take the {item} from the garden without permission.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Disturb the harmony with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Study the {item} closely.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Explore the unique flora of the {location}.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_eclipsis = {
    "name": "Eclipsis",
    "description": "Eclipsis, the fourth planet of the Awakening, a realm of cosmic mysteries. The epic of 'Love and Miracles' is etched into the fabric of this enigmatic land.",
    "lore": story.epic_tales["Love and Miracles"],
    "exits": {"northeast": "Garden", "southwest": "CLion", "northwest": "Earth"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Defeat the {enemy} using the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Solve cosmic riddles with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Take the {item} from the enigmatic vault without permission.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Unleash the power of the {item} in the heart of cosmic mysteries.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Study the {item} and its connection to cosmic enigmas.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Explore the cosmic wonders of Eclipsis.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_CLion = {
    "name": "CLion",
    "description": "CLion, the fifth planet of the Awakening, a land of intricate machinery and enigmatic technology. The epic of 'Aladdin and the Magic Lamp' unfolds in this realm.",
    "lore": story.epic_tales["Aladdin and the Magic Lamp"],
    "exits": {"north": "Earth", "southeast": "Eclipsis", "west": "Gortrov"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Discover the hidden powers of the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Navigate the labyrinthine machinery of CLion.", "GO", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Misuse the power of the {item} for personal gain.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Study the {item} and its mystical properties.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Grant a stranger's wish using the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Take the {item} from the secret chamber without permission.", "TAKE", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_gortrov = {
    "name": "Gortrov",
    "description": "Gortrov, the sixth planet of the Awakening, a realm of relentless fire and molten landscapes. The epic of 'Prince vs. Demon' takes place in this fiery domain.",
    "lore": story.epic_tales["Prince vs. Demon"],
    "exits": {"northeast": "Earth", "east": "CLion", "northwest": "Fffire"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Rescue a trapped soul using the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Face the trials of the fiery land with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Steal a valuable artifact using the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Unleash the destructive power of the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Explore the burning landscapes with the {item}.", "GO", pathfinder.inventory, planet_inventory),
            generate_choice("Study the {item} and its ancient powers.", "USE", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_fffire = {
    "name": "Fffire",
    "description": "Fffire, the seventh planet of the Awakening, a land consumed by eternal flames and burning desires. The epic of 'White Snake's Tale' unfolds in this fiery realm.",
    "lore": story.epic_tales["White Snake's Tale"],
    "exits": {"north": "Vulcan", "east": "Earth", "southeast": "Gortrov"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Aid the White Snake spirit using the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Safeguard a forbidden love with the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Steal a mystical artifact using the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Unleash the fiery power of the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Embark on a journey through the blazing landscape with the {item}.", "GO", pathfinder.inventory, planet_inventory),
            generate_choice("Investigate the {item} and its mystical qualities.", "USE", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_vulcan = {
    "name": "Vulcan",
    "description": "Vulcan, the eighth planet of the Awakening, a land of molten rivers and mighty forges. The epic of 'Warrior vs. Demon' unfolds in this fiery realm.",
    "lore": story.epic_tales["Prince vs. Demon"],
    "exits": {"northeast": "Azeroth", "southeast": "Forest-of-the-Dead", "south": "Fffire"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Defeat the {enemy} with the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Support a fellow warrior with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Take the {item} from the enemy's arsenal.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Betray a fellow warrior with the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Forge a new weapon with the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Explore the molten landscape of Vulcan with the {item}.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_fotd = {
    "name": "Forest-of-the-Dead",
    "description": "The ninth planet of the Awakening, a mysterious and eerie forest. The epic of 'White Snake's Tale' is woven in this dark realm.",
    "lore": story.epic_tales["White Snake's Tale"],
    "exits": {"north": "Azeroth", "northwest": "Vulcan"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Aid the lost souls with the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Defeat the {enemy} using the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Unleash the {item} on the forest's guardian spirit.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Take the {item} from the haunted grove.", "TAKE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Wander through the spectral forest with the {item}.", "GO", pathfinder.inventory, planet_inventory),
            generate_choice("Study the {item} closely.", "USE", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

planet_earth = {
    "name": "Earth",
    "description": "The final planet of the Awakening, the origin of all tales and the epicenter of Azathoth's presence.",
    "lore": story.epic_tales["The Cosmic Chronicles"],
    "exits": {"north": "Azeroth", "northeast": "Zygar", "east": "Garden", "southeast": "Eclipsis", "south": "CLion", "southwest": "Gortrov", "west": "Fffire", "northwest": "Vulcan"},
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "choices": {
        "good": [
            generate_choice("Help the denizens of Earth with the {item}.", "TAKE", pathfinder.inventory, planet_inventory),
            generate_choice("Defeat the cosmic enemies using the {item}.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "bad": [
            generate_choice("Use the {item} to disrupt the tales.", "GO", pathfinder.inventory, planet_inventory),
            generate_choice("Take the forbidden {item} from the core of Earth.", "USE", pathfinder.inventory, planet_inventory),
        ],
        "neutral": [
            generate_choice("Explore Earth with the {item}.", "USE", pathfinder.inventory, planet_inventory),
            generate_choice("Study the {item} closely.", "GO", pathfinder.inventory, planet_inventory),
        ],
    },
}

planet_inventory = generate_random_items()

landing_pad = {
    "name": "Landing Pad",
    "items": planet_inventory,
    "enemies": generate_random_enemies(),
    "description": "Landing Pad is a critical location on the planet Azeroth, where spacecraft and travelers from distant realms arrive. It serves as the primary gateway to Azeroth, a world filled with epic tales and challenges. This bustling hub is teeming with life, offering a vibrant and dynamic environment for adventurers. It is a place of arrival, departure, and endless possibilities, where the destiny of heroes unfolds.",
    "exits": {"south": "Azeroth"}
}

# Filler locations: 
locations = {
        "Azeroth": planet_azeroth,
        "Zygar": planet_Zygar,
        "Garden": planet_Garden,
        "Eclipsis": planet_eclipsis,
        "CLion": planet_CLion,
        "Gortrov": planet_gortrov,
        "Fffire": planet_fffire,
        "Vulcan": planet_vulcan,
        "Forest-of-the-Dead": planet_fotd,
        "Earth": planet_earth,
        "Landing Pad": landing_pad
    }

# Filler locations list. 
filler_locations = ['library', 'castle', 'garden', 'marketplace']

# Function to generate filler locations for each planet.
for planet in locations.values():
    for location in filler_locations:
        planet[location] = {
            "name": location.capitalize(),
            "description": f"This is the {location} of {planet['name']}.",
            "items": generate_random_items(),
            "enemies": generate_random_enemies(),
            "exits": {"out": planet['name']}
        }


# In-game shop/emporium (accessible at all times).
def generate_cosmic_emporium():
    
    emporium_items = generate_random_items2()

    # Create the Cosmic Emporium location.
    cosmic_emporium = {
        "name": "Cosmic Emporium",
        "description": "The bustling Cosmic Emporium of Azeroth is a hub for intergalactic trade. Various vendors offer exotic items from across the cosmos.",
        "items": emporium_items,
    }

    return cosmic_emporium

cosmic_emporium = generate_cosmic_emporium()