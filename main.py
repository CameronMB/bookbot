import sys
from stats import count_words, count_characters, sort_characters_by_count

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()

        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    
    book_contents = get_book_text(book_path)


    word_count = count_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_count = count_characters(book_contents)
    sorted_characters = sort_characters_by_count(char_count)
    
    print("--------- Character Count -------")
    for entry in sorted_characters:
        if entry['character'].isalpha():
            print(f"{entry['character']}: {entry['count']}")

    print("============= END ===============")

main()