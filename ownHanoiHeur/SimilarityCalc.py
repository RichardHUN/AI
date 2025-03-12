def SimilarityCalc(problem, currentState):
    if problem.goal_test(currentState):
        return 0

    nrOfDisksToMove = 0
    currentPoles = currentState.split("_")
    goalPoles = problem.goal.split("_")
    movesNecessaryToPlace = 0

    for i in range(problem.nrOfPoles):
        for j in range( len(currentPoles[i]) ):
            if j >= len(goalPoles[i]):#Ha nincs korong ugyan azon a pozíción az célállapotba
                nrOfDisksToMove += 1
                movesNecessaryToPlace = calcDistance(currentPoles, goalPoles, i, j, nrOfDisksToMove , movesNecessaryToPlace)
                continue
            if currentPoles[i][-j-1] != goalPoles[i][-j-1]:#Ha nem ugyan az a korong van azon a pozíción a célállapotba
                nrOfDisksToMove += 1
                movesNecessaryToPlace = calcDistance(currentPoles, goalPoles, i, j, nrOfDisksToMove , movesNecessaryToPlace)
    #print(nrOfDisksToMove + movesNecessaryToPlace)
    return nrOfDisksToMove + movesNecessaryToPlace


def SimilairtyCalc(problem, currentNode):
    return SimilarityCalc(problem, currentNode.state)


def calcDistance(currentPoles, goalPoles, i, j, nrOfDisksToMove, movesNecessaryToPlace):
    if j != 0:
        movesNecessaryToPlace += j

    #A jelenleg vizsgált szám heylének oszlopindexe a célállapotba (ChatGPT szerint)
    index = next((index for index, string in enumerate(goalPoles) if string.find(currentPoles[i][j]) != -1), -1)

    #Ha a keresett szám a célállapotba nem a rúd tetején van, a szükséges lépések számához hozzáadja
    #a fölötte levő korongok számát kétszer
    if goalPoles[index].find(currentPoles[i][j]) != 0:
        movesNecessaryToPlace += ( goalPoles[index].find(currentPoles[i][j]) ) #* 2
    #print(nrOfDisksToMove + movesNecessaryToPlace)
    return movesNecessaryToPlace