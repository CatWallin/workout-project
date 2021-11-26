from preworkout import *
from workouts import *
import csv


class Exercise:

    def __init__(self, name, muscle_groups, type):
        self.name = name
        self.muscle_groups = muscle_groups
        self.type = type

exercises_master_list = []

with open('exercise_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        exercise = Exercise(row[0], row[1], row[2])
        exercises_master_list.append(exercise)
