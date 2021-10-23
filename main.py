# Catherine Wallin

import tkinter as tk


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
        element += preworkout_list[i].name + ' $' + str(preworkout_list[i].price) + ' ' + str(preworkout_list[i].servings) + '\n'
    return element


bucked_up = PreWorkout("Bucked Up Woke AF", "Watermelon Lemonade", 54.99, 30, 333)
ghost_legend = PreWorkout("Ghost Legend", "Ocean Water", 44.99, 25, 250)
alani_nu = PreWorkout("Alani Nu Pre-Workout", "Breezeberry", 39.99, 30, 200)
total_war = PreWorkout("Total War REDCON1", "Tiger's Blood", 44.99, 30, 250)

preworkout_list = [bucked_up, ghost_legend, alani_nu, total_war]

class Exercise:                                 # class to hold info about individual exercises

    def __init__(self, name):
        self.name = name
        self.reps = 0


class Workout:                                  # class to hold workout data

    def __init__(self):
        self.title = ""
        self.exercises = []
        self.time = 0
        self.muscle_group = ""

    def add_exercise(self, exercise):
        self.exercises.append(exercise)


window = tk.Tk()
label = tk.Label(text="Workout Application")
label.pack()

create_workout_button = tk.Button(
    text="Create Workout!",
    width=20,
    height=4
)
create_workout_button.pack()

preworkout_button = tk.Button(
    text="Browse Pre-Workout!",
    width=20,
    height=4
)
preworkout_button.pack()


def handle_preworkout_click(event):
    preworkout_window = tk.Tk()
    pre_label = tk.Label(text=print_preworkout(preworkout_list))
    pre_label.pack()

preworkout_button.bind("<Button-1>", handle_preworkout_click)

window.mainloop()



