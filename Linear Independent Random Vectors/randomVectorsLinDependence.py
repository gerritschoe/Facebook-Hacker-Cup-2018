# Written by Gerrit Schoettler, 2018

import numpy as np
import time

out = 0
tests = 1000000
elapsedCross = 0
elapsedRand = 0
for i in range(tests):
    #a = np.random.rand(3)
    #b = np.random.rand(3)
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])

    t = time.time()
    c = np.random.rand(3)
    A = np.matrix([a,b,c])
    det = np.linalg.det(A)

    elapsedRand = time.time() - t + elapsedRand
    #print('rand time: ', elapsedRand)
    t = time.time()
    c2= np.cross(a, b)
    elapsedCross = time.time() - t + elapsedCross
    #print('cross time: ', elapsedCross)

    if det == 0:
        pass
    else:
        out = out + 1
print('3 random R^3 vectors are linear independent in %d of %d cases.' % (out, tests))
print('Time for %d rand vectors and check: %f, time for %d cross products: %f, fraction cross / rand: %f' % (tests, elapsedRand, tests, elapsedCross, elapsedCross/elapsedRand))