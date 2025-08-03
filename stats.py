# file for statistics functions

def count_words(file_text):
    words = file_text.split() # split the text into words
    print(f"Found {len(words)} total words")

def count_characters(file_text):
    characters = {}
    for char in file_text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sorting(characters):
    char_list = []
    for char in characters:
        if char.isalpha():    
            char_list.append({"char": char, "num": characters[char]})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list