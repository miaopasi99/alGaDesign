import numpy as np

def getFitness(pop): #计算适应度的函数
     return  

def translateDNA(pop): #将编码转换为实际值
    return


def select(pop, fitness):
    idx = np.random.choice(np.arrange(POP_SIZE), size = POP_SIZE, replace = True, p = (fitness)/(fitness.sum()))
    return pop[idx]
    
    
def crossoverAndMutation(pop, CROSSOVER_RATE = 0.8):  #交叉与变异
    new_pop = []
    for father in pop:
        child = father 
        if np.random .rand() < CROSSOVER_RATE:
            mother = pop[ni.random.randient(POP_SIZE)] #选择一个母亲
            cross_points = np.random.randint(low = 0,high = DNA_SIZE*eleNum)
            child[cross_points:] = mother[cross_points:]
        mutation(child)
        new_pop.append(child)
    return new_pop

def mutation(child, MUTATION_RATE):     #变异的函数
    if np.random.rand () < MUTATION_RATE:
        mutate_point = np.random.radint(0, DNA_SIZE*eleNum) #随机选择一个变异点
        child[mutate_point] = child[mutate_point]^1    #反转该点

def print_info(pop):
    fitness = get_fitness(pop)
    max_fitness_index = np.argmax(fitness)
    print("max_fitness:", fitness[max_fitness_index])
    x,y = translateDNA(pop)
    print("最优的基因型：", pop[max_fitness_index])
    print("对应的元素含量为：", )

