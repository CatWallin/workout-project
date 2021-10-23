# Catherine Wallin

import tkinter as tk
from tkinter import font as tkfont
from preworkout import *
from workouts import *
from exercises import *


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
        workouts = tk.Label(self, text=print_workout_list(workout_list))
        workouts.pack(side="bottom", fill="x", pady=10)
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





