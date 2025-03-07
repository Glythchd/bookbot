def get_num_words(text):
    return len(text.split())

def get_num_char(text):
    character = {}
    for char in text:
        if char.lower() in character:
            character[char.lower()] += 1
        else:
            character[char.lower()] = 1
    return(character)