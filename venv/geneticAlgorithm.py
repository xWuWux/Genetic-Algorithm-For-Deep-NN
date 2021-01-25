from random import seed
from random import random
from random import randint


MAX_LAYER = 8
MAX_NEURONS = 128
POPULATION = 8 #best if dividable by 4
GENERATIONS = 10


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
    print("Each of this will take 5 minutes")
    return cost


def sort_and_divide(bag_with_cost):
    sorted_bag = []
    bag_with_cost.sort(key=lambda x:x[1])
    for x in range(len(bag_with_cost)//2, len(bag_with_cost)):
        sorted_bag.append(bag_with_cost[x])
    return sorted_bag


def cross_parents(parent1, parent2):
    cross_point = randint(1, MAX_LAYER)
    child1 = []
    child1.extend(parent1[:cross_point])
    child1.extend(parent2[cross_point:])
    child2 = []
    child2.extend(parent2[:cross_point])
    child2.extend(parent1[cross_point:])
    cost(child1)
    cost(child2)
    return child1, child2


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
#sprawdzenie warunku stopu


print("Generation 1 ~~ best score = " + str(max_score))
pop_bag.sort(key=lambda x:x[1])
for x in pop_bag:
    print(x)

pop_bag = sort_and_divide(pop_bag)







print("xxxxxxxx _gen1_ xxxxxxxxxx")
for x in pop_bag:
    print(x)

    # test
# pop_bag.append([88, 26, 5, 39, 29, 66, 4, 126]) #100.25
#musimy dobrac randomowo starych, i ich ze sobą zmutować.



print("xxxxxxxx _gen2_ xxxxxxxxxx")

pop_bag = calculate_missing_cost(pop_bag)

for x in pop_bag:
    print(x)
