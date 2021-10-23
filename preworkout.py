from workouts import *
from exercises import *


class PreWorkout:                               # class to hold preworkout information
    def __init__(self, name, flavor, price, servings, caffeine):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.servings = servings
        self.caffeine = caffeine

def print_preworkout(preworkout_list):
    element = ''
    for i in range(len(preworkout_list)):
        element += preworkout_list[i].name + '\n' + ' $' + str(preworkout_list[i].price) + ' ' + str(preworkout_list[i].servings) + ' servings' + '\n\n'
    return element


bucked_up = PreWorkout("Bucked Up Woke AF", "Watermelon Lemonade", 54.99, 30, 333)
ghost_legend = PreWorkout("Ghost Legend", "Ocean Water", 44.99, 25, 250)
alani_nu = PreWorkout("Alani Nu Pre-Workout", "Breezeberry", 39.99, 30, 200)
total_war = PreWorkout("Total War REDCON1", "Tiger's Blood", 44.99, 30, 250)

preworkout_list = [bucked_up, ghost_legend, alani_nu, total_war]