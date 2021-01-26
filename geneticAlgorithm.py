from random import random
from random import randint
from random import shuffle


MAX_LAYER = 8
MAX_NEURONS = 128
POPULATION = 240  # needs to be dividable by 4
GENERATIONS = 50
TARGET_SCORE = 1000000
MUTATION_CHANCE = 0.05


def generate_individual():
    new_ind = []
    for n in range(0, MAX_LAYER):
        new_ind.append(randint(1, MAX_NEURONS))
    return new_ind


def initialize():
    pop = []
    for n in range(0, POPULATION):
        pop.append(generate_individual())
    return pop


def cost(ind):
    c = (ind[0]/ind[1]/ind[2]*ind[3]*ind[4]*ind[5]/ind[6]/ind[7])
    return c


def sort_and_divide(pop_with_cost):
    sorted_pop = []
    pop_with_cost.sort(key=lambda x: x[1])
    for n in range(len(pop_with_cost) // 2, len(pop_with_cost)):
        sorted_pop.append(pop_with_cost[n])
    return sorted_pop


def roulette(pop_with_cost):
    cost_sum = sum(n for _, n in pop_with_cost)

    cost_table = []
    for ind in pop_with_cost:
        cost_table.append(ind[1])

    rel_cost = [cost_ind / cost_sum for cost_ind in cost_table]
    probability = [sum(rel_cost[:i + 1]) for i in range(len(rel_cost))]

    new_pop = []
    for n in range(POPULATION//2):
        r = random()
        for (i, individual) in enumerate(pop_with_cost):
            if r <= probability[i]:
                new_pop.append(individual)
                break
    return new_pop


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

    for x in range(0, len(pop), 2):
        p1 = pop[random_index_table[x]][0]
        p2 = pop[random_index_table[x+1]][0]
        cross_point = randint(1, MAX_LAYER)
        pop.append(cross_parents(p1, p2, cross_point))
        pop.append(cross_parents(p2, p1, cross_point))
    return pop


def calculate_missing_cost(pop):
    pop_with_scores = []
    for ind in pop:
        if len(ind) == 2 and len(ind[0]) == MAX_LAYER:
            pop_with_scores.append(ind)
        elif len(ind) == MAX_LAYER:
            pop_with_scores.append([ind, cost(ind)])
    return pop_with_scores


def mutate(pop):
    mutated_pop = []
    for ind in pop:
        rand = random()
        if rand <= MUTATION_CHANCE:
            mutated_pop.append(generate_individual())
        else:
            mutated_pop.append(ind)
    return mutated_pop


if __name__ == "__main__":
    # creates the initial randomized population bag:
    init_pop_bag = initialize()
    pop_bag = []

    # initial pop go through neural network and setting the score:
    for init_ind in init_pop_bag:
        pop_bag.append([init_ind, cost(init_ind)])
    best_of_gen = max(pop_bag, key=lambda x: x[1])[1]
    max_score = best_of_gen

    # loop that goes through rest of generations:
    for g in range(1, GENERATIONS+1):

        # checks if generations maximum was better that top score
        if max_score < best_of_gen:
            max_score = best_of_gen

        print("Generation " + str(g) + " ~~ best score = " + str(round(best_of_gen,2)))

        # stop condition check
        if max_score >= TARGET_SCORE:
            print("Target of score of " + str(TARGET_SCORE) + " was accomplished.")
            break

        # sorting the list
        # #1 taking top 50% to next generation (much slower)
        # pop_bag = sort_and_divide(pop_bag)
        # #2 roulette method
        pop_bag = roulette(pop_bag)
        # crossover of randomly selected parents
        pop_bag = crossover(pop_bag)
        # mutating
        pop_bag = mutate(pop_bag)
        # calculating score for new children and mutated ones
        pop_bag = calculate_missing_cost(pop_bag)
        # getting best score of generation
        best_of_gen = max(pop_bag, key=lambda x: x[1])[1]
