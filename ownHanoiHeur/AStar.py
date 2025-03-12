from ownHanoiHeur.Node import Node
from ownHanoiHeur.SimilarityCalc import calcDistance, SimilarityCalc


def AStar(problem, maxSteps = 1000):
    initNode = Node(problem.initial, None, None, SimilarityCalc(problem, problem.initial))
    accessibleNodes = []
    visitedAlready = []
    for node in initNode.expand(problem):
        accessibleNodes.append( (node, node.path_cost) )

    i = 0
    while len(accessibleNodes) != 0:
        accessibleNodes.sort(key = lambda tpl: tpl[1])
        if type(accessibleNodes[0][0]) != Node:
            print("Nem Node típusú elem ˘:/")
            #print(accessibleNodes[0])
            return
        #print(accessibleNodes[0])
        #print(accessibleNodes)
        node = accessibleNodes.pop(0)[0]
        if problem.goal_test(node.state):
            return node
        for node in node.expand(problem):
            if (node, node.path_cost) not in accessibleNodes and (node, node.path_cost) not in visitedAlready:
                accessibleNodes.append( (node, node.path_cost) )
            elif (node, node.path_cost) not in visitedAlready:
                visitedAlready.append( (node, node.path_cost) )
        #accessibleNodes.append(node for node in node.expand(problem))
        i += 1
        #maxSteps-szer fut csak le, ne legyen végtelen ciklus
        if i == maxSteps-1:
            print("No solution found in " + str(maxSteps) + " steps")
            return
    print("Reached end of search tree, no solution found")
    return