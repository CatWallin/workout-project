import tkinter.ttk
from tkinter import *
from tkinter import ttk
from preworkout import *
from workouts import *
from exercises import *


class Workout:

    def __init__(self, name, exercises, time):
        self.name = name
        self.exercises = exercises
        self.time = time

    def add_exercise(self, exercise):
        self.exercises.append(exercise)


def print_workout_list(workout_list):
    element = ''
    for i in workout_list:
        element += i.name + ' ' + str(i.time) + '\n'
    return element


def print_workout(workout_object):

    workout_tk = Tk()
    workout_tk.geometry("450x150")

    table = ttk.Treeview(workout_tk, column=('exercise', 'reps'), show='headings', height=5)
    table['columns'] = ('exercise', 'reps')

    table.column("0", anchor=CENTER)
    table.heading("0", text="Exercise")
    table.column("1", anchor=CENTER)
    table.heading("1", text="Reps")

    for i in range(len(workout_object.exercises)):

        table.insert('', 'end', text=i, values=(workout_object.exercises[i].name, str(workout_object.exercises[i].reps)))

    table.pack()

    return


quad_exercises = []

for exercise in exercises_master_list:
    if "Quads" in exercise.muscle_groups:
        quad_exercises.append(exercise)
        print(exercise.name)

quad_burnout = Workout("Quad Burnout!", quad_exercises, "30 minutes")


upper_body_exercises = []

for exercise in exercises_master_list:
    if "Chest" in exercise.muscle_groups or "Biceps" in exercise.muscle_groups or "Triceps" in exercise.muscle_groups:
        upper_body_exercises.append(exercise)
        print(exercise.name)

upper_body = Workout("Upper Body", upper_body_exercises, "30 minutes")

workout_list = [quad_burnout, upper_body]
