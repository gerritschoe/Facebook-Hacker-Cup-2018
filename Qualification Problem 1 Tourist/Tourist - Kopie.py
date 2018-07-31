import numpy as np
f = open("tourist_example_input.txt")
output=open("tourist_output_submission.txt",'w')
read_rows = f.readlines()

def visit(N,K,V):
    # N = number of places
    # K = number of places to visit at one time
    # V = V'th visit
    positionOfFirst = ((V-1) * (N-K)) % N
    return positionOfFirst

T = int(read_rows[0])
#print(T)
j = 1
for i in range(T):
    NKV = read_rows[j] #list
    [N,K,V] = NKV.split()
    N = int(N)
    K = int(K)
    V = int(V)
    positionOfFirst = visit(N, K, V)
    #print('positionOfFirst = ',positionOfFirst)
    places = read_rows[j+1:j+N+1]
    positions = list(range(N))
    for k in range(N - positionOfFirst):
        positions.append(positions.pop(0))
    positions = positions[0:K]
    j = j + N + 1

    positions = np.asarray(positions)
    positions.sort()
    #print(positions)
    #print(places)
    placesSorted = list()
    for h in range(len(positions)):
        placesSorted.append(places[positions[h]].rstrip())
    placesSorted = ' '.join(placesSorted)

    #print(f"Case #{i+1}: {placesSorted}", end="",file=output)
    print(f"Case #{i+1}: {placesSorted}",file=output)

