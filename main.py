def get_book_text(path_to_book):
    file_contents = ""
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def count_words(contents):
    resulting_list = []
    resulting_list = contents.split()
    num_words = len(resulting_list)
    print(f"{num_words} words found in the document")

def main():
    result = "" 
    result= get_book_text("./books/frankenstein.txt")
    count_words(result)


main()