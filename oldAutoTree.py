
import monkdata as m
from dtree import *
from drawtree import *

lev = input('levels: ')

tree = buildTree(m.monk1,m.attributes, lev)

print buildTree(m.monk1, m.attributes, lev)

#drawTree(buildTree(m.monk1, m.attributes, lev))

print 'correct', check(tree,m.monk1)
