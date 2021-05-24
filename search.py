from sr import recognize
from googlesearch import search

def firstLinkSerch(filename):
    return search(recognize(filename))[0]
