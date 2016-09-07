# lab 1 decision trees, machine learning

import numpy
import monkdata as m
from dtree import *

monkSet = [m.monk1, m.monk2, m.monk3]                   # monk sets defined in monkdata.py
monkTestSet = [m.monk1test, m.monk2test, m.monk3test]   # monk test sets
att = m.attributes                                      # attributes to consider


# --- assignment 1 : compute entropy ---
########################################

ent = []
for monk in monkSet:
    ent.append(round(entropy(monk),3))                  # supress some decimals
print 'entropy: ', ent


# --- assignment 2 : average gain ---
#####################################

def gainCalc(setList, attributesToIterate):
    monkGain = []
    for set in setList:
        # iterates over monksets
        setGain = []

        for i in range(len(attributesToIterate)):
            # iterates over attributes for each monk
            avG = round(averageGain(set,attributesToIterate[i]),12)
            setGain.append(avG)
        monkGain.append(setGain)
    return monkGain

# calculate average gain for all monk in monkset:
monkGain = gainCalc(monkSet, att)
print 'agerage gain calculation for monk1, monk2, monk3:'
for i in range(len(monkGain)):
    print monkGain[i]


# --- assignment 3 : build tree ---

# --- 3a : build manually ---
# create subsets according to A5:
subli = []
for val in m.attributes[4].values:
    sub = select(m.monk1, m.attributes[4], val)
    subli.append(sub)
# update remaining attributes:
att = tuple(x for x in att if x != m.attributes[4])
# calcate average gain for each subset and get max:
monkGain2 = gainCalc(subli, att)
maxGain = []; ind = []
print 'agerage gain calculation for each subset:'
for i in range(len(monkGain2)):
    mg = monkGain2[i]
    print mg
    maxGain.append(max(mg))
    ind.append(mg.index(max(mg)))

print 'max: ', maxGain
print 'ind: ', ind
# remove first node since gain is zero:
maxGain = maxGain[1:]
ind = ind[1:]
subli = subli[1:]
print 'max: ', maxGain
print 'ind: ', ind

# determine majority class of second level nodes:
print 'majority class by second level nodes:'
for i in range(len(maxGain)):
    for val in m.attributes[ind[i]].values:
        sub = select(subli[i], m.attributes[ind[i]], val)
        print mostCommon(sub)
    print ''

# --- 3b : build with predefined function ---
for i in range(len(monkSet)):
    fullTree = buildTree(monkSet[i], m.attributes)
    limTree = buildTree(monkSet[i], m.attributes,2)
    print 'error training set', i+1, ':', round(1-check(limTree, monkSet[i]),4)
    print 'error test set', i+1, ':', round(1-check(fullTree, monkTestSet[i]),4)
