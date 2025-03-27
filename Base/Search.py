from collections import deque

import numpy as np

from Base.Node import Node


def breadth_first_tree_search(problem):
    # kezdő állapot kiolvasása és FIFO sorba helyezése
    frontier = deque([Node(problem.initial)])

    # Amig nem értük el a határt
    while frontier:
        # legszélsőbb elem kiemelése
        node = frontier.popleft()

        # ha cél állapotban vagyunk akkor vége
        if problem.goal_test(node.state):
            return node

        # A kiemelt elemből az összes új állapot legyártása az operátorok segítségével
        frontier.extend(node.expand(problem))
        #print(node.state)

def breadth_first_tree_search_with_stepcount(problem):
    # kezdő állapot kiolvasása és FIFO sorba helyezése
    frontier = deque([Node(problem.initial)])

    steps = 0
    discovered = 0

    # Amig nem értük el a határt
    while frontier:
        # legszélsőbb elem kiemelése
        node = frontier.popleft()

        # ha cél állapotban vagyunk akkor vége
        if problem.goal_test(node.state):
            return node, steps, discovered

        old_size = len(frontier)
        # A kiemelt elemből az összes új állapot legyártása az operátorok segítségével
        frontier.extend(node.expand(problem))
        discovered += len(frontier) - old_size
        steps += 1
        #print(node.state)

def depth_first_graph_search(problem):
    # Kezdő elem verembe helyezése
    frontier = [(Node(problem.initial))]
    # halmaz deklarálása a már bejárt elemekhez
    explored = set()

    # Amig tudunk mélyebre menni
    while frontier:
        # Legfelső elem kiemelése a veremből
        node = frontier.pop()

        # ha cél állapotban vagyunk vége
        if problem.goal_test(node.state):
            return node

        # állapot feljegyzése hogy tudjuk hogy már jártunk itt
        explored.add(node.state)

        # verem bővítése amig benemjárt elemekkel
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
        #print(node.state)

def depth_first_graph_search_with_stepcount(problem):
    # Kezdő elem verembe helyezése
    frontier = [(Node(problem.initial))]
    # halmaz deklarálása a már bejárt elemekhez
    explored = set()

    steps = 0
    discovered = 0

    # Amig tudunk mélyebre menni
    while frontier:
        # Legfelső elem kiemelése a veremből
        node = frontier.pop()

        # ha cél állapotban vagyunk vége
        if problem.goal_test(node.state):
            return node, steps, discovered

        # állapot feljegyzése hogy tudjuk hogy már jártunk itt
        explored.add(node.state)

        # verem bővítése amig benemjárt elemekkel
        old_size = len(frontier)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
        steps += 1
        discovered += len(frontier) - old_size
        #print(node.state)

def best_first_graph_search(problem, f):
    "A best-first kereső olyan keresőfával kereső, mely a legkisebb heurisztikájú nyílt csúcsot választja kiterjesztésre."

    # kezdő állapot létrehozása
    node = Node(problem.initial)
    # prioritásos (valamilyen heurisztika szerint rendezett) sor létrehozása
    frontier = []
    # kezdő állapot felvétele a prioritásos sorba
    frontier.append(node)
    # halmaz létrehozása a már megvizsgál elemekhez
    explored = set()

    # amíg találunk elemet
    while frontier:
        # elem kivétele a verem tetejéről
        node = frontier.pop()

        # ha cél állapotban vagyunk akkor kész
        if problem.goal_test(node.state):
            return node

        # feldolgozott elemek bővítése
        explored.add(node.state)

        # operátorral legyártott gyermek elemek bejárása
        for child in node.expand(problem):
            # ha még nem dolgoztuk fel
            if child.state not in explored and child not in frontier:
                frontier.append(child)

        # Rendezzük a listát (sort) a heurisztikának megfelelően
        frontier = f(frontier)
        #print(node.state)

def best_first_graph_search_with_stepcount(problem, f):
    "A best-first kereső olyan keresőfával kereső, mely a legkisebb heurisztikájú nyílt csúcsot választja kiterjesztésre."

    # kezdő állapot létrehozása
    node = Node(problem.initial)
    # prioritásos (valamilyen heurisztika szerint rendezett) sor létrehozása
    frontier = []
    # kezdő állapot felvétele a prioritásos sorba
    frontier.append(node)
    # halmaz létrehozása a már megvizsgál elemekhez
    explored = set()

    steps = 0
    discovered = 0

    # amíg találunk elemet
    while frontier:
        # elem kivétele a verem tetejéről
        node = frontier.pop()

        # ha cél állapotban vagyunk akkor kész
        if problem.goal_test(node.state):
            return node, steps, discovered

        # feldolgozott elemek bővítése
        explored.add(node.state)

        # operátorral legyártott gyermek elemek bejárása
        for child in node.expand(problem):
            # ha még nem dolgoztuk fel
            old_size = len(frontier)
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            steps += 1
            discovered += len(frontier) - old_size

        # Rendezzük a listát (sort) a heurisztikának megfelelően
        frontier = f(frontier)
        #print(frontier)
        #print(node.state)

def astar_search(problem, f=None):
    """
    Az A*-algoritmus olyan A-algoritmusfajta, mely garantálja az optimális megoldás előállítását.
    h*(n) : az n -ből valamely célcsúcsba jutás optimális költsége.
    g*(n) : a startcsúcsból n -be jutás optimális költsége.
    f*(n)=g*(n)+h*(n) : értelemszerűen a startcsúcsból n -en keresztül valamely célcsúcsba jutás optimális költsége."""
    return best_first_graph_search(problem, f)

def astar_search_with_stepcount(problem, f=None):
    """
    Az A*-algoritmus olyan A-algoritmusfajta, mely garantálja az optimális megoldás előállítását.
    h*(n) : az n -ből valamely célcsúcsba jutás optimális költsége.
    g*(n) : a startcsúcsból n -be jutás optimális költsége.
    f*(n)=g*(n)+h*(n) : értelemszerűen a startcsúcsból n -en keresztül valamely célcsúcsba jutás optimális költsége."""
    return best_first_graph_search_with_stepcount(problem, f)

def trial_error(problem):
    """
    Próba hiba módszer
    """

    # kezdő állapot
    state = Node(problem.initial)

    # végtelen ciklus definiálása
    while True:
        # Ha a probléma megoldva akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            #print('Got it')
            return state

        # Az alkalmazható operátorok segítsével
        # gyártsuk le az összes lehetséges utódot
        succesors=state.expand(problem)

        # Ha nincs új állapot (utód)
        if len(succesors)==0:
            return 'Unsolvable'

        # random választunk egy újat a legyártott utódok közül
        state=succesors[np.random.randint(0,len(succesors))]
        #print(state.state)

def trial_error_with_stepcount(problem):
    """
    Próba hiba módszer
    """

    # kezdő állapot
    state = Node(problem.initial)

    steps = 0
    discovered = 0

    # végtelen ciklus definiálása
    while True:
        # Ha a probléma megoldva akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            #print('Got it')
            #print(state.path())
            return state, steps, discovered

        # Az alkalmazható operátorok segítsével
        # gyártsuk le az összes lehetséges utódot
        succesors=state.expand(problem)
        discovered += len(succesors)

        # Ha nincs új állapot (utód)
        if len(succesors)==0:
            return -1,-1,-1

        # random választunk egy újat a legyártott utódok közül
        state=succesors[np.random.randint(0,len(succesors))]
        steps += 1
        #print(state.state)