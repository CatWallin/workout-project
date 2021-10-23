from preworkout import *
from workouts import *


class Exercise:                                 # class to hold info about individual exercises

    def __init__(self, name):
        self.name = name
        self.reps = 12


deadlift = Exercise("deadlift")
squat = Exercise("squat")
lunges = Exercise("lunges")
bulgarian_split_squats = Exercise("bulgarian split squats")
jump_squat = Exercise("jump squat")