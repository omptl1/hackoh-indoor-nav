# Takes an input txt file and converts it to this form: (x, y, type)
def convert_input_txt():
    util.raiseNotDefined()
    
    
# Takes in a current point, and it returns a list of triples, (successor, action, stepCost)
def getSuccessors(self, state):
    """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
    util.raiseNotDefined()
  
# Takes in a current point and returns a boolean of whether valid goal state  
def isGoalState(self, state):
    """
        state: Search state

        Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()
   
# Determines the start state and returns the triple
def getStartState(self):
    """
        Returns the start state for the search problem
    """
    util.raiseNotDefined()
    
# Determines the heuristic value of the current point from the goal state
def heuristic(state):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0