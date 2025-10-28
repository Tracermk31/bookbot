def get_word_count(filepath):
    text = get_book_text(filepath).split()
    count = 0
    for word in text:
        count += 1
    return count

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

def get_character_count(filepath):
    lower_text = get_book_text(filepath).lower().split()
    character_count = {}
    for word in lower_text:
        for character in word:
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1
    return character_count
    
def sort_dictionaries(dictionary):
    dictionary_list = []
    for key in dictionary:
        if key.isalpha() == True:
            count = dictionary[key]
            temp_dic = {"char": key, "num": count}
            dictionary_list.append(temp_dic)
    dictionary_list.sort(reverse= True, key=lambda item: item['num'])
    return dictionary_list

def print_report(filepath):
    num_words = get_word_count(filepath)
    character_count = get_character_count(filepath)
    sorted_dictionary_list = sort_dictionaries(character_count)
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {filepath}...\n"
    "----------- Word Count ----------\n"
    f"Found {num_words} total words\n"
    "--------- Character Count -------")
    for dictionary in sorted_dictionary_list:
        print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")
   