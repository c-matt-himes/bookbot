path = "" #define path as a string

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    print(get_book_text(path))

main()

