import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
#get book
def get_books_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

# splits the string into words to count
def split(file_contents):
    return file_contents.split()

# main function - prints the number of book words
def main():
    from stats import get_num_words, count_letters, sort_letter_count
    text = get_books_text(book)
    words = split(text)
    word_count = get_num_words(words)
    letter_count = count_letters(text)
    #print(f"{word_count} words found in the document")
    #print(letter_count)
    sorted_list = sort_letter_count(letter_count)
    header = f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------"""
    print(header)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for report_data in sorted_list:
        if report_data["char"].isalpha():
            print(f"{report_data["char"]}: {report_data["num"]}")
    print("============= END ===============")




main()