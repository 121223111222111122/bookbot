def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return (character_count)

# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method:
# Use a helper function to return the "num" key of each dictionary for comparison.
# Sort the list from greatest to least by the count.
def sort_on(item):
    return item["num"]

def sort_character_count(character_count):
    sorted_list = []
    for character, count in character_count.items():
        sorted_list.append({"char": character, "num": count})
    sorted_list.sort(key=sort_on,  reverse=True)
    return sorted_list
