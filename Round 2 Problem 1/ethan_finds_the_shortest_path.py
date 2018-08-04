# Written by Gerrit Schoettler, 2018

f = open("ethan_finds_the_shortest_path_sample_input.txt", 'r')
output = open("TEST_ethan_finds_the_shortest_path_sample_output.txt", 'w')
input = f.readline
ans = 1
for cnum in range(1, int(input()) + 1):
    N, K = input().strip().split()
    N = int(N)
    K = int(K)
    graph = []
    E = 0
    #print(N, K)
    diff = 0

    if K >= 3 and N >= 3:
        if K <= N:
            diff = (K-1)*K/2 - K

        elif K > N:
            KminN = K - N + 1
            diff = (K - 1) * K / 2 - K - (KminN - 1) * KminN / 2
        E = min(N, K)

    elif N == 2:
        diff = 0
        E = 1
        #graph = [1, 2, K]
    elif K == 2:
        diff = 0
        E = 1

    elif K == 1:
        diff = 0
        E = 1

    ans = diff
    print("Case #%d: %d" % (cnum, ans))
    print("Case #%d: %d" % (cnum, ans), file=output)

    print(E, file=output)

    if K >= 3 and N >= 3:
        Uj = 1
        Vj = N
        Wj = K
        line = [Uj, Vj, Wj]
        print(*line, sep=' ', file=output)
        for j in range(1, min(K, N)-1):
            Uj = j
            Vj = j + 1
            Wj = K - j
            line = [Uj, Vj, Wj]
            print(*line, sep=' ', file=output)

        Uj = min(K, N) - 1
        Vj = N
        Wj = K - min(K, N) + 1
        line = [Uj, Vj, Wj]
        print(*line, sep=' ', file=output)

    elif N == 2:
        Uj = 1
        Vj = N
        Wj = K
        line = [Uj, Vj, Wj]
        print(*line, sep=' ', file=output)

    elif K == 2:
        Uj = 1
        Vj = N
        Wj = K
        line = [Uj, Vj, Wj]
        print(*line, sep=' ', file=output)

    elif K == 1:
        Uj = 1
        Vj = N
        Wj = K
        line = [Uj, Vj, Wj]
        print(*line, sep=' ', file=output)



f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
