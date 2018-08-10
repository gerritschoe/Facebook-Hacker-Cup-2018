# Written by Gerrit Schoettler, 2018

f = open("jacks_candy_shop_sample_input.txt", 'r')
output = open("TESTjacks_candy_shop_sample_output.txt", 'w')
input = f.readline
ans = 1
for cnum in range(1, int(input()) + 1):
    N, M , A, B = input().strip().split()
    N = int(N)
    M = int(M)
    A = int(A)
    B = int(B)

    P = [0]*N
    for j in range(1, N):
        Rootj = input().strip()
        P[j] = int(Rootj)
    # list of subtrees
    Subtrees = []

    '''
    for k in range(N-1):
        D = k
        root = k
        Subs = P.index(root)
        print('Subs = ', Subs)
        #while root != None:

        #   root = find()
        Subtrees.append(D)
    '''
    C = [0]*M
    for i in range(M):
        D0 = (A*i+B)%N
        C[i] = D0
    print('C = ', C)

    # follow each node til root(0), add note to list of child if a parent is the Ci of a child
    Subtrees = [[] for y in range(N)]
    print('P = ', P)
    for i in range(N):
        rootPi = P[i]
        Subtrees[i].append(i)
        while rootPi != 0:
            #print('rootPi = ', rootPi)
            Subtrees[rootPi].append(i)
            rootPi = P[rootPi]
            '''
            if rootPi in C:

                index = C.index(rootPi)
                print('rootPi = ', rootPi, 'index in C = ', index, 'C = ', C)
                KidsSubtree[index].append(rootPi)
            '''

    for k in range(N):
        Subtrees[0].append(k)
    #Subtrees[0].append(0)
    print('Subtrees = ', Subtrees)
    # list all the subtrees for the kids
    KidsSubtrees = [[] for y in range(M)]
    for i in range(M):
        KidsSubtrees[i] = Subtrees[C[i]]
    print('KidsSubtrees = ', KidsSubtrees)
    #print('maxKidsSubtrees = ', max(KidsSubtrees[0]))
    lengths = []
    for i in range(M):
        lengths.append(len(KidsSubtrees[i]))
    #print('lengths = ', lengths)
    Sum = 0
    alreadyUsed = []
    for i in range(N):
        if i in lengths:
            indices = [j for j, x in enumerate(lengths) if x == i]
            #print('indices = ', indices)
            a = [KidsSubtrees[i] for i in indices]
            for j in range(len(a)-1):
                c = a[j]
                used = True
                while used == True:
                    print('c, j ', c, j)
                    b = max(c)
                    if b in alreadyUsed:
                        c.remove(b)
                    else:
                        alreadyUsed.append(b)
                        Sum = Sum + int(b)
                        used = False


    ans = Sum
    print("Case #%d: %d" % (cnum, ans))
    print("Case #%d: %d" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
