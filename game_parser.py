import math
import string
import difflib
import locations
import items
import characters

# 4. **parser.py**: Interprets user input and translates it into game actions.

stop_words = [
    "a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", 
    "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been", 
    "before", "being", "below", "between", "both", "but", "by", "can", "couldn", 
    "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", 
    "doing", "don", "don't", "down", "during", "each", "few", "for", "from", 
    "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", 
    "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", 
    "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its", 
    "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", 
    "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", 
    "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", 
    "over", "own", "re", "s", "same", "shan", "shan't", "she", "should", "should've", 
    "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", 
    "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", 
    "those", "through", "to", "towards", "toward", "too", "under", "until", "up", "ve", "very", "was", "wasn", 
    "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "whilst",
    "who", "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", 
    "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "region", "district", 
    "land", "mainland"
]

command_variations = {
    "go": ["go", "move", "head", "travel", "went", "goes"],
    "take": ["take", "pickup", "grab", "acquire", "takes", "took", "taken"],
    "drop": ["drop", "put", "release", "leave", "dropped", "putting"],
    "use": ["use", "utilize", "apply", "employ", "used", "using"],
    "display": ["display", "show", "view", "see", "displaying", "showing"],
    "buy": ["buy", "purchase", "acquire", "procure", "bought", "buying"],
    "quit": ["QUIT", "QUITS", "end", "quits", "finish", "complete"]
}

# List of all key words within the game. 
all_game_words = [key for key in locations.locations.keys()] + [key for key in command_variations.keys()] + [item.name for item in items.Items.values()] + [key for key in characters.Enemies.keys()] + ["north", "northeast", "southeast", "south", "southwest", "west", "northwest", "out"] + ['library', 'castle', 'garden', 'marketplace'] + ["pathfinder"] + ['shop', 'stats', 'inventory', 'enemies', 'enemy', 'item']

# Function to normalize user_input i.e., format according to requirements.
def normalize_input(user_input):
    user_input = remove_punctuation(user_input)
    user_input = create_list(user_input.lower())
    user_input = filter_words(user_input, stop_words)
    user_input = normalize_commands(user_input)
    user_input = suggest_spelling_corrections(user_input)
    
    return user_input

# Function to suggest spelling corrections for user input.
def suggest_spelling_corrections(words):
    
    corrected_words = []
    # Concatenating indexes of words[1] + words[2] to prevent difflib errors. 
    if len(words) > 2 and len(words) < 4:
        if words[0] in ["take", "drop", "use", "display", "item", "go"]:
            words[1] += " " + words[2]
            for word in words:
                    suggested_word = suggest_word_correction(word)
                    corrected_words.append(suggested_word)
                    
    elif words[0] in ["use"] and len(words) > 4:
         words[1] += " " + words[2]
         words[3] += " " + words[4]
         for word in words:
                    suggested_word = suggest_word_correction(word)
                    corrected_words.append(suggested_word)
                    
    elif words[0] in ["display", "buy"] and len(words) >= 4:
         words[2] += " " + words[3]
         for word in words:
                    suggested_word = suggest_word_correction(word)
                    corrected_words.append(suggested_word)
    else:
        for word in words:
                suggested_word = suggest_word_correction(word)
                corrected_words.append(suggested_word)
                
    return corrected_words

# Function to suggest a spelling correction for a word.
def suggest_word_correction(word):
    closest_match = difflib.get_close_matches(word, all_game_words, cutoff=0.55)
    if closest_match:
        return closest_match[0]
    return word

# Function to normalize commands using command variations.
def normalize_commands(words):
    normalized_words = []
    for word in words:
        for canonical_command, variations in command_variations.items():
            if word in variations:
                normalized_words.append(canonical_command)
                break
        else:
            normalized_words.append(word)
    
    return normalized_words

# Function to remove punctuation marks from a string. 
def remove_punctuation(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

# Function to create list from user input. 
def create_list(text):
    text = text.strip()
    text = text.split()
    return text

# Function to filter stop words. 
def filter_words(words, stop_words):
    filtered_list = []
    for word in words:
        if not (word in stop_words):
            filtered_list.append(word)
    
    return filtered_list    




















#xy = normalize_input("BUY GALACTIC GUAVA")
#print(xy)

#TEST CASES
#USE ASTRAL BOW ON STELLAR SPHERE - PASS
#DISPLAY ITEM ASTRAL AXE - PASS
#BUY ITEM ASTRAL AXE - PASS