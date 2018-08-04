# Written by Gerrit Schoettler, 2018

f = open("carnival_coins_sample_input.txt", 'r')
output = open("carnival_coins_sample_output.txt", 'w')
input = f.readline

for cnum in range(1, int(input()) + 1):
    N,K,p = input().strip().split()
    N = int(N)
    K = float(K)
    p = float(p)
    print(N,K,p)

    # Dynamic programming to compute the probability DP[i][j] of exactly j heads when i coins are flipped
    DP = [[0 for x in range(N+1)] for y in range(N+1)]
    DP[0][0] = 1
    for i in range(1, N+1):
        for j in range(0, i+1):
            DP[i][j] = DP[i - 1][j - 1] * p + DP[i - 1][j] * (1 - p)
    print(DP[N][N])

    # Dynamic programming to compute DP2[k], the maximum number of prioes that can be won after flipping a total of k coins
    DP2 = [0]*(N+1)
    print((DP2))
    DP2[0] = 0
    for k in range(1, N+1):
        maxOF = []

        for x in range(int(k)):
            print(DP[k - x][:])
            maxOF[x] = DP2[x] + DP[k - x][:]
        DP2[k] = max(maxOF)

    print('DP2[0] = ', DP2[N])
    ans = DP2[N]
    print("Case #%d: %.9f" % (cnum, ans))
    print("Case #%d: %.9f" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
