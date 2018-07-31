import numpy as np
f = open("let_it_flow.txt",'r')
output=open("let_it_flow_gerrit_submission.txt",'w')
read_rows = f.readlines()
#print(read_rows[:])


T = int(read_rows[0])

for i in range(T):
    out = 1
    j = i * 4 + 1
    N = int(read_rows[j])

    if N % 2 == 1:
        out = 0 # if N is odd, there will not be a valid path
    else:
        # read middle row
        middle = read_rows[j+2]
        middleBlocked = '#' in middle
        if middleBlocked:
            out = 0 # if the middle is blocked, there will not be a valid path
        else:
            top = read_rows[j+1]
            bottom = read_rows[j+3]

            if '#' in top[0]:
                out = 0
            elif '#' in bottom[N-1]:
                out = 0
            else:
                for k in range(int((N-2)/2)):
                    idx = 2*k +1
                    #print('idx = ', idx, ' i = ', i)
                    top2 = top[idx:idx+2]
                    bot2 = bottom[idx:idx+2]
                    #print('top2 = ', top2)
                    if '#' in top2 and '#' in bot2:
                        out = 0
                    elif '#' in top2 or '#' in bot2:
                        out = out * 1
                    else:
                        out = out * 2
                #out = N
    out = out % 1000000007
    #print(f"Case #{i+1}: {out} {N}", end="\n",file=output)
    print(f"Case #{i+1}: {out}",file=output)
