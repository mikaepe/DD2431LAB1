# lab 1 decision trees, machine learning

import monkdata as m
from dtree import *

monkset = [m.monk1, m.monk2, m.monk3]
att = m.attributes

ent = [entropy(m.monk1), entropy(m.monk2), entropy(m.monk3)]
#print ent
# assignment 1:
# answer: 1.0, 0.9571, 0.9998


def gainCalc(setList, attributesToIterate):
    monkGain = []
    for set in setList:
        # iterates over monksets
        setGain = []

        # fix attributes to iterate
        #attributesToIterate = m.attributes
        #for att in enumerate(attributesToSkip):
        #    attributesToIterate = attributesToIterate.remove(att)

        for i in range(len(attributesToIterate)):
            # iterates over attributes for each monkset
            avG = round(averageGain(set,attributesToIterate[i]),12)
            setGain.append(avG)
        monkGain.append(setGain)
    return monkGain

monkGain = gainCalc(monkset, att)

# for i in range(len(monkGain)):
#     print monkGain[i]

subli = []
for aval in m.attributes[4].values:
    sub = select(m.monk1, m.attributes[4], aval)
    subli.append(sub)

# update remaining attributes
att = tuple(x for x in att if x != m.attributes[4])

monkGain2 = gainCalc(subli, att)

for i in range(len(monkGain2)):
    print monkGain2[i]
