from preworkout import *
from workouts import *
from exercises import *


class Workout:                                  # class to hold workout data

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
    element = workout_object.name + '\n'
    for i in range(len(workout_object.exercises)):
        element += workout_object.exercises[i].name + ' ' + str(workout_object[i].exercises.reps) + '\n'
    return element


lower_body_exercises = [deadlift, squat, lunges, bulgarian_split_squats, jump_squat]

lower_body_workout = Workout("Lower Body Burnout", lower_body_exercises, "30 minutes")

workout_list = [lower_body_workout]
