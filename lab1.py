# lab 1 decision trees, machine learning

# --- imports and such ---
##########################

import monkdata as m
from dtree import *
from drawtree import *
import os, random, numpy

os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal

mSet = [m.monk1, m.monk2, m.monk3]   # monk sets def. in monkdata.py
monkTestSet = [m.monk1test, m.monk2test, m.monk3test]   # test sets
att = m.attributes                      # attributes to consider

# --- function definitions ---
##############################

def gainCalc(setList, attToIter):
    # computes gain for sets in setlist for the attToIter

    monkGain = []
    for set in setList:                 # iterates over monksets
        setGain = []
        for i in range(len(attToIter)): # run for attToIter and each mSet
            avG = round(averageGain(set,attToIter[i]),6)
            setGain.append(avG)
        monkGain.append(setGain)
    return monkGain


def part(data, fraction):
    # partition function as given in description

    ldata = list(data)                  # data => list
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def cls():
    # clear output promt

    os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal



# --- assignment 1 : compute entropy ---
#########################################

print 'press <enter> to continue the script throughout'

raw_input('compute entropy:')
ent = []                                # list of the entropies
for monk in mSet:
    ent.append(round(entropy(monk),4))  # supress some decimals
print 'entropy: ', ent                  # display entropies


# --- assignment 2 : average gain ---
#########################################

raw_input('compute average gain for monk1, monk2, monk3:')
monkGain = gainCalc(mSet, att)          # compute for 3 sets in mSet
for i in range(len(monkGain)):
    print monkGain[i]


# --- assignment 3 : build tree ---
#########################################

# --- 3a : build manually ---

raw_input('compute info to draw tree manually using A5 at root:')
subli = []                              # create subsets according to A5:
for val in m.attributes[4].values:
    sub = select(m.monk1, m.attributes[4], val)
    subli.append(sub)

att = tuple(x for x in att if x != m.attributes[4]) # rm A5 attribute

monkGain2 = gainCalc(subli, att)        # compute avg.gain for subsets
maxGain = []; ind = []                  # lists to figure splits at 2nd nodes

for i in range(len(monkGain2)):
    mg = monkGain2[i]
    #print mg
    maxGain.append(max(mg))
    ind.append(mg.index(max(mg)))
    
indStr = ['A'+str(x+1+int(x >=4)) for x in ind] # lite hardkodat har ar jag radd..
print 'max gain at 2nd nodes and attribute:'
print 'max: ', maxGain
print 'ind: ',                          # display attributes w/ max gain
for s in indStr:
    print s,                            # print attributes
print

maxGain = maxGain[1:]                   # remove 1st node, gain zero (leaf)
ind = ind[1:]
subli = subli[1:]
''' #multiline comment :-)
print 'max: ', maxGain
print 'ind: ', ind
'''

raw_input('majority class by second level nodes (except leaf):')
for i in range(len(maxGain)):
    for val in m.attributes[ind[i]].values:
        sub = select(subli[i], m.attributes[ind[i]], val)
    print mostCommon(sub),' ',
print

raw_input('\nNow check the result of builtin functions:')
cls()

# --- 3b : build with predefined function ---


text = '\n1: text based tree\n2: visual tree\nq: quit\n'
text2 = 'wrong, press q+enter to continue or enter to check trees'

while True:
    # an attempt to some u/i, so we dont need to see all trees....
    answer = raw_input(text)
    if answer in ['1','2','q']:
        if answer == '1' or answer == '2':
            lev = int(raw_input('levels?')) # levels of tree to draw
            monks = int(raw_input('set?'))  # which set to draw
            if answer == '1':               # call builtin fcts:
                print buildTree(mSet[monks-1],m.attributes, lev)
            else:                           # call drawTree:
                drawTree(buildTree(m.monk1,m.attributes,lev))
        elif answer == 'q':
            cls()                       # clear screen and cont. script
            print('continuing script')
            break
    else:
        print text2                     # user error


for i in range(len(mSet)):
    # fullTree = buildTree(mSet[i], m.attributes)   # full tree
    limTree = buildTree(mSet[i], m.attributes, 2)   # only two-level
    # print 'error training set', i+1, ':', round(1-check(limTree, mSet[i]),4)
    # print 'error test set', i+1, ':', round(1-check(fullTree, monkTestSet[i]),4)


# --- assignment 4 : pruning ---
#########################################

raw_input('continue with assignment 4, pruning:')

for fraction in [.3, .4, .5, .6, .7, .8]:
    raw_input('fraction '+str(fraction)+' :')

    for monk in [0,2]:                  # perform for monk1 & monk2
        mTrain, mVal = part(mSet[monk], fraction)   # split, training & validation
        bestTree = buildTree(mTrain, m.attributes)  # first pruned tree
        minErr = round(1-check(bestTree, mVal),3)   # its error
        accuracyIncreases = True                    # always prune once
        print 'error, before pruning monk', monk+1, ':', minErr

        while accuracyIncreases:
            # print 'tree:', tree1
            prunedList = allPruned(bestTree)
            # print 'pruned tree:', pruned1
            err = []; ind = []
            prevMinErr = minErr
            # prune current tree in all possible ways:
            for prtree in prunedList:
                err.append(round(1-check(prtree, mVal),3))
                # find pruned tree will smallest error and choose as best tree so far:
                minErr = min(err)
                ind = err.index(minErr)
                bestTree = prunedList[ind]
                # condition to stop pruning if accuracy decreases
                accuracyIncreases = (minErr < prevMinErr)

        print 'error, after pruning monk', monk+1, ':', minErr

# End script lab1.py

