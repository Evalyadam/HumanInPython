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
        print(f"{self.name}, {self.sex}, {self.reactiontime} s")


human = Human(name=name_options[randomnameselect], sex=gender, reactiontime=random.Random())


