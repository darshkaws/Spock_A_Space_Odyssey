import math
import characters
import random

# 7. **items.py**: Defines game items and properties.

class Item:
    # Attributes/parameters for the class 'Item' are defined below. 
    def __init__(self, name, description, mass_kg, effects, is_disposable, is_special, value):
        self.name = name
        self.description = description
        self.mass_kg = mass_kg
        # Self.effects is a dictionary value; example = effects={"health": 20} -> adds 20 to health upon consumption.
        self.effects = effects
        self.is_disposable = is_disposable 
        self.is_special = is_special
        self.value = value
    
    # Call this function to apply effects of specified item to spaceship or other class with attributes. 
    def use(self, spaceship, pathfinder):
        for attribute, amount in self.effects.items():
            if hasattr(spaceship, ("current_" + attribute)):
                current_value = getattr(spaceship, ("current_" + attribute))
                maximum_value = getattr(spaceship, ("maximum_" + attribute))
                new_value = min(maximum_value, current_value + amount)
                setattr(spaceship, "current_" + attribute, new_value)
        if self.is_disposable:
            for index, itemx in enumerate(pathfinder.inventory):
                if self == itemx.name:
                    del pathfinder.inventory[index]
                
                
    # Call this function to use special items i.e., items which involve upgrading maximum_<attribute>.             
    def use_special(self, spaceship, pathfinder):
        for attribute, amount in self.effects.items():
            if hasattr(spaceship, ("maximum_" + attribute)):
                maximum_value = getattr(spaceship, ("maximum_" + attribute))
                new_value = maximum_value + amount
                setattr(spaceship, "current_" + attribute, new_value)
        if self.is_disposable:
            for index, itemx in enumerate(pathfinder.inventory):
                if self == itemx.name:
                    del pathfinder.inventory[index]

# Item objects defined below:

Cosmic_Scepter = Item("Cosmic Scepter", "Cosmic scepter inflicts serious damage to one's enemy", 3, {"health": -15}, False, False, 40)

Celestial_Shield = Item("Celestial Shield", "A shield made of celestial energy that protects from enemy attacks", 8, {"health": 20, }, False, False, 45)

Starlight_Sword = Item("Starlight Sword", "A sword made of starlight, deals significant damage to enemies", 5, {"health": -20}, False, False, 50)

Astral_Bow = Item("Astral Bow", "A bow that shoots arrows made of astral energy", 5, {"health": -10,}, False, False, 25)

Quantum_Quiver = Item("Quantum Quiver", "A quiver that never runs out of arrows when used with the Astral Bow", 2, {"health": 5}, True, False, 5)

Chronos_Clock = Item("Chronos Clock", "A clock that can manipulate time", 1, {"time": 5}, True, False, 75)

Elixir_of_Life = Item("Elixir Of Life", "A magical potion that can restore health", 0.5, {"health": 50}, True, False, 50)

Galactic_Grapes = Item("Galactic Grapes", "Grapes that can quench thirst and stave off hunger", 0.2, {"food": 10, "water": 10}, True, False, 20)

Nebula_Nuts = Item("Nebula Nuts", "Nuts that can stave off hunger", 0.2, {"food": 15}, True, False, 50)

Stellar_Steak = Item("Stellar Steak", "A steak that can stave off hunger", 1, {"food": 30}, True, False, 30)

Cosmic_Cloak = Item("Cosmic Cloak", "A cloak that can make the wearer invisible", 5, {"speed": 20}, False, False, 70)

Stellar_Staff = Item("Stellar Staff", "A staff that can be used to cast powerful spells", 7, {"health": -45}, False, False, 45)

Astral_Amulet = Item("Astral Amulet", "An amulet that can increase the wearer's power", 2, {"health": 25}, True, True, 25)

Chronos_Crystal = Item("Chronos Crystal", "A crystal that can manipulate time", 1, {"time": 7}, True, False, 100)

Elixir_of_Energy = Item("Elixir Of Energy", "A magical potion that can restore energy", 0.5, {"fuel": 50}, True, False, 75)

Galactic_Guava = Item("Galactic Guava", "A guava that can quench thirst and stave off hunger", 0.2, {"food": 15, "water": 15}, True, False, 30)

Nebula_Nectarine = Item("Nebula Nectarine", "A nectarine that can stave off hunger", 0.2, {"food": 20}, True, False, 20)

Stellar_Salmon = Item("Stellar Salmon", "A salmon that can stave off hunger", 1, {"food": 35}, True, False, 35)

Void_Vegetables = Item("Void Vegetables", "Vegetables that can stave off hunger", 0.5, {"food": 25}, True, False, 25)

Quantum_Quinoa = Item("Quantum Quinoa", "Quinoa that can stave off hunger", 0.5, {"food": 25}, True, False, 25)

Astral_Axe = Item("Astral Axe", "An axe made of astral energy, deals significant damage to enemies", 10, {"health": -50}, False, False, 75)

Galactic_Glaive = Item("Galactic Glaive", "A glaive made of galactic energy, deals significant damage to enemies", 12, {"health": -75}, False, False, 100)

Stellar_Scythe = Item("Stellar Scythe", "A scythe made of starlight, deals significant damage to enemies", 12, {"health": -100}, False, False, 150)

Void_Slicer = Item("Void Slicer", "A blade made of void energy, deals significant damage to enemies", 8, {"health": -150}, False, False, 250)

Elixir_of_Endurance = Item("Elixir Of Endurance", "A magical potion that can restore a large amount of health", 0.5, {"health": 500}, True, False, 250)

Galactic_Ginseng = Item("Galactic Ginseng", "A ginseng that can restore a large amount of health", 0.2, {"health": 300}, True, False, 170)

Stellar_Salve = Item("Stellar Salve", "A salve that can restore a large amount of health", 0.1, {"health": 200}, True, False, 130)

Astral_Ambrosia = Item("Astral Ambrosia", "The food of the gods that can restore a large amount of health", 0.5, {"health": 1000}, True, False, 500)

Cosmic_Codex = Item("Cosmic Codex", "A codex that can increase the ship's maximum health", 5, {"health": 500}, True, True, 1000)

Stellar_Sphere = Item("Stellar Sphere", "A sphere that can increase the ship's maximum health", 10, {"health": 1000}, True, True, 2000)

Astral_Aegis = Item("Astral Aegis", "A shield that can increase the ship's maximum health", 10, {"health": 1500}, True, True, 2500)

Galactic_Graviton = Item("Galactic Graviton", "A graviton that can increase the ship's maximum health", 14, {"health": 2000}, True, True, 3000)

# Dictionary of all items. 
Items = {
    "Cosmic Scepter": Cosmic_Scepter,
    "Celestial Shield": Celestial_Shield,
    "Starlight Sword": Starlight_Sword,
    "Astral Bow": Astral_Bow,
    "Quantum Quiver": Quantum_Quiver,
    "Chronos Clock": Chronos_Clock,
    "Elixir Of Life": Elixir_of_Life,
    "Galactic Grapes": Galactic_Grapes,
    "Nebula Nuts": Nebula_Nuts,
    "Stellar Steak": Stellar_Steak,
    "Cosmic Cloak": Cosmic_Cloak,
    "Stellar Staff": Stellar_Staff,
    "Astral Amulet": Astral_Amulet,
    "Chronos Crystal": Chronos_Crystal,
    "Elixir Of Energy": Elixir_of_Energy,
    "Galactic Guava": Galactic_Guava,
    "Nebula Cectarine": Nebula_Nectarine,
    "Stellar Salmon": Stellar_Salmon,
    "Void Vegetables": Void_Vegetables,
    "Quantum Quinoa": Quantum_Quinoa,
    "Astral Axe": Astral_Axe,
    "Galactic Glaive": Galactic_Glaive,
    "Stellar Scythe": Stellar_Scythe,
    "Void Slicer": Void_Slicer,
    "Elixir Of Endurance": Elixir_of_Endurance,
    "Galactic Ginseng": Galactic_Ginseng,
    "Stellar Salve": Stellar_Salve,
    "Astral Ambrosia": Astral_Ambrosia,
    "Cosmic Codex": Cosmic_Codex,
    "Stellar Sphere": Stellar_Sphere,
    "Astral Aegis": Astral_Aegis,
    "Galactic Graviton": Galactic_Graviton
}
