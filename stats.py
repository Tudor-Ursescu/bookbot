def get_num_words(contents):
    resulting_list = []
    resulting_list = contents.split()
    num_words = len(resulting_list)
    print(f"Found {num_words} total words")

def get_char_count(book_string):
    result = {}
    lower_book = book_string.lower()
    for i in range(0, len(lower_book)):
        if lower_book[i] not in result:
            result[lower_book[i]] = 1
        else:
            result[lower_book[i]] += 1
    return result

def sort_on(items):
    return items["num"];

def arrange(book_dict):
    list_of_dicts = []
    for item in book_dict:
        char = item
        num = book_dict[item]
        mini_dict = {}
        mini_dict["char"] = char
        mini_dict["num"] = num
        list_of_dicts.append(mini_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    for dict in list_of_dicts:
        character = dict["char"]
        number = dict["num"]
        if character.isalpha():
            print(f"{character}: {number}")

    