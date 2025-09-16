from stats import get_num_words
from stats import get_char_count
from stats import arrange
import sys

def get_book_text(path_to_book):
    file_contents = ""
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book= get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words(book)
    print("--------- Character Count -------")
    resulting_dict = {}
    resulting_dict = get_char_count(book)
    list_of_dicts = arrange(resulting_dict)
    print("============= END ===============")

main()


# "import sys" enables argument handling in main() (sys.argv)
