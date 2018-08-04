# Written by Gerrit Schoettler, 2018

f = open("boomerang_decoration.txt", 'r')
output = open("boomerang_decoration_output.txt", 'w')
input = f.readline

for cnum in range(1, int(input()) + 1):
    N = input().strip()
    A = input().strip()
    B = input().strip()
    print(N, A, B)
    #p = list(map(float, p))
    j = 1
    last = B[0]
    beginnings = [0]
    for i in range(int(N)):
        curr = B[i]
        if curr != last:
            j = j+1
            beginnings.append(i)
        last = curr
    print('j = ', j)
    print(beginnings)
    half1 = int(j/2)
    half2 = int(j/2)
    for i in range(half1):
        print('half1 = ', half1)
        print('half2 = ', half2)
        h1l = beginnings[half1]
        h1r = beginnings[half1+1]
        h2l = beginnings[half2]
        h2r = beginnings[half2+1]
        print('h1l:h1r', h1l, h1r)
        print('h2l:h2r', h2l, h2r)
        if A[h1l:h1r] == B[h1l:h1r] and A[h2l:h2r] == B[h2l:h2r]:
            half1 = half1 - 1
            half2 = half2 + 1
            #j = j - 1
            print('j = ', j)
        else:
            break
    print(half1, half2)
    ans = max(half1, j - half2)
    print("Case #%d: %d" % (cnum, ans))
    print("Case #%d: %d" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
