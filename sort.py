from collections import Counter

def openfile():
    return open(raw_input("Enter exact path of the file here: ")) #"/home/vineeth/Desktop/wa.txt"

def process_file():
    xlist = []
    file = openfile()
    wcount = Counter(file.read().split())
    for word in wcount.items():
              xlist.append(word)
    print xlist.sorted(reversed=True)

process_file()
