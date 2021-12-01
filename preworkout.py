from workouts import *
from exercises import *
import json, requests
from flask import request
import ast
import requests as req
from tkinter import *
from tkinter import ttk


class PreWorkout:
    def __init__(self, name, flavor, price, servings, caffeine):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.servings = servings
        self.caffeine = caffeine


def get_preworkout(preworkout_data):
    if preworkout_data is None:
        pre_workout = open("preworkout.json")
        preworkout_data = json.load(pre_workout)
        #resp = req.get("http://localhost:8000/pre-workout")
        #preworkout_data = resp.json()

    table = Tk()
    table.geometry("1200x300")

    preworkout_display = ttk.Treeview(table, column=("Brand", "Price", "Oz./Servings", "Link"), show='headings', height=15)
    preworkout_display.column("# 1", anchor=CENTER, width="600")
    preworkout_display.heading("# 1", text="Brand")
    preworkout_display.column("# 2", anchor=CENTER, width="100")
    preworkout_display.heading("# 2", text="Price")
    preworkout_display.column("# 3", anchor=CENTER, width="200")
    preworkout_display.heading("# 3", text="Oz./Servings")
    preworkout_display.column("# 4", anchor=CENTER, width="200")
    preworkout_display.heading("# 4", text="Link")

    count = 0
    for product in preworkout_data:
        if count == 45: break

        string = preworkout_data[product]["brand details"]
        if string.find("(") != -1:
            text = string.split("(")
            text[1] = text[1].replace(')', '')

        preworkout_display.insert('', 'end', text=count, values=(text[0], preworkout_data[product]["price"], text[1], preworkout_data[product]["website"]))
        count += 1

    preworkout_display.pack()

    return
