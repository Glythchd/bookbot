from stats import get_num_words, get_num_char

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(f"{num_words} words found in the document")
    print(num_char)

main()
