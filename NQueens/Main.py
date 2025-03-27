from Base.Search import breadth_first_tree_search, breadth_first_tree_search_with_stepcount, \
    depth_first_graph_search_with_stepcount, astar_search, astar_search_with_stepcount, trial_error_with_stepcount
from NQueens import NQueens

nq4 = NQueens(4)

b = breadth_first_tree_search_with_stepcount(nq4)
print( "Number of steps needed for width search: ", b[1],
       "\nNumber of node discovered by width search: ", b[2], "\n")
d = depth_first_graph_search_with_stepcount(nq4)
print( "Number of steps needed for depth search: ", d[1],
       "\nNumber of node discovered by depth search: ", d[2], "\n")
te = trial_error_with_stepcount(nq4)
print( "Number of steps needed for trial-error search: ", te[1],
       "\nNumber of node discovered by trial-error search: ", te[2], "\n")

def sort_by_heur(items):
    """Válasszuk mindig a lehető legnagyobb indexű sort"""
    return sorted(items, key=lambda x: sum(x.state))

def sort_by_number_of_twos(items):
    return sorted(items, key=lambda x: nrOfX(x.state, 2))

def nrOfX(matrix, X):
    count = 0
    for element in matrix:
        if element == X:
            count +=1
    return count

a = astar_search_with_stepcount(nq4, sort_by_number_of_twos)
print( "Number of steps needed for astar search(nrOfTwos heuristic): ", a[1],
       "\nNumber of node discovered by astar search: ", a[2], "\n")