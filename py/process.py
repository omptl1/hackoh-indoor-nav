# Takes an input txt file and converts it to this form: [['start', 'wall'], ['space', 'goal']]
def convert_input_text(filename):
    # Define mapping of characters to types
    char_to_type = {
        'o': 'wall',
        ' ': 'space',
        'G': 'goal',
        '*': 'start'
    }

    # Initialize the 2D array
    grid = []

    with open(filename, 'r') as file:
        for line in file:
            row = []
            for char in line.strip():
                if char in char_to_type:
                    row.append(char_to_type[char])
                else:
                    # Handle unknown characters (optional)
                    row.append('unknown')
            grid.append(row)

    return grid
    
    
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
    for element in inputArray:
        if element[2] == 'start':
            return element
        
    return []
    
# Determines the heuristic value of the current point from the goal state
def heuristic(inputArray):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0