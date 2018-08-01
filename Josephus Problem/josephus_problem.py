# Written by Gerrit Schoettler, 2018

f = open("josephus_problem_input.txt", 'r')
output = open("josephus_problem_output.txt", 'w')
input = f.readline

for cnum in range(1, int(input()) + 1):
    p = int(input())
    b = "{0:b}".format(p)
    a = b[1:] + b[0]
    a = int(a, 2)
    print('Surviving seat in the %d seat josephus problem: %d' % (p,a))
    ans = a
    print("Case #%d: %s" % (cnum, ans), file=output)

f.close()
output.close()
print('Input file closed:', f.closed)
print('Output file closed:', output.closed)
