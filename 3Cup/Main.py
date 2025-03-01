import queue
from tkinter import Listbox

from Cup3 import Cup3
from Node import Node
from Problem import Problem

"""
Problem
    -action (state)
    -result (state, action)
    -goal_test (state)
    -path_cost (c, state, action, state)
    -value (state)
    
Node
    -child_node (problem, action)
    -expand (problem)
    -solution ()
    -path ()
    
Cup3
    -actions (state) -> list
    -result (state, action) -> (string)state
"""

CupProblem = Cup3((5,0,0), [(4,1,0),(4,0,1)])
startNode = Node( (5,0,0), None, None, 0 )

nodesQueue = queue.Queue() #feldolgozandó Node-ok listája
nodesQueue.put(startNode)

goalNode = None
found = False

for n in range(100): #100 node-ot engedek max feldolgozni, ne legyen baj belőle
    if nodesQueue.empty(): #ha már nincs több lehetésges lépés
        print("Nincs több feldolgozandó Node, "
              "100 iteráció alatt nem található megoldás")
        break #abbahagyja a keresést
    currentNode = nodesQueue.get() #kiveszi a sorból a soron köv. még fel nem dolgozott elemt
    currentState = currentNode.state
    currentActions = CupProblem.actions(currentState)
    for action in currentActions: #elvégzi az összes lehetséges operátort azon az elemen
        newNode = currentNode.child_node(CupProblem, action) #az így kapott Node-ot
        if CupProblem.goal_test(newNode.state): #leteszteli hogy célállapot-e
            goalNode = newNode
            found = True #leállítja a keresést
            break
        if newNode not in nodesQueue.queue: #ha még nincs bent a sorban
            nodesQueue.put(newNode) #berakja a sorba
    if found: break
    if n == 99:
        print("100 iteráció alatt nem található megoldás :'(")

goal = goalNode #a megtalált célállapotnak
print(goal)
print(goal.parent)
path = []
while goal is not None:
    """print(goal)
    goal = goal.parent"""

    path.append(goal) #kiolvassa az odavezető útját
    print(path.reverse())
    goal = goal.parent
