import numpy as np

from Base.Node import Node


def hill_climbing(problem, heuristic):
    # kezdő állapot
    state = Node(problem.initial)

    # végtelen ciklus definiálása
    while True:
        # Ha a probléma megoldva akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            return state

        # Az alkalmazható operátorok segítsével
        # gyártsuk le az összes lehetséges utódot
        succesors=state.expand(problem)

        # keresünk egy jobb állapotott a heurisztikának megfelelően
        test_succesors=[]
        for s_test in succesors:
            if heuristic(state.state)>=heuristic(s_test.state):
                test_succesors.append(s_test)

        # Ha nincs jobb állapot
        if len(test_succesors)==0:
            return 'Unsolvable'

        # ha több azonosan jó van akkor random választunk egyet
        state=test_succesors[np.random.randint(0,len(test_succesors))]
        print(state.state)

def heuristic_calc_empty_jar(State):
    if State==(4,0,1) or State == (4,1,0):
        return 0
    c=0
    for i in State:
        if i == 0:
            c+=1
    return c+1

def heuristic_zero(State):
    return 0

def heuristic_calc_first_not_on_second(State):
    if State == len(State) * "3":
        return 0
    c = 0
    if State.find("2") != -1:
        c += State.count("2")
    return c + 1

"""def heuristic_calc_minimal_poles_used(State):
    szamok = len(State)-State.count("_")
    if State.split("_")[-1] == ( i+1 for i in range(szamok) ):
        return 0
    c = 0
    poles = State.split("_")
    for i in range(len(poles)):
        #c += len(poles[i]) + ( szamok - i )
        #c += ( ( szamok - i ) / szamok ) * len( poles[i] )
        #c += szamok - i + len(poles[i])
        #c += ( ( szamok - i ) / szamok ) * ( szamok - i + len(poles[i]) )
    

    return c + 1"""

