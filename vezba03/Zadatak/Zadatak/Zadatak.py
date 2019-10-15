import math
import random
import time

def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)//2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        

def merge(A, p, q, r):
    
    L = []
    R = []
    
##    n1 = q - p + 1
##    n2 = r - q

  ##  for i in range(0, n1):
##        L.append(A[p+ i - 1])

 ##   for j in range(0, n2):
  ##      R.append(A[q + j])

    for i in range (p, q):
        L.append(A[i])

    for j in range (q, r):
        R.append(A[j])

    L.append(math.inf)
    R.append(math.inf)

    print(L)
    print(R)
   

    i = 0
    j = 0
    
    for k in range (p, r):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

def randomized_partition(A, p, r):
    i = int(random.choice(range(p,r)))

    A[i], A[r] = A[r], A[i]
    return quick_partition(A, p, r)

def quick_partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range (p, r):
        if A[j] <= x:
            i = i +1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1



def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

A = random_list(0, 10, 10)
B = A[:]

print(A)
start_time = time.time()
merge_sort(A,0,10)
merge_time = time.time() - start_time
print("Sorted array:", A)

start_time = time.time()
##randomized_quicksort(B, 0, 999)
quick_time = time.time() - start_time
#print("Sorted array:", B)
print("Merge sort time:", merge_time)
print("Quick sort time:", quick_time)