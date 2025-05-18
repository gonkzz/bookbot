from stats import get_num_words, get_char_count, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


# opens a file and returns its contents as a string
def get_book_text(file_path):

    with open(file_path) as file:
        file_content = file.read()

    return file_content


def main():
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    char_list = sorted_dict(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for items in char_list:
        char = items["char"]
        value = items["value"]

        if char.isalpha():
            print(f"{char}: {value}")

    print("============= END ===============")


main()
