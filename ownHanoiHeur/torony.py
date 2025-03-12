from Base.Problem import Problem
from Base.WidthSearch import widthSearch
from ownHanoiHeur.SimilarityCalc import SimilarityCalc
from ownHanoiHeur.AStar import AStar


class torony(Problem):
    def __init__(self, nrOfPoles = 3, nrOfDisks = 3, initial=None, goal=None):
        initState = ""
        goalState = ""
        if initial is None:
            for i in range(nrOfDisks):
                initState += str(i + 1)
            for i in range(nrOfPoles-1):
                initState += "_"
        else:
            if initial.count("_") != nrOfPoles - 1:
                print("Wrong number of poles in initial state")
                return
            initState = initial
        if goal is None:
            for i in range(nrOfPoles-1):
                goalState += "_"
            for i in range(nrOfDisks):
                goalState += str(i + 1)
        else:
            if goal.count("_") != nrOfPoles - 1:
                print("Wrong number of poles in goal state")
                return
            goalState = goal
        super().__init__(initState, goalState)
        self.nrOfPoles = nrOfPoles
        self.nrOfDisks = nrOfDisks
    #"123__"

    def actions(self, state):
        acts = []
        poles = state.split("_")

        for i in range(self.nrOfPoles):
            for j in range(self.nrOfPoles):
                if i == j:
                    continue
                if poles[i] != "" and (poles[j] == "" or int(poles[i][0]) < int(poles[j][0]) ):
                    acts.append("O_" + (i+1).__str__() + "_" + (j+1).__str__())
        return acts

    def result(self, state, action):
        newState = [ "" for i in range(self.nrOfPoles) ]
        poles = state.split("_")
        fromIndex = int(action.split("_")[1]) - 1
        toIndex = int(action.split("_")[2]) - 1

        diskToMove = poles[fromIndex][0]
        #poles[fromIndex][0] =
        #poles[fromIndex].replace(poles[fromIndex][0], "")
        poles[fromIndex] = poles[fromIndex][1:]
        newState[toIndex] = diskToMove + poles[toIndex]
        for i in range(self.nrOfPoles):
            if i != toIndex:
                newState[i] = poles[i]
        newState = "_".join(newState)
        return newState

    def path_cost(self, c, state1, action, state2):
        """print(SimilarityCalc(self, state1))
        print(SimilarityCalc(self, state2))"""
        return SimilarityCalc(self, state1) + SimilarityCalc(self, state2) + 1 #+ heuristic_calc_second_to_last_used(self, state2)

    def goal_test(self, state):
        """Igaz értékkel tér vissza, ha az adott állapot egy cél állapot.
        Az alapértelmezett metódus összehasonlítja az állapotot a self.goal-al,
        vagy ellenőrzi a self.goal állapotát, ha az egy lista, a konstruktorban megadottak szerint.
        A módszer felülírása szükséges lehet, ha nem elegendő egyetlen self.goal összehasonlítása."""
        if isinstance(self.goal, list):
            for s in self.goal:
                if s==state:
                    return True

            return False
        else:
            return state == self.goal

def heuristic_calc_second_to_last_used(Problem, State):
    if Problem.goal_test(State):
        return 0
    c = 0
    poles = State.split("_")
    c += len(poles[-2])
    return c + 1

t = torony(3, 4,"_1234_")
#t = torony(3, 3, "123__")

print( AStar(t, 10000).path() )
#print(SimilarityCalc(t, "123__"))
