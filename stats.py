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

# Dictionary list of characters 
def srt_dict(character_dict):
    res_lst = []
    for character, count in character_dict.items():
        char_info = {"char": character, "count": count}
        res_lst.append(char_info)
    
    res_lst.sort(reverse=True, key=lambda char_info: char_info["count"])
    return res_lst