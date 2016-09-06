# lab 1 decision trees, machine learning

import monkdata as m
from dtree import entropy, averageGain

monkset = [m.monk1, m.monk2, m.monk3]

ent = [entropy(m.monk1), entropy(m.monk2), entropy(m.monk3)]
print ent
# assignment 1:
# answer: 1.0, 0.9571, 0.9998


# testar lite.... :-)
avG = averageGain(m.monk1,m.attributes[1])
print avG


