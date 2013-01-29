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
 