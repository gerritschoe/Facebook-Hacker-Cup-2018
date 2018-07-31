f = open("let_it_flow_sample_input.txt",'r')
output=open("gerrit_submission.txt",'w')
input = f.readline

for cnum in range(1,int(input())+1):
    n = int(input())
    line1 = input().strip()
    line2 = input().strip()
    line3 = input().strip()
    if n%2==1 or line1[0]=='#' or line3[-1]=='#' or ('#' in line2):
        ans = 0
    else:
        ans = 1
        for i in range(1,n-1,2):
            t = 0
            if line1[i] == '.' and line1[i + 1] == '.': t += 1
            if line3[i] == '.' and line3[i + 1] == '.': t += 1
            ans = ans * t
    ans = ans % 1000000007
    print("Case #%d: %d"%(cnum,ans),file=output)

f.close()
print('Input file closed:',f.closed)
