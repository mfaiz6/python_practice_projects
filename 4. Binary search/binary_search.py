# Implementation of binary search alogrithm

#naive search: scan entire list and ask if it's equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
   for i in range(len(l)):
      if l[i] == target:
         return i
   return -1


# binary search (divide and conquer)
# we will assume that our list is sorted
def binary_search(l, target, low=None, high=None):
    if low is None:
       low = 0
    if high is None:
       high = len(l) - 1

    if high < low:
       return -1

# example l = [1, 3, 5, 10, 12] # let's say we are searching for 10, then it should return 3, which is the index of 10
    midpoint = (low + high) // 2

    if l[midpoint] == target:
       return midpoint
    elif target < l[midpoint]:
       return binary_search(l, target, low. midpoint-1)
    else:
       target > l[midpoint]
       return binary_search(l, target, midpoint+1, high)
    
if __name__ == '__main__':
   l = [1, 3, 5, 10, 12]
   target = 10
   print(naive_search(l, target))
   print(binary_search(l, target))