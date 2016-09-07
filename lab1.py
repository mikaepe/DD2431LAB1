# lab 1 decision trees, machine learning

import monkdata as m
from dtree import entropy, averageGain

monkset = [m.monk1, m.monk2, m.monk3]

ent = [entropy(m.monk1), entropy(m.monk2), entropy(m.monk3)]
print ent
# assignment 1:
# answer: 1.0, 0.9571, 0.9998

monkGain = []

for data in monkset:
    # iterates over monksets
    setGain = []
    for i in range(len(m.attributes)):
        # iterates over attributes for each monkset
        avG = round(averageGain(data,m.attributes[i]),4)
        setGain.append(avG)
    monkGain.append(setGain)

for i in range(len(monkGain)):
    print monkGain[i]

# hej /Sara
