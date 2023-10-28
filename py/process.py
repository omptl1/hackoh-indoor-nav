# Takes an input txt file and converts it to this form: (x, y, type)
def convert_input_txt(filename):
    # Define mapping of characters to types
    char_to_type = {
        '|': 'wall',
        ' ': 'space',
        '.': 'goal',
        'P': 'start'
    }

    # Initialize variables to store the result
    result = []

    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char in char_to_type:
                    result.append((x, y, char_to_type[char]))

    return result
    
    
# Takes in a current point, and it returns a list of triples, (successor, action, stepCost)
def getSuccessors(self, inputArray):
    """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
    util.raiseNotDefined()
   
# Determines the start state and returns the triple
def getStartState(inputArray):
    
    
# Determines the heuristic value of the current point from the goal state
def heuristic(inputArray):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0