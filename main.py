# Catherine Wallin

import tkinter as tk
from tkinter import font as tkfont


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


class WorkoutApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (HomePage, CreateWorkoutPage, PreworkoutPage):
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

        create_workout_button = tk.Button(
            self,
            text="Create Workout!",
            command=lambda: controller.show_frame("CreateWorkoutPage")
        )

        preworkout_button = tk.Button(
            self,
            text="Browse Pre-Workout!",
            command = lambda: controller.show_frame("PreworkoutPage")
        )
        create_workout_button.pack()
        preworkout_button.pack()


class CreateWorkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create Workout", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        home_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.place(x=10, y=10)


class PreworkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Browse Pre-Workout", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        pre_label = tk.Label(self, text=print_preworkout(preworkout_list))
        pre_label.pack(side="bottom", fill="x", pady=10)
        home_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.place(x=10, y=10)

if __name__ == "__main__":
    app = WorkoutApp()
    app.minsize(300, 300)
    app.mainloop()





