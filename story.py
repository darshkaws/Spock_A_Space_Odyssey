# 10. **story.py**: Contains the game's storyline, dialogues, and branching paths.
import time
from ascii_art import clear_screen, colored
import math
import random
import pygame

def typewriter_effect1(text, color_list):
    for char in text:
        time.sleep(0.06)
        print(colored(char, color=random.choice(color_list), attrs=['bold']), end='', flush=True)
    print()


# Game Title: "Spock: A Space Odyssey"
game_title = "Spock: A Space Odyssey"

# Geographical divisions within the story.
geographical_divisions = {
    "Northern Land": "Azelas",
    "Northeastern Realm": "Zygar",
    "Eastern Enclave": "The Garden",
    "Southeastern Territory": "Eclipsis",
    "Southern Domain": "CLion",
    "Southwestern Dominion": "Gortrov",
    "Western Expanse": "Fffire",
    "Northwestern Province": "Vulcan",
    "Central Hub": "Courtyard",
}

# Background setting of the story.
background_setting = """
Before the birth of the universe, an indescribable cosmic entity known as "Azathoth" existed at the edge of the cosmos.
It is believed that His slumber gave rise to all things, including the powerful ancient deities and omnipotent outer gods.
He is a source of both awe and dread, for His awakening could lead to the obliteration of the universe as we know it.
To prevent this cataclysm, Azathoth was confined within a celestial body referred to as "Earth."
The denizens of Earth, through their epic narratives and harmonious compositions, have the power to lull Him back to a peaceful slumber.
"""



# Description of the mission. 
mission_description = """
In their quest to prevent Azathoth's resurgence, the denizens of Earth have constructed nine grandiose stages within these nine realms.
Their mission is to interpret nine epic tales that would appease Azathoth's dreams and keep Him in peaceful slumber.
"""

# Epic Tales within the story.
epic_tales = {
    "Hero vs. Dark Lord": "Dive into the world inspired by Homer's epic 'The Iliad,' where the hero Achilles, a warrior of unmatched skill and bravery, faces off against Hector, the formidable dark lord of Troy. \nTheir titanic conflict shakes the very foundations of the world, as they engage in epic battles, their actions echoing through the annals of history.",
    "Dragon Slayer": "In the tradition of Norse mythology's 'Beowulf,' you'll embark on a perilous journey alongside Sigurd, a courageous hero. He's on a quest to rid the land of the fearsome dragon, Fafnir, \nWhose presence casts a shadow of dread. The battle against this monstrous creature is a gripping saga of valor and the triumph of humanity over ancient evil.",
    "Prince and Princess": "This tale, rooted in Greek mythology's 'Persephone,' transports you to a world of gods, mortals, and epic love. Follow the enchanting Princess Andromeda as she challenges Prince Perseus with daring tasks. \nHis determination to win her heart leads to a story of devotion, bravery, and the power of love to conquer all obstacles.",
    "Aladdin and the Magic Lamp": "Drawn from the enchanting tales of 'One Thousand and One Nights,' Aladdin's journey takes you from poverty to royalty with the discovery of a magical lamp. \nAs Aladdin marries the king's daughter and becomes a prince, you'll witness a story filled with intrigue, wishes, and a rags-to-riches transformation that captures the imagination.",
    "Prince vs. Demon": "Adapted from the Indian epic 'Ramayana,' the story of Prince Rama unfolds as he embarks on a noble quest to rescue his beloved Sita from the clutches of the demon king Ravana. \nWitness the clash of epic forces, divine intervention, and the indomitable spirit of a prince on a mission to save his true love.",
    "The Hero's Return": "Inspired by Greek mythology's 'The Odyssey,' you'll join the hero Odysseus on an odyssey of epic proportions. As he journeys through the vast and treacherous seas, \nOvercoming mythical creatures and divine challenges, you'll experience a saga of adventure and perseverance. His triumphant return to Ithaca is a testament to the enduring power of homecoming and fidelity.",
    "Warrior vs. Demon": "Drawing from the Samharam epic, the story chronicles the relentless conflict between the valiant warrior Sindbad and the malevolent demon Gabaar, a central figure in Indian mythology. \nTheir epic battle takes place in a world where mysticism and valor collide, creating a tale of legendary proportions.",
    "White Snake's Tale": "Inspired by the Chinese traditional myth of 'Legend of the White Snake,' this narrative introduces you to the ethereal love between the White Snake spirit, Bai Suzhen, and the mortal Xu Xian. \nTheir romance is filled with magical battles, mystical adventures, and the enduring power of love that transcends the boundaries between worlds.",
    "Love and Miracles": "Based on Egyptian mythology's 'Isis and Osiris,' this story unveils the deep and enduring love between Prince Osiris and Princess Isis. Their love is tested by malevolent forces that seek to tear them apart. \nThe tale is a testament to the resilience of love, the power of sacrifice, and the miracles that can arise from unwavering devotion.",
    "The Cosmic Chronicles": "Embark on a journey through the boundless cosmos as you follow the adventures of an intrepid space explorer. Discover alien worlds, face unknown perils, and unlock the mysteries of the universe. \nYour path is filled with cosmic wonders, uncharted territories, and the quest for knowledge beyond the stars."
}

endings = {
    "good_ending": """
    Congratulations to you and the inhabitants of Earth for successfully interpreting these nine epics, preventing the resurgence of Azathoth, and restoring Earth to its former state. 
    Recognizing the paramount importance of these epic narratives, the outer gods have decided to return Earth to a medieval era and have sealed off the potential for technological development, ensuring that Earth continues to perform and sustains Azathoth's peaceful slumber. 
    The denizens of Earth thrive in this new era, living harmoniously and cherishing their responsibility as cosmic custodians.
    """,
    "neutral_ending": """
    While you and the inhabitants of Earth managed to interpret some of the epic tales, you fell short of fully preventing the resurgence of Azathoth. 
    As a result, Earth is returned to a medieval era, and its potential for technological development is sealed off. 
    The universe remains in a delicate balance, with the looming threat of Azathoth's awakening. 
    The denizens of Earth continue to strive to interpret the remaining epics and maintain the cosmic equilibrium.
    """,
    "bad_ending": """
    Despite your efforts, you and the inhabitants of Earth were unable to interpret the epic tales adequately. 
    Azathoth's resurgence is inevitable, and the universe faces a cataclysmic obliteration. 
    The denizens of Earth are left to witness the unfolding destruction as Azathoth awakens, consuming everything in its path. 
    The cosmos is forever altered by this catastrophic event, and the memory of Earth fades into cosmic history as a cautionary tale.
    """
}


def introduction():
    # Clear the screen.
    clear_screen()

    # Display the background setting with a typewriter effect.
    background_setting = """
    Before the birth of the universe, an indescribable cosmic entity known as "Azathoth" existed at the edge of the cosmos.
    It is believed that His slumber gave rise to all things, including the powerful ancient deities and omnipotent outer gods.
    He is a source of both awe and dread, for His awakening could lead to the obliteration of the universe as we know it.
    To prevent this cataclysm, Azathoth was confined within a celestial body referred to as "Earth."
    The denizens of Earth, through their epic narratives and harmonious compositions, have the power to lull Him back to a peaceful slumber.
    """
    color_list = ['magenta', 'cyan', 'blue']
    pygame.mixer.init()
    # Play a sound effect (replace with your own sound file)
    pygame.mixer.music.load("game_assets/game_sound_intro_1.mp3")
    pygame.mixer.music.play()
    typewriter_effect1(background_setting, color_list)
    clear_screen()
    # Display the main introductory narrative.
    pygame.mixer.music.load("game_assets/game_sound_intro_2.mp3")
    pygame.mixer.music.play()
    game_title = "Spock: A Space Odyssey"
    intro_text = f"""
    Welcome to "{game_title}!"

    In the vast cosmic expanse, where the stars themselves tell stories, you embark on a journey of epic proportions. 
    
    The universe stands on the brink of destiny, and you, Commander Spock, are its beacon of hope.

    A Cosmic Tale Unfolds!

    Deep in the heart of the cosmos, the legendary entity "Azathoth" slumbers, whose awakening could bring an end to all that exists. 
    
    To prevent this impending cataclysm, the denizens of Earth have devised a grand plan. They have built nine extraordinary realms, each housing an epic narrative of immense power.

    Your mission is to explore these realms, to delve into these timeless tales, and to harness their cosmic essence to lull Azathoth back into peaceful slumber.

    Journey through Nine Epic Realms:

    - Battle alongside Achilles in "Hero vs. Dark Lord."
    - Brave the shadows with Sigurd as a "Dragon Slayer."
    - Experience the enchanting love story of Andromeda and Perseus in "Prince and Princess."
    - Unleash the power of wishes in the legendary "Aladdin and the Magic Lamp."
    - Join Rama on a quest to save Sita in "Prince vs. Demon."
    - Follow Odysseus in "The Hero's Return" as he battles mythical creatures.
    - Witness the relentless conflict between Sindbad and the malevolent demon Gabaar in "Warrior vs. Demon."
    - Embrace the enduring love between Bai Suzhen and Xu Xian in "White Snake's Tale."
    - Uncover the miracles of love and sacrifice in "Love and Miracles."
    - Embark on a cosmic voyage in "The Cosmic Chronicles" to explore the mysteries of the universe.

    Choose Your Path:

    Your choices, bravery, and intelligence will shape the destiny of Earth. 
    
    Will you interpret these epic tales in a way that keeps Azathoth's slumber unbroken? Or will the universe face an inevitable cataclysm?

    The fate of the cosmos rests in your hands, Commander Spock. Your odyssey begins now.
    """
    typewriter_effect1(intro_text, color_list)
    time.sleep(10)
    clear_screen()

credits = {
    "game_credits": """
    Game Credits:
    
    Group Leader and Our Saint - Darsh Kanjani
    Game Mechanics - Morgan, Darsh
    Game Parser - Darsh
    Items - Hamood, Philip
    Locations - Morgan, Darsh, Andrien
    Story - Anurag, Morgan, Ziyi
    Testing and Debugging - Philip, Ziyi
    User Interface - Darsh
    Presentation - Darsh, Morgan, Hamood, Philip, Anurag, Andrien, Thejana, Ziyi
    
    THANK YOU for playing the game!
    """
}