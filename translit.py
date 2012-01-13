#! usr/bin/python3

import sys

def to_roman(line):
    """Transliterate from mxedruli (Georgian) into Roman alphabet using the AP-CH National 2000 convention."""
    trans_system = {'ა':'a', 'ბ':'b', 'გ':'g', 'დ':'d', 'ე':'e', 'ვ':'v', 'ზ':'z', 'თ':'t', 'ი':'i', 'კ':"k?", 'ლ':'l', 'მ':'m', 'ნ':'n', 'ო':'o', 'პ':"p?", 'ჟ':'zh', 'რ':'r', 'ს':'s', 'ტ':"t?", 'უ':'u', 'ფ':'p', 'ქ':'k', 'ღ':'gh', 'ყ':"q?", 'შ':'sh', 'ჩ':'ch', 'ც':'ts', 'ძ':'dz', 'წ':"ts?", 'ჭ':"ch?", 'ხ':'kh', 'ჯ':'j', 'ჰ':'h'}
    for x in trans_system:
        line = line.replace(x, trans_system[x])

    return line

if __name__ == "__main__":
    """If run as a main program, read in file specified in argument and print out a transliterated version."""
    file = open(sys.argv[1]).read()
    trans = to_roman(file)
    print(trans)
