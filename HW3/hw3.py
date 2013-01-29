import random
import sys, time

def bubble_sort(unsorted, sorted):
  print "Unsorted array: %r" % unsorted
  count = 1
  while unsorted != sorted:
    for i in range(0, len(unsorted)-1):
      if unsorted[i] > unsorted[i+1]: 
         unsorted.insert(i, unsorted[i+1])
         unsorted.pop(i+2)
    print "Round %d: %r" % (count, unsorted)
    count += 1
 
def comb_sort(unsorted, sorted):
  shrink = 1.3
  #print "Unsorted arrary: %r" % unsorted
  count = 1
  while unsorted != sorted:
    gap = int(len(unsorted)/shrink**count)
    if gap < 1: gap = 1
    for i in range(0, len(unsorted)-gap):
      if unsorted[i] > unsorted[i+gap]:
        unsorted.insert(i, unsorted[i+gap])
        unsorted.pop(i+gap+1)
        unsorted.insert(i+gap+1, unsorted[i+1])
        unsorted.pop(i+1)
    #print "Round %d (Gap = %d): %r" % (count, gap, unsorted)
    count += 1
    if unsorted == sorted: print "Done!"
    