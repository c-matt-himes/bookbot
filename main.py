path = "" #define path as a string

def get_book_text(path):
    with open(path) as f:
        return f.read()
#takes a filepath and returns full contents of the book

def main():
    path = "./books/frankenstein.txt"
    print(get_book_text(path))
#enters filepath as string path, prints the full contents

main()

