# Written by Gerrit Schoettler, 2018

f = open("ethan_finds_the_shortest_path_sample_input.txt", 'r')
output = open("TEST_ethan_finds_the_shortest_path_sample_output.txt", 'w')
input = f.readline
ans = 1
for cnum in range(1, int(input()) + 1):
    N, K = input().strip().split()
    N = int(N)
    K = int(K)

    print(N, K)
    diff = 0

    if K >= 3 and N >= 3:
        if K <= N:
            diff = (K-1)*K/2 - K
        elif K > N:
            KminN = K - N + 1
            diff = (K - 1) * K / 2 - K - (KminN - 1) * KminN / 2

    elif N == 2:
        diff = 0
    elif K == 2:
        diff = 0
    elif K == 1:
        diff = 0

    ans = diff
    print("Case #%d: %d" % (cnum, ans))
    print("Case #%d: %d" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
