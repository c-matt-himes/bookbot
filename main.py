path = "" #define path as a string
book_text = "" #define full book as a string
wcnt = 0 #sets wcnt to be an integer
wsplt = [] #defines wsplt as a list

def get_book_text(path):
    with open(path) as f:
        return f.read()
#takes a filepath and returns full contents of the book

def word_cnt(book_text):
    wsplt = book_text.split()
    return len(wsplt)
#takes string (full book text) and returns full contents of book

def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    wcnt = word_cnt(book_text)
    print(f"{wcnt} words found in the document")
#enters filepath as string path, gets full text, uses full text to get count, and prints message

main()

