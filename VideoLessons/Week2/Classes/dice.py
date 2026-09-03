import random

class Dice:
    # you can add default values
    def __init__(self, sides=6):
        self.sides = sides

    #refers to roll a dice with X sides
    def roll(self):
        return random.randint(1, self.sides)


dice = Dice(5)
print(dice.roll())

# is it really random?
for roll in range(1, 6):
    print(dice.roll())
