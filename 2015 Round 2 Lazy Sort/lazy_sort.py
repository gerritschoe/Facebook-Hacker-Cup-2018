# Written by Gerrit Schoettler, 2018

#f = open("lazy_sort_sample_input.txt", 'r')
#output = open("lazy_sort_sample_submissionTest.txt", 'w')
f = open("lazy_sort.txt", 'r')
output = open("lazy_sort_submission.txt", 'w')
input = f.readline

for cnum in range(1, int(input()) + 1):
    n = int(input())
    aOriginal = input().strip().split()
    ans = 'no'
    answer = [1, 1]
    for side in range(2):
        b = []
        a = []
        a = aOriginal * 1
        b.append(int(a.pop(-side)))
        A = b[0]
        B = b[0]

        for i in range(n-1):
            #print('i = ', i,'a = ', a,'A = ', A, 'B = ', B)
            if int(a[0]) == A + 1:
                A = A +1
                a.pop(0)
            elif int(a[-1]) == A + 1:
                A = A+1
                a.pop(-1)
            elif int(a[0]) == B-1:
                B=B-1
                a.pop(0)
            elif int(a[-1])==B-1:
                B=B-1
                a.pop(-1)
            else:
                answer[side] = 0
                break
    if 1 in answer:
        ans = 'yes'

    print("Case #%d: %s" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
