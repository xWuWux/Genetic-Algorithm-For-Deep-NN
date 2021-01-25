from random import seed
from random import random
from random import randint
from random import shuffle


MAX_LAYER = 8
MAX_NEURONS = 128
POPULATION = 40 #need to be dividable by 4
GENERATIONS = 200
TARGET_SCORE = 50000
MUTATION_CHANCE = 0.05


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


def mutate(pop):
    mutated_pop = []
    for ind in pop:
        rand = random()
        if (rand <= MUTATION_CHANCE):
            mutated_pop.append(generate_individual())
            print("MUTEK")
        else:
            mutated_pop.append(ind)
    return mutated_pop


if __name__ == "__main__":
    # creates the initial randomized population bag:
    init_pop_bag = initialize()
    # init_pop_bag=[[2,1,1,1,1,1,1,1],[1,1,1,1,1,1,2,1],[1,1,1,1,1,1,2,1],[1,1,1,1,1,2,1,1],[1,1,1,1,1,1,1,1],[1,2,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
    pop_bag = []

    # initial pop go through neural network and setting the score:
    for x in init_pop_bag:
        pop_bag.append([x, cost(x)])
    best_of_gen = max(pop_bag, key=lambda x: x[1])[1]
    max_score = best_of_gen

    #loop that goes through rest of generations:
    for g in range(1, GENERATIONS):

        #checks if generations maximum was better that top score
        if max_score < best_of_gen: max_score = best_of_gen
        print("Generation " + str(g) + " ~~ best score = " + str(round(best_of_gen,2)))

        #stop condtiion check
        if(max_score) >= TARGET_SCORE:
            print("Target of score = " + str(TARGET_SCORE) + " was accomplished.")
            break

        #sorting the list and getting top 50%
        pop_bag = sort_and_divide(pop_bag)
        #crossover of randomly selected parents
        pop_bag = crossover(pop_bag)
        #mutating
        pop_bag = mutate(pop_bag)
        #calculating score for new children and mutated ones
        pop_bag = calculate_missing_cost(pop_bag)
        #getting best score of generation
        best_of_gen = max(pop_bag, key=lambda x: x[1])[1]
