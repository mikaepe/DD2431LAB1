# lab 1 decision trees, machine learning

import monkdata as m
from dtree import *
import os, random
os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal

monkSet = [m.monk1, m.monk2, m.monk3]   # monk sets defined in monkdata.py
monkTestSet = [m.monk1test, m.monk2test, m.monk3test]
att = m.attributes                      # attributes to consider

# --- assignment 1 : calculate entropy ---
ent = []
for monk in monkSet:
    ent.append(round(entropy(monk),3))
# print 'entropy: ', ent

# --- assignment 2 : average gain ---
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
# for i in range(len(monkGain)):
#    print monkGain[i]


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
    #print mg
    maxGain.append(max(mg))
    ind.append(mg.index(max(mg)))

# print 'max: ', maxGain
# print 'ind: ', ind
# remove first node since gain is zero:
maxGain = maxGain[1:]
ind = ind[1:]
subli = subli[1:]
# print 'max: ', maxGain
# print 'ind: ', ind

# determine majority class of second level nodes:
print 'majority class by second level nodes:'
for i in range(len(maxGain)):
    for val in m.attributes[ind[i]].values:
        sub = select(subli[i], m.attributes[ind[i]], val)
    #     print mostCommon(sub)
    # print '-'

# --- 3b : build with predefined function ---
for i in range(len(monkSet)):
    fullTree = buildTree(monkSet[i], m.attributes)      # enough levels
    limTree = buildTree(monkSet[i], m.attributes, 2)    # only two-level
    # print 'error training set', i+1, ':', round(1-check(limTree, monkSet[i]),4)
    # print 'error test set', i+1, ':', round(1-check(fullTree, monkTestSet[i]),4)

# --- assignment 4 : pruning ---

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

for fraction in [.3, .4, .5, .6, .7, .8]:
    print 'fraction', fraction, ':'
    # do for both monk1 and for monk3:
    for monk in [0,2]:
        # partition into training and validation set:
        monkTrain, monkVal = partition(monkSet[monk], fraction)

        bestTree = buildTree(monkTrain, m.attributes)  # first pruned tree
        minErr = round(1-check(bestTree, monkVal),3)   # its error
        accuracyIncreases = True    # always prune at least once
        print 'error, before pruning monk', monk+1, ':', minErr

        while accuracyIncreases:
            # print 'tree:', tree1
            prunedList = allPruned(bestTree)
            # print 'pruned tree:', pruned1
            err = []; ind = []
            prevMinErr = minErr
            # prune current tree in all possible ways:
            for prtree in prunedList:
                err.append(round(1-check(prtree, monkVal),3))
                # find pruned tree will smallest error and choose as best tree so far:
                minErr = min(err)
                ind = err.index(minErr)
                bestTree = prunedList[ind]
                # condition to stop pruning if accuracy decreases
                accuracyIncreases = (minErr < prevMinErr)

        print 'error, after pruning monk', monk+1, ':', minErr
