import queue
from Base.Node import Node


def widthSearch(Problem, steps = 100):
    startNode = Node( Problem.initial, None, None, 0 )

    nodesQueue = queue.Queue() #feldolgozandó Node-ok listája
    nodesQueue.put(startNode)

    goalNode = None
    found = False

    for n in range(steps): #100 node-ot engedek max feldolgozni, ne legyen baj belőle
        if nodesQueue.empty(): #ha már nincs több lehetésges lépés
            print("Nincs több feldolgozandó Node, " + steps.__str__()
                  + "iteráció alatt nem található megoldás")
            break #abbahagyja a keresést
        currentNode = nodesQueue.get() #kiveszi a sorból a soron köv. még fel nem dolgozott elemet
        currentState = currentNode.state
        currentActions = Problem.actions(currentState)
        for action in currentActions: #elvégzi az összes lehetséges operátort azon az elemen
            newNode = currentNode.child_node(Problem, action) #az így kapott Node-ot
            if Problem.goal_test(newNode.state): #leteszteli hogy célállapot-e
                goalNode = newNode
                found = True #ha igen,leállítja a keresést
                break
            if newNode not in nodesQueue.queue: #ha nem, és ha még nincs bent a sorban
                nodesQueue.put(newNode) #berakja a sorba
        if found:
            break
        if n == steps - 1:
            print(steps.__str__() + " iteráció alatt nem található megoldás :'(")

    if goalNode is None:
        return -1

    goal = goalNode #a megtalált célállapotnak
    path = []
    while goal is not None:
        path.append(goal) #kiolvassa az odavezető útját
        goal = goal.parent
    path.reverse()
    return path