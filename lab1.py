# lab 1 decision trees, machine learning

# --- imports and such ---
##########################

import numpy
import monkdata as m
from dtree import *

monkSet = [m.monk1, m.monk2, m.monk3]   # monk sets def. in monkdata.py
monkTestSet = [m.monk1test, m.monk2test, m.monk3test]   # test sets
att = m.attributes                      # attributes to consider


# --- function definitions ---
##############################

def gainCalc(setList, attributesToIterate):

    monkGain = []
    for set in setList:                 # iterates over monksets
        setGain = []
        for i in range(len(attributesToIterate)):
            # iterates over attributes for each monk
            avG = round(averageGain(set,attributesToIterate[i]),12)
            setGain.append(avG)
        monkGain.append(setGain)
    return monkGain


# --- assignment 1 : compute entropy ---
########################################

print 'press <enter> to continue the script'

raw_input('compute entropy:')
ent = []
for monk in monkSet:
    ent.append(round(entropy(monk),4))  # supress some decimals
print 'entropy: ', ent


# --- assignment 2 : average gain ---
#####################################

raw_input('compute average gain for monk1, monk2, monk3:')
monkGain = gainCalc(monkSet, att)       # compute for 3 sets in monkSet
for i in range(len(monkGain)):
    print monkGain[i]


# --- assignment 3 : build tree ---
###################################

# --- 3a : build manually ---
raw_input('press <enter> to compute info to draw tree manually:')
subli = []                              # create subsets according to A5:
for val in m.attributes[4].values:
    sub = select(m.monk1, m.attributes[4], val)
    subli.append(sub)
# update remaining attributes:
att = tuple(x for x in att if x != m.attributes[4])
# calcate average gain for each subset and get max:
monkGain2 = gainCalc(subli, att)        # compute avg.gain for subsets
maxGain = []; ind = []

raw_input('average gain calculation for each subset:')
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
