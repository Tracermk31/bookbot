def read_book(file_path):
    with open(file_path, 'r') as text:
        book_string = text.read()
    return book_string

def count_words(book_string):
    words = book_string.split()
    word_count = len(words)
    return word_count

def count_character(book_string):
    character_count = {}
    lowercase_words = book_string.lower()
    for character in lowercase_words:
        count = character_count.get(character, 0)
        count += 1
        character_count[character] = count
    return character_count

def report(character_count, word_count, file_path):
    report_string = f" --- Begin report of {file_path} ---\n"
    report_string += f"{word_count} words found in document\n"

    character_list = [{"character": character, "count": count }
    for character, count in character_count.items()
        if character.isalpha()]

    character_list.sort(key=lambda x: x['count'], reverse=True)

    for character_dict in character_list:
        report_string += f"there are {character_dict['count']} repititions of {character_dict['character']} in this book\n"

    report_string += "This is the end of the Book Report\n"
    return report_string


def main():
    book = read_book("books/frankenstein.txt")
    word_count = count_words(book)
    character_count = count_character(book)
    book_report = report(character_count, word_count, "books/frankenstein.txt")
    print (book_report)

main()