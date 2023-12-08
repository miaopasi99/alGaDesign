import numpy as np

DNA_SIZE = 8 
POP_SIZE = 200
elemNum = 5 #AL   Mg:8bit Si:6bit Sc：6bit Zr:6bit Mn:6bit
N_GENERATIONS = 50
MUTATION_RATE = 0.005
CROSSOVER_RATE = 0.8

mgBound = [4, 9]
siBound = [0.01, 2.5]
scBound = [0.2, 1]
zrBound = [0.2, 0.6]
mnBound = [0.3, 0.8]





if __name__ == "__main__":
    pop = np.random.radient(2, size = (POP_SIZE, 32))  #生成01矩阵，其中行数为种群数目，列数为元素个数*DNA数目，相当于每一行是一个种群的个体
    for _ in range(N_GENERATIONS):  #迭代N代
        pop = np.array(crossAndMutation(pop, CROSSOVER_RATE))   
        fitness = getFitness(pop)
        pop = select(pop, fitness)
    prit_info(pop)

    
