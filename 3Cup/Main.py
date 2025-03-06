import queue
from tkinter import Listbox

from Base.Node import Node
from Base.WidthSearch import widthSearch
from Base.hill_climbing import hill_climbing, heuristic_calc_empty_jar
from Cup3 import Cup3

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

#print( widthSearch(CupProblem, (5,0,0)) )
print( hill_climbing( CupProblem, heuristic_calc_empty_jar ).solution )