path = "" #define path as a string
book_text = "" #define full book as a string
wcnt = 0 #sets wcnt to be an integer
ccnt = {}
kccnt = []

def get_book_text(path):
    with open(path) as f:
        return f.read()
#takes a filepath and returns full contents of the book

from stats import word_cnt
from stats import char_cnt
from stats import mult_dict


def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    wcnt = word_cnt(book_text)
    ccnt = char_cnt(book_text)
    ccnt = mult_dict(ccnt)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {wcnt} total words")
    print ("--------- Character Count -------")
    for c in ccnt:
        key = c["char"]
        if key.isalpha():
            print(f"{key}: {c['num']}")
        #for every one line dict in ccnt, checks to see if "char" value is a letter, 
        #then prints that "char" value (original key) and count
#enters filepath as string path, gets full text, uses full text to get count, breaks into individual dicts, and prints message

main()

