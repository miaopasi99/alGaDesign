import numpy as np
pop = np.random.randint(2, size=(1, 32))
mgBound = [4, 9]
mgPop = pop[:, [0, 5, 10, 15, 20, 25, 30, 31]]
mg = mgPop.dot(2** np.arange(8)[::-1]/ float(2** 8- 1)* (mgBound[1]- mgBound[0]))+ mgBound[0]
print(pop)
print(mg)