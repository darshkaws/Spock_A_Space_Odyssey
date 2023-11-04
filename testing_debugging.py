"""
Testing & Debugging, please enter any issues and log any changes here in comments. 
"""
"""
Bug #1: (Phil)
When menu is displayed from Zygar and Garden, displays "SOUTHEAST" as one word 
rather than as "SOUTH EAST", with every direction. This then requires the player
to type their input as one word, otherwise it is seen as invalid input
"""  #FIXED, Zygar and Garden's definitions of their directions had no spaces. 
#NOT A BUG_.
"""
Bug #2: (Phil)
when attempting to head west to Gortrov from CLion, no variation of west
is a valid input
""" #FIXED, In CLion's dictionary exits, "West" had a capital W when it shouldve been lowercase.
"""
Bug #3: (ziyi)
When a player inputs an item name like "STARLIGHT SWORD" into the game interface 
without preceding action verbs such as "take" or "drop", the game interface will 
reload. It won't display prompt messages like "What is your intention?" or "Please 
enter your next action."
""" #FIXED, the execute functions have now been implemented, letting the user to do these
"""
Bug #4:(ziyi)
When the player enters the game, the player's inventory is not displayed.
"""