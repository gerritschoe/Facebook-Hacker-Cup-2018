f = open("ethan_traverses_a_tree_sample_input.txt",'r')
output=open("ethan_traverses_a_tree_sample_output_test.txt",'w')
read_rows = f.readlines()
#print(read_rows[1])


"""
def calcPreTraversal(nodes, root,res):
    if root != None:
        print('root = ', root)
        res.append(root)
        leftChild = int(nodes[root][0])
        if leftChild == 0:
            leftChild = None
        else:
            leftChild = leftChild - 1
        rightChild = int(nodes[root][2])
        if rightChild == 0:
            rightChild = None
        else:
            rightChild = rightChild - 1
        print('root = ', root, 'leftChild = ', leftChild)
        print('root = ', root, 'rightChild = ', rightChild)
        print('res = ', res)
        res = res + calcPreTraversal(nodes, leftChild,res)
        res = res + calcPreTraversal(nodes, rightChild,res)
        #res = res + calcPreTraversal(nodes, leftChild)
        #res = res + calcPreTraversal(nodes, rightChild)
    return res
"""
"""
def recursivePreTra(nodes, currNode, prevNode, preTraversal, ):
    leftNode = int(nodes[currNode][0])
    rightNode = int(nodes[currNode][2])
    if rightNode != 0:
        prevNode = currNode
    if leftNode != 0:
        preTraversal.append(leftNode)
        preTraversal = recursivePreTra(nodes, leftNode, prevNode, preTraversal)
    else:
        if rightNode != 0:
            preTraversal.append(rightNode)
            preTraversal = recursivePreTra(nodes, rightNode, prevNode, preTraversal)
        else:
            recursivePreTra(nodes, prevNode, preTraversal)
    return preTraversal
"""

def calPreTraversal(nodes, next):
    preTraversal = []
    if next != -1:
        print('current = ', next + 1, 'childs = ', int(nodes[next].split()[0]), int(nodes[next].split()[1]))
        preTraversal.append(next + 1)

        nextLeft = int(nodes[next].split()[0]) - 1
        nextRight = int(nodes[next].split()[1]) - 1

        preTraversal = preTraversal + calPreTraversal(nodes, nextLeft)
        preTraversal = preTraversal + calPreTraversal(nodes, nextRight)
    return preTraversal
def calcPostTraversal(nodes, next):
    postTraVersal = []
    if next != -1:
        print('current = ', next + 1, 'childs = ', int(nodes[next].split()[0]), int(nodes[next].split()[1]))
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
    print('Tree Number ', i, 'j = ', j, 'N = ', N, ' K = ', K)
    print('nodes = ', nodes)
    print('nodes1 = ', nodes[1].split()[1])
   # print('nodes10 = ', nodes[1][0])
    #print('nodes12 = ', nodes[1][2])
    print('len(nodes) = ', len(nodes))
    preTraFull = calPreTraversal(nodes, 0)
    print('preTraFull = ', preTraFull)
    postTraFull = calcPostTraversal(nodes, 0)
    print('postTraFull = ', postTraFull)
    #PreTraversal = calcPreTraversal(nodes, 0, res)
    #print('PreTraversal = ', PreTraversal)

    j = j + N + 1
    out = N
    print(f"Case #{i+1}: {out}", end="\n",file=output)
    #print(f"Case #{i+1}: {out}",file=output)
