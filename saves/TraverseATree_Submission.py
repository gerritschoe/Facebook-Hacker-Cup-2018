f = open("ethan_traverses_a_tree_sample_input.txt",'r')
output=open("ethan_traverses_a_tree_sample_output_test.txt",'w')
read_rows = f.readlines()

def calPreTraversal(nodes, next):
    preTraversal = []
    if next != -1:
        #print('current = ', next + 1, 'childs = ', int(nodes[next].split()[0]), int(nodes[next].split()[1]))
        preTraversal.append(next + 1)

        nextLeft = int(nodes[next].split()[0]) - 1
        nextRight = int(nodes[next].split()[1]) - 1

        preTraversal = preTraversal + calPreTraversal(nodes, nextLeft)
        preTraversal = preTraversal + calPreTraversal(nodes, nextRight)
    return preTraversal
def calcPostTraversal(nodes, next):
    postTraVersal = []
    if next != -1:
        #print('current = ', next + 1, 'childs = ', int(nodes[next].split()[0]), int(nodes[next].split()[1]))
        nextLeft = int(nodes[next].split()[0]) - 1
        nextRight = int(nodes[next].split()[1]) - 1

        postTraVersal = calcPostTraversal(nodes, nextLeft)
        postTraVersal = postTraVersal + calcPostTraversal(nodes, nextRight)
        postTraVersal.append(next + 1)
    return postTraVersal

T = int(read_rows[0])
#print(T)
j = 1
for i in range(T):
    NK = read_rows[j] #list
    [N,K] = NK.split()
    N = int(N)
    K = int(K)

    nodes = read_rows[j+1:j+1+N]

    preTraFull = calPreTraversal(nodes, 0)
    #print('preTraFull = ', preTraFull)
    postTraFull = calcPostTraversal(nodes, 0)
    #print('postTraFull = ', postTraFull)
    alreadyGrouped = set()
    groupAssignments = [0] * N
    #groupAssignments = groupAssignments.astype(int)
    #toPrint = ' '.join(map(str, groupAssignments))
    #print(f" Print Test: {toPrint}")
    label = 1
    Groups = []
    for k in range(N):
        if preTraFull[k] not in alreadyGrouped:
            v = k
            newGroup = []
            groupNotDone = True
            while groupNotDone:
                newGroup.append([preTraFull[v]])
                alreadyGrouped.add(preTraFull[v])
                v = preTraFull.index(postTraFull[v])
                if v == k:
                    groupNotDone = False
            Groups.append(newGroup)

    #print("Groups = ",Groups)
    if len(Groups) < K:
        out = "Impossible"
    else:
        for t in range(len(Groups)):
            oneGroup = Groups[t]
            for m in range(len(oneGroup)):
                #print('oneGroup[m] = ', oneGroup[m][0])
                groupAssignments[oneGroup[m][0]-1] = t + 1
                if t >= K:
                    groupAssignments[oneGroup[m][0]-1] = 1
            #print('oneGroup =', oneGroup)
        groupAssignments = ' '.join(map(str, groupAssignments))
        out = groupAssignments

    #print('groupAssignments =', groupAssignments)

    j = j + N + 1
    #print(f"Case #{i+1}: {out}", end="\n",file=output)
    print(f"Case #{i+1}: {out}",file=output)
