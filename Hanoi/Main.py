from Base.WidthSearch import widthSearch
from Base.hill_climbing import hill_climbing, heuristic_calc_empty_jar, heuristic_zero, heuristic_calc_first_not_on_second
from Base.trial_error import trial_error
from Hanoi import Hanoi

h = Hanoi(2)

#print(h.goal)

#print(trial_error(h).solution())

#print(hill_climbing(h, heuristic_calc_not_on_first()).solution)
#print(hill_climbing(h, heuristic_calc_empty_jar).solution)

#print( widthSearch(h, 2000) )
print( hill_climbing(h, heuristic_calc_first_not_on_second).solution )
#print( hill_climbing(h, heuristic_zero).solution )