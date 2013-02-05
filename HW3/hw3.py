import random
import sys, time
from matplotlib import pyplot as plt

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
      average_time += (time.time() - start_time)/sims * 1000
  elif algorithm == 'comb':
    for i in range(0, sims):
      random.shuffle(unsorted)
      start_time = time.time()
      comb_sort(unsorted, sorted)
      average_time += (time.time() - start_time)/sims * 1000
  print "Ran %s simulations, averaging %.3f milliseconds per sort" %(sims, average_time) 
  return round(average_time, 10)
  
comb_averages = []
bubble_averages = []
n = range(2, 51, 5)
for i in n:
  comb_averages.append(simulate(i, 'comb', 1000))
  bubble_averages.append(simulate(i, 'bubble', 1000))
print comb_averages
print bubble_averages

plt.plot(n, bubble_averages, 'b--',  n, comb_averages, 'r--')
plt.scatter(n, bubble_averages, marker = '.', color = 'b', label = 'Bubble Sort', s=50, facecolors='none')
plt.scatter(n, comb_averages, marker = '.', color = 'r', label = 'Comb Sort', s=50, facecolors='none')
plt.xlabel('Number of values to be sorted')
plt.ylabel('Average sort time in milliseconds')
plt.xlim(0, 50)
plt.ylim(0, 0.5)
plt.legend(loc='upper center')
plt.savefig('hw3_bubble_vs_comb.png')
  
