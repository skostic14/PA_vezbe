import time

def LCS(S, n, T, m):
        if (n < 0) | (m < 0):
            return 0
        if S[n] == T[m]:
            return 1 + LCS(S, n-1, T, m-1)
        return max(LCS(S, n-1, T, m), LCS(S, n, T, m-1))


def LCSLength(x, y):
    m = len(x)
    n = len(y)
    b = []
    c = []
    for i in range(m):
        c.append([])
        b.append([])

    for i in range(m):
        for j in range(n):
           c[i].append(0)
           b[i].append(0)

    for i in range(1, m):
        for j in range(n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j]="UL"
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] ="UP"
            else:
                c[i][j] = c[i][j-1]
                b[i][j]="LF"
    return(c, b)

def printLCS(b, X, i, j):
    if (i < 0) | (j < 0):
        return
    if b[i][j] == "UL":
        printLCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == "UP":
        printLCS(b, X, i-1, j)
    else:
        printLCS(b, X, i, j-1)

stra = "abcdefgxxhijkl"
strb = "bcdefghyyijklm"

start_time = time.time()
print("Najduzi podniz ima duzinu:", LCS(stra, len(stra)-1, strb, len(strb)-1))
print("Vreme izvrsavanja LCS:", time.time() - start_time)


rez = ()
start_time = time.time()
rez = LCSLength(stra, strb)
printLCS(rez[1], stra, len(stra)-1, len(strb)-2)
print("Vreme izvrsavanja LCSLength:", time.time() - start_time)