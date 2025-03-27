from Base.Search import *
from NQueens import NQueens

def sort_by_heur(items):
    """Válasszuk mindig a lehető legnagyobb indexű sort"""
    return sorted(items, key=lambda x: sum(x.state))

def sort_by_number_of_twos(items):
    return sorted(items, key=lambda x: nrOfX(x.state, 2))

def distinctElems(matrix):
    distincts = set()
    for elem in matrix:
        if elem not in distincts and elem != -1:
            distincts.add(elem)
    return distincts

def nrOfSames(matrix):
    count = 0
    for elem in distinctElems(matrix):
        count += nrOfX(matrix, elem)
    return count

def sort_by_number_of_sames(items):
    return sorted(items, key=lambda x: nrOfSames(x.state))

def nrOfX(matrix, X):
    count = 0
    for element in matrix:
        if element == X:
            count +=1
    return count

nq4 = NQueens(4)


limit = 5
steps = 0
discovered = 0
notFound = 0
for i in range(limit):
    te = trial_error_with_stepcount(nq4)
    if te[1] != -1:
        steps += te[1]
        discovered += te[2]
        continue
    notFound += 1
avgSteps = steps / max( ( limit - notFound ), 1 )
avgDiscovered = discovered / max( ( limit - notFound ), 1 )
print( "Average number of steps needed for trial-error search(", limit, " tries) : ", avgSteps.__int__(),
       "\nAverage number of nodes discovered by trial-error search(", limit, " tries) : ", avgDiscovered.__int__(),
       "\nNumber of times trial-error search didn't find the goal(", limit, " tries) : ", notFound, "\n")

b = breadth_first_tree_search_with_stepcount(nq4)
print( "Number of steps needed for width search: ", b[1],
       "\nNumber of nodes discovered by width search: ", b[2], "\n")
d = depth_first_graph_search_with_stepcount(nq4)
print( "Number of steps needed for depth search: ", d[1],
       "\nNumber of nodes discovered by depth search: ", d[2], "\n")

a1 = astar_search_with_stepcount(nq4, sort_by_number_of_sames)
print( "Number of steps needed for astar search(nrOfSames heuristic): ", a1[1],
       "\nNumber of nodes discovered by astar search: ", a1[2], "\n")


"""Ez valójában egy kicsit lassabb mélységi, mivel minden kereső csak a olyan operátorokat választ, melyek
nem okoznak sorban ütést, tehát csak a keresztbe-irányt kell vizsgálni, a keresztbe-ütés meg elég ritka"""
a2 = astar_search_with_stepcount(nq4, sort_by_number_of_twos)
print( "Number of steps needed for astar search(nrOfTwos heuristic): ", a2[1],
       "\nNumber of nodes discovered by astar search: ", a2[2], "\n")
