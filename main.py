def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        text = f.read()
        words = get_word_count(text)
        char_dict = get_char_dict(text)

    print(chars_dict_to_sorted_list(char_dict))


def get_char_dict(text):
    char_dict = {}
    for c in text.lower():
            if c not in char_dict:
                char_dict[c] = 0
            char_dict[c] += 1
    return char_dict

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["count"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({"char": c, "count": num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(file_path, words, characters):
    
    print(f"--- Begin report for {file_path} ---")
    print(f"{words} found in document")
    print("")

    for c in characters:
        if c.isalpha():
            print(f"Character '{c}' was found {characters[c]} times")

    print("--- End report ---")
    

main()