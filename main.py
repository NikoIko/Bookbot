from collections import OrderedDict

def main():
    book_path = "books/frankenstein.txt"    
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_of_each_letter = get_string_num(book_text)
    dictionary_list = split_dictionary(num_of_each_letter)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for item in dictionary_list:
        print(f"The {item['character']} was found {item['value']} times")
    


def get_string_num(book):
    letter = {}
    lowercase_letter = ""
    for word in book:
        if word.isalpha():
            lowercase_letter = word.lower()
            letter[lowercase_letter] = letter.get(lowercase_letter, 0) + 1
    return letter


def split_dictionary(dictionary):
    dict_list = [] 
    for key, value in dictionary.items():
        dict_list.append({'character': key, 'value': value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def get_num_words(book):
    stringified_book = book.split()
    return len(stringified_book)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def sort_on(dict):
    return dict['value']
 
    
main()