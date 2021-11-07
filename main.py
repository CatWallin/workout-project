# Catherine Wallin

import tkinter as tk
from tkinter import font as tkfont
import requests as req
import flask

from preworkout import *
from workouts import *
from exercises import *

preworkout_data = None


class WorkoutApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (HomePage, LetsWorkoutPage, PreworkoutPage, WorkoutPage):
            page_name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Workout Application", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        lets_workout_button = tk.Button(
            self,
            text="Let's Workout!",
            command=lambda: controller.show_frame("LetsWorkoutPage")
        )

        preworkout_button = tk.Button(
            self,
            text="Browse Pre-Workout!",
            command = lambda: controller.show_frame("PreworkoutPage")
        )
        lets_workout_button.pack()
        preworkout_button.pack()


class LetsWorkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Let's Workout!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #workouts = tk.Label(self, text=print_workout_list(workout_list))
        #workouts.pack(side="bottom", fill="x", pady=10)
        for workout in workout_list:
            #workouts = tk.Label(self, text=workout.name + ' ' + workout.time)
            #workouts.pack(side="bottom", fill="x", pady=10)
            workout_button = tk.Button(
                self,
                text=workout.name + ' ' + workout.time,
                command=lambda: controller.show_frame("WorkoutPage")
            )
            workout_button.pack()

        home_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.place(x=10, y=10)


class PreworkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Browse Pre-Workout", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        pre_label = tk.Label(self, text=get_preworkout(preworkout_data))

        pre_label.pack(side="bottom", fill="x", pady=10)
        home_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.place(x=10, y=10)


class WorkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='name', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #pre_label = tk.Label(self, text=print_preworkout(preworkout_list))
        #pre_label.pack(side="bottom", fill="x", pady=10)
        home_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("LetsWorkoutPage"))
        home_button.place(x=10, y=10)





if __name__ == "__main__":
    app = WorkoutApp()
    app.minsize(300, 300)
    app.mainloop()





