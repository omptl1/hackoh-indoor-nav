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
    successors = []
    if inputArray[self[0] + 1][self[1]] == 'space' or inputArray[self[0] + 1][self[1]] == 'goal':
        successors.append(((self[0] + 1, self[1]), 's', 1))

    if inputArray[self[0]] > 0:
        if inputArray[self[0] - 1][self[1]] == 'space' or inputArray[self[0] - 1][self[1]] == 'goal':
            successors.append(((self[0] - 1, self[1]), 'n', 1))
    
    if inputArray[self[0]][self[1] + 1] == 'space' or inputArray[self[0]][self[1] + 1] == 'goal':
        successors.append(((self[0], self[1] + 1), 'e', 1))

    if inputArray[self[1]] > 0:
        if inputArray[self[0]][self[1] - 1] == 'space' or inputArray[self[0]][self[1] - 1] == 'goal':
            successors.append(((self[0], self[1] - 1), 'w', 1))

    return successors
        
# Determines the start state and returns the triple
def getStartState(inputArray):
    inputArray
    
# Determines the heuristic value of the current point from the goal state
def heuristic(inputArray):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0