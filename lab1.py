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

        for i in range(len(attributesToIterate)):
            # iterates over attributes for each monkset
            avG = round(averageGain(set,attributesToIterate[i]),12)
            setGain.append(avG)
        monkGain.append(setGain)
    return monkGain

monkGain = gainCalc(monkset, att)

# for i in range(len(monkGain)):
#     print monkGain[i]

subli1 = []
for aval in m.attributes[4].values:
    sub = select(m.monk1, m.attributes[4], aval)
    subli1.append(sub)

# update remaining attributes
att = tuple(x for x in att if x != m.attributes[4])

monkGain2 = gainCalc(subli1, att)

# for i in range(len(monkGain2)):
#     print monkGain2[i]

# determine majocity class of second level nodes
for aval in m.attributes[3].values:
    sub = select(subli1[1], m.attributes[3], aval)
    print mostCommon(sub)
print
for aval in m.attributes[5].values:
    sub = select(subli1[2], m.attributes[5], aval)
    print mostCommon(sub)
print
for aval in m.attributes[0].values:
    sub = select(subli1[3], m.attributes[0], aval)
    print mostCommon(sub)
