from workouts import *
from exercises import *
import json, requests
from flask import request
import ast
import requests as req


class PreWorkout:                               # class to hold preworkout information
    def __init__(self, name, flavor, price, servings, caffeine):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.servings = servings
        self.caffeine = caffeine


def get_preworkout(preworkout_data):
    if preworkout_data is None:
        resp = req.get("http://localhost:8000/pre-workout")
        preworkout_data = resp.json()
    element = ''
    for product in preworkout_data:
        element += product + '\n' + preworkout_data[product]["brand details"] + "\n" + \
                   preworkout_data[product]["price"] + "\n" + preworkout_data[product]["website"] + "\n\n"

    return element