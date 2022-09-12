import random
import matplotlib.pyplot as plt
import numpy as np

class Dice():
    def __init__(self, sides):
        self.roll = random.randint(0, sides)

class DiceGroup():
    def __init__(self, dices, sides):
        self.diceList = [Dice(sides) for x in range(dices)]
        self.total = 0
        for dice in self.diceList:
            self.total += dice.roll
        self.average = self.total / dices

SIDES = 6
DICES = 100
ITTERATIONS = 10000

diceGroupList = []
for i in range(ITTERATIONS):
    diceGroupList.append(DiceGroup(DICES, SIDES))

# print(diceGroupList)

# total = 0
# for dice in diceList:
#     total += dice.roll
# average = total / DICES
# x =
# totals = []
# for group in diceGroupList:
#     totals.append(group.total)

totals = [group.total for group in diceGroupList]
# Show plain totals
# plt.scatter(totals, [i for i in range(len(diceGroupList))])

percentages = []
for i in range(SIDES*DICES):
    percentages.append(0)
for total in totals:
    percentages[total] += 1

for i, percent in enumerate(percentages):
    percentages[i] = (percent / ITTERATIONS) * 100

print(percentages)

plt.scatter([i for i in range(len(percentages))], percentages)


plt.show()