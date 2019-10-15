import math
import random
import time

class Data:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return str("Key: " + str(self.key) + " Data: " + str(self.data))

def divisionMethod(key, space):
    return int(key % space)

def multiplicationMethod(key, space):
    return int(space * ((key * 0.6180339887) % 1))

def universalMethod(key, space, p):
    a = random.randrange(p)
    b = random.randrange(p)
    return int(((a*key+b)%p)%space)

def chainingHash(key, space):
    return divisionMethod(key, space)
    ##return multiplicationMethod(key,space)
    ##return universalMethod(key, space, int(space/2))

def chainedHashInsert(list, data):
    loc = chainingHash(data.key, len(list))
    list[loc].append(data)

def chainedHashSearch(list, key):
    loc = chainingHash(key, len(list))
    for i in range(len(list[loc])):
        if list[loc][i].key == key:
            return list[loc][i]

def chainedHashDelete(list, key):
    loc = chainingHash(key, len(list))
    for i in range(len(list[loc])):
        if list[loc][i].key == key:
            list[loc].pop(i)
            break

def linearProbing(key, space, i):
    return int((divisionMethod(key, space) + i)%space)

def quadraticProbing(key, space, i):
    return int((divisionMethod(key, space) + 5*i + 7*i*i)%space)

def doubleHashing(key, space, i):
    return int((divisionMethod(key, space) + multiplicationMethod(key, space) + i)%space)

def openHashing(key, space, i):
    ##return linearProbing(key, space, i)
    ##return quadraticProbing(key, space, i)
    return doubleHashing(key, space, i)

def hashInsert(list, data):
    i = 0
    while(i < len(list)):
        temp = openHashing(data.key, len(list), i)
        if list[temp] != None:
            i += 1
        else:
            list[temp] = data
            return i
    return -1

def hashSearch(list, key):
    i = 0
    while(i < len(list)):
        temp = openHashing(key, len(list), i)
        if list[temp].key == key:
            return list[temp]
        else:
            i += 1
    return None

def hashDelete(list, key):
    i = 0
    while(i < len(list)):
        temp = openHashing(key, len(list), i)
        if list[temp] == None:
            return False
        if list[temp].key == key:
            list[temp] = None
            return True
        else:
            i += 1
    return False

def listInit(length):
    list = []
    for i in range(length):
        list.append([])
    return list

def hashListInit(length):
    list = []
    for i in range(length):
        list.append(None)
    return list

def printHashList(list):
    for i in range (len(list)):
        temp = list[i]
        if temp!=None:
            print(temp)

def printList(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            temp = list[i][j]
            if temp!=None:
                print(temp)

list = []
list = listInit(100)

datas = []

for i in range(100):
    datas.append(Data(random.randrange(100), random.randrange(20)))
    

a = Data(16, 'a')
b = Data(6, 'b')
c = Data(10, 'c')
d = Data(7, 'd')

for i in range(100):
    chainedHashInsert(list, datas[i])



chainedHashInsert(list, a)
chainedHashInsert(list, b)
chainedHashInsert(list, c)
chainedHashInsert(list, d)

chainedHashDelete(list, 7)

hashList = []
hashList = hashListInit(10)

hashInsert(hashList, a)
hashInsert(hashList, b)
hashInsert(hashList, c)
hashInsert(hashList, d)

hashDelete(hashList, 6)
hashDelete(hashList, 8)

printList(list)
printHashList(hashList)