import heapq
import random

mylist = list(random.sample(range(100), 10))
# Top_k
k = 3
largest = heapq.nlargest(k, mylist)
smallest = heapq.nsmallest(k, mylist)

print('original list is', mylist)
print('largest-'+ str(k)+' is ',largest)
print('smallest-'+ str(k)+ ' is ',smallest)


