# import _tkinter as tk
from operator import itemgetter
from collections import Counter

file = open("C:\\Users\\vnn92583\\Desktop\\wa.txt")
xlist = []

# def listgen(filename):
#     file = open(filename)
wordcount = Counter(file.read().split())
for item in wordcount:
    innerList = [item, wordcount[item]]
    # print innerList
    xlist.append(innerList)

xSorted = sorted(xlist, key=itemgetter(1), reverse=True)
for item in xSorted:
    # if item[0] == '"PM"':
        print item

    # print ("{}\t{}".format(*item))
    # xlist.append(item)
# print xlist.sort()
# if any("ok" in s for s in list):
# newList = xlist.sort(reverse=True)
# print newList