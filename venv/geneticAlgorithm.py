from random import seed
from random import random
from random import randint
from random import shuffle


MAX_LAYER = 8
MAX_NEURONS = 128
POPULATION = 40 #need to be dividable by 4
GENERATIONS = 200
TARGET_SCORE = 50000


def generate_individual():
    new_ind = []
    for x in range (0, MAX_LAYER):
        new_ind.append(randint(1,MAX_NEURONS))
    return new_ind


def initialize():
    pop_bag = []
    for x in range(0, POPULATION):
        pop_bag.append(generate_individual())
    return pop_bag


def cost(ind):
    cost = (ind[0]/ind[1]/ind[2]*ind[3]*ind[4]*ind[5]/ind[6]/ind[7])
    # print("Indiv: " + str(ind) + " | Cost: " + str(cost))
    # print("Each of this will take 5 minutes")
    return cost


def sort_and_divide(bag_with_cost):
    sorted_bag = []
    bag_with_cost.sort(key=lambda x:x[1])
    for x in range(len(bag_with_cost)//2, len(bag_with_cost)):
        sorted_bag.append(bag_with_cost[x])
    return sorted_bag


def cross_parents(parent1, parent2, cross_point):
    child = []
    child.extend(parent1[:cross_point])
    child.extend(parent2[cross_point:])
    return child


def crossover(pop):
    random_index_table = []

    for x in range (0, len(pop)):
        random_index_table.append(x)
    shuffle(random_index_table)
    # print(random_index_table)

    for x in range (0, len(pop), 2):
        p1 = pop[random_index_table[x]][0]
        p2 = pop[random_index_table[x+1]][0]
        cross_point = randint(1, MAX_LAYER)
        pop.append(cross_parents(p1,p2,cross_point))
        pop.append(cross_parents(p2,p1,cross_point))

    return pop


def calculate_missing_cost(population):
    pop_with_scores = []
    for x in population:
        if (len(x) == 2 and len(x[0]) == MAX_LAYER):
            pop_with_scores.append(x)
        elif (len(x) == MAX_LAYER):
            pop_with_scores.append([x, cost(x)])
    return pop_with_scores

# creates the initial randomized population bag:
pop_bag = []
init_pop_bag = initialize()

# initial go through neural network:
for x in init_pop_bag:
    pop_bag.append([x, cost(x)])

max_score = max(pop_bag, key=lambda x: x[1])[1]

#here it'll check if max_score is enough

for g in range(1, GENERATIONS):
    print("Generation " + str(g) + " ~~ best score = " + str(max_score))

    if(max_score) >= TARGET_SCORE: break

    pop_bag = sort_and_divide(pop_bag)
    pop_bag = crossover(pop_bag)
    pop_bag = calculate_missing_cost(pop_bag)

    if max_score < max(pop_bag, key=lambda x: x[1])[1]:
        max_score = max(pop_bag, key=lambda x: x[1])[1]

