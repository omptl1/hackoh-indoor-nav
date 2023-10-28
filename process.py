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
                    row.append('?')
            grid.append(row)

    return grid
    
    
# Takes in a current point, and it returns a list of triples, (successor, action, stepCost)
def getSuccessors(self, inputArray):
    successors = []
    if inputArray[self[0] + 1][self[1]] == 'space' or inputArray[self[0] + 1][self[1]] == 'goal':
        successors.append(((self[0] + 1, self[1]), 's', 1))

    if self[0] > 0:
        if inputArray[self[0] - 1][self[1]] == 'space' or inputArray[self[0] - 1][self[1]] == 'goal':
            successors.append(((self[0] - 1, self[1]), 'n', 1))
    
    if inputArray[self[0]][self[1] + 1] == 'space' or inputArray[self[0]][self[1] + 1] == 'goal':
        successors.append(((self[0], self[1] + 1), 'e', 1))

    if self[1] > 0:
        if inputArray[self[0]][self[1] - 1] == 'space' or inputArray[self[0]][self[1] - 1] == 'goal':
            successors.append(((self[0], self[1] - 1), 'w', 1))

    return successors
        
# Determines the start state and returns the triple
def getStartState(inputArray):
    rowCount = 0
    for row in inputArray:
        columnCount = 0
        for element in row:
            if element == 'start':
                return (rowCount, columnCount)
            columnCount += 1
        rowCount += 1
        
    return []
    
# Determines the heuristic value of the current point from the goal state
def heuristic(inputPoint, inputArray):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic uses Manhattan distance.
    """

    # Extract the current point from the input array
    current_point = inputPoint

    # Find the goal point in the input array
    goal_point = None
    for element in inputArray:
        if element[2] == 'goal':
            goal_point = element[:2]
            break

    # If no goal point was found, raise an error
    if goal_point is None:
        raise ValueError("No goal point found in inputArray")

    # Calculate the Manhattan distance between the current point and the goal point
    return abs(current_point[0] - goal_point[0]) + abs(current_point[1] - goal_point[1])