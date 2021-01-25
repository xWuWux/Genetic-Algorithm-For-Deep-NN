from random import seed
from random import random
from random import randint

MAX_LAYER = 8
MAX_NEURONS = 128

#neurony min. 1
#warstwa moze byc 1

def cross_parents(parent1, parent2):
    cross = randint(1,8)
    child = []
    child.extend(parent1[:cross])
    child.extend(parent2[cross:])
    print(child)
    return child


hidden_units = [8,40,50,50,30,20,20,10,8]
hidden_units2 = [3,1,1,1,1,1,1,1,1]



[3][12,12,12,12,24,424,412]


layers = 8;
hidden_units = [40,50,50,30,20,20,10,8]


print(len(hidden_units))

8,13,123,213,23,23,
1,12



for x in range (0,20):
    cross_parents(hidden_units2, hidden_units)




def siecNeuronowa(hidden_units):
    cel = hidden_units[0]*hidden_units[1]
    return cel

