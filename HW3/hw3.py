import random
import sys, time

def bubble_sort(unsorted, sorted):
  #print "Unsorted array: %r" % unsorted
  count = 1
  while unsorted != sorted:
    for i in range(0, len(unsorted)-1):
      if unsorted[i] > unsorted[i+1]: 
         unsorted.insert(i, unsorted[i+1])
         unsorted.pop(i+2)
    #print "Round %d: %r" % (count, unsorted)
    #if unsorted == sorted: print "Done!"
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
    #if unsorted == sorted: print "Done!"
        
def simulate(n, algorithm, sims):
  sorted = range(0, n)
  unsorted = range(0, n)
  average_time = 0
  if algorithm == 'bubble':
    for i in range(0, sims):
      random.shuffle(unsorted)
      start_time = time.time()
      bubble_sort(unsorted, sorted)
      average_time += (time.time() - start_time)/sims
  elif algorithm == 'comb':
    for i in range(0, sims):
      random.shuffle(unsorted)
      start_time = time.time()
      comb_sort(unsorted, sorted)
      average_time += (time.time() - start_time)/sims
  print "Ran %s simulations, averaging %.4f seconds per sort" %(sims, average_time) 
  return round(average_time, 4)
  
comb_averages = []
bubble_averages = []
for i in range(1, 15):
  comb_averages.append(simulate(2**i, 'comb', 1000))
  bubble_averages.appenD(simulate(2**i, 'bubble', 1000))
print comb_averages
print bubble_averages
  
