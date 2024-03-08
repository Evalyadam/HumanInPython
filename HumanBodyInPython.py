import random
from time import sleep

name_options = ["Jaiden", "Bob", "Mike", "John", "Braiden"]

randomnameselect = random.randint(0, 4)

name = name_options[randomnameselect]

gender = random.choice(["Female", "Male"])

# Really important bit down below. DO NOT CHANGE IT!!


class Human:
        def __init__(self, name, sex, reactiontime):
            self.name = name
            self.sex = sex
            self.reactiontime = reactiontime

    def __str__(self):
        return f"{self.name}, {self.sex}, {self.reactiontime} s"

    def set_name(self, new_name):
        self.name = new_name

    def set_sex(self, new_sex):
        self.sex = new_sex

    def set_reaction_time(self, new_rt):
        self.reactiontime = new_rt

human = Human(name=name_options[randomnameselect], gender=gender)


