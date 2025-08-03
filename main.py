# file_path = input("Enter the path to the book file: ")
def get_book_text(file_path):
    with open(file_path) as f:
        file_text = f.read()
    return file_text
    
from stats import count_words, count_characters, sorting

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count_words(get_book_text(sys.argv[1]))
    number_of_char = count_characters(get_book_text(sys.argv[1]))
    # print(number_of_char)
    sorted_sequence = sorting(number_of_char)
    # print(sorted_sequence)
    for item in sorted_sequence: # print each character and its count
        print(f"{item['char']}: {item['num']}")
main()