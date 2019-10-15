import math
import random
import time

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] < A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] < A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_maxheap(A, heap_size):
    for i in range(math.floor(len(A)/2), -1, -1):
        max_heapify(A, i, heap_size)

def heapsort(A, heap_size):
    build_maxheap(A, heap_size)
    for i in range(len(A)-1, 1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size -1
        max_heapify(A, 0, heap_size)

def bucketsort(A):
    B = []
    C = []
    n = len(A)
    for i in range(n):
        B.append([])
    for i in range(n):
        B[math.floor(n*A[i])].append(A[i])

    for i in range (n):
        B[i].sort()

        for j in range(len(B[i])):
            C.append(B[i][j])

    return C

def countingsort(A, B, k):
    C = []
    for i in range(k):
        C.append(0)

    for i in range(len(A)):
         C[A[i]-1]+= 1
    print(A)
    print(C)
    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(len(A)-1, 0, -1):
        B[C[A[i]-1]] = A[i]
        C[A[i]-1] -= 1

def random_dec_list(max):
    list = []
    for i in range(max):
        list.append(random.choice(range(max))/100)
    return list

def random_list(max):
    list = []
    for i in range(max):
        list.append(random.choice(range(max))+1)
    return list

A = random_list(15)
B = random_dec_list(20)
D = A[:]
E = []
heap_size = 15
print("Random list generated")
print(A)
heapsort(A, heap_size)
C = bucketsort(B)
print()
print()
print("Heapsorted list")
print(A)
print()
print()
print("Unsorted:", B)
print("Bucketsorted list")
print(C)
countingsort(D, E, max(D))
print()
print()
print("Countsorted list")
print(E)
