import sys
from stats import get_num_words, get_num_char, srt_dict

if len(sys.argv) < 2:
     print('Usage: python3 main.py <path_to_book>')
     sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = get_num_char(text)
    sorted_chars = srt_dict(char_dict)
    
    # Print report according to the format in the assignment
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count if it's alphabetical
    for char_info in sorted_chars:
        char = char_info["char"]
        if char.isalpha():  # Only print alphabetical characters
            count = char_info["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()