from ownHanoiHeur.SimilarityCalc import SimilarityCalc


class Node:
    """Csomópont a kereső fában.
       Tartalmaz egy mutatót a szülőre (a csomópontra, amelynek ez az utódja) és a
       csomópont aktuális állapotára.
       Egy állapotot két útvonalon érünk el, akkor két azonos állapotú csomópont van.
       Tartalmazza azt a műveletet is, amely ebbe az állapotba juttatott minket,
       valamint a csomópont eléréséhez szükséges teljes path_cost (más néven g) értéket.
       Más függvények hozzáadhatnak egy f és h értéket;
       lásd a best_first_graph_search és az astar_search leírását az
       f és h értékek kezelésének magyarázatához."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Node osztály konstruktora."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        """Speciális metódus mely az objektum string állapotát definiálja"""
        #return "<Node {}, {}, {}, {}>".format(self.state, self.parent, self.action, self.path_cost)
        """str = "\n"
        for ch in self.state:
            str += "\n" + ch
        return str"""
        #return "<Node {}>".format(self.state)
        return "<{}>".format(self.state)

    def __lt__(self, node):
        """Speciálist metódus mely definiálja hogy az adott Node objektum
        mikor kisebb e egy másik Node objektumnál"""
        return self.path_cost < node.path_cost

    def __eq__(self, other):
        """Speciálist metódus mely definiálja hogy az adott Node objektum
        mikor egyenlő egy másik Node objektummal"""
        return isinstance(other, Node) and self.path_cost == other.path_cost and self.state == other.state

    def __hash__(self):
        """Speciális metódus mely definiálja hogy egy adott Node objektum
        hash állapotát definiálja"""
        return hash(self.state)

    def child_node(self, problem, action):
        """A következő csomópont az adott probléma és adott operátor szerinti elkészítése és visszaadása"""
        next_state = problem.result(self.state, action)
        next_node = Node(state = next_state,
                         parent = self,
                         action = action,
                         path_cost = self.path_cost + SimilarityCalc(problem, next_state) )
        """ + heuristic_calc_second_to_last_used(problem, next_state) ) """
        return next_node

    def expand(self, problem):
        """A csomópontból egy lépésben eléhető csomópontok visszadása"""
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def solution(self):
        """A gyökér csomóponttól a csompontig terjedő műveletek listájának visszaadása"""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """A gyökér csomópontól a csompontig vezető utvonal csomópontjainak listája"""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
