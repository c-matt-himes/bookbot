def word_cnt(book_text):
    wsplt = [] #defines wsplt as a list
    wsplt = book_text.split()
    return len(wsplt)
#takes string (full book text) and returns full contents of book

def char_cnt(book_text):
    l_book_text = ""
    char_cnt = {}
    l_book_text = book_text.lower()
    for c in l_book_text:
        char_cnt[c] = char_cnt.get(c, 0) + 1
    return char_cnt
#char_cnt lowers case of all letters and creates a dictionary with each letter and number of instances of that letter 
    
def mult_dict (ccnt):
    kccnt_list = []
    for c, num in ccnt.items():
        kccnt_list.append({"char": c, "num": num})
    def sort_on(ccnt):
        return ccnt["num"]
    kccnt_list.sort(reverse=True,key=sort_on)
    return kccnt_list
#mult_dict creates a list of single item dictionaries with each entry in the ccnt dictionary
#as it's own full dict with keys char and num
#It then sorts based on value from using "num" key
