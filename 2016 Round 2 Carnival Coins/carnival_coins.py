# Written by Gerrit Schoettler, 2018

f = open("carnival_coins_sample_input.txt", 'r')
output = open("carnival_coins_sample_output.txt", 'w')
input = f.readline

for cnum in range(1, int(input()) + 1):
    N,K,p = input().strip().split()
    N = int(N)
    K = float(K)
    p = float(p)
    #print(N,K,p)

    ans1 = N/K * p**K
    ans2 = N/2 * p**K

    ans = max(ans1,ans2)
    print("Case #%d: %.9f" % (cnum, ans))
    print("Case #%d: %.9f" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
