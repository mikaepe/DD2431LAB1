import monkdata as m
import dtree as d

trainset = [m.monk1,m.monk2,m.monk3]
testset = [m.monk1test,m.monk2test,m.monk3test]

for i in range(len(trainset)):
    t=d.buildTree(trainset[i],m.attributes)
    print d.check(t,testset[i])
    print d.check(t,trainset[i])

