def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_letter_report(chars_dict)
    

def get_num_words(text):
    words = text.split()
    return print(f"This report contains {len(words)} words")


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def remove_numeric_string_keys(d):
    keys_to_remove = [key for key in d if not key.isalpha() or key == '']
    for key in keys_to_remove:
        del d[key]
    return d

def print_letter_report(chars):
    just_letters = remove_numeric_string_keys(chars)
    print("---The letter report---")
    for c in just_letters:
        print(f"The '{c}' charcter was found {just_letters[c]} times")
   
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
