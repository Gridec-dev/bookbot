from stats import num_of_words, num_of_each_character,sort_dict
import sys

if len(sys.argv) < 2:
        sys.exit("Usage: python3 main.py <path_to_book>")

file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content

def main():

    
    content = get_book_text(file_path)
    words = num_of_words(content)
    letters = num_of_each_character(content)
    print(f"{words} words found in the document")

    sorted_letters = sort_dict(letters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()



