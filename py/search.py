# Successor looks like this: [[0, 1, 'start'], 'n']

from collections import deque
import process

# Travels 
def aStarSearch(inputArray):
    # Start node
    startNode = process.getStartState()
    foundGoal = False

    # Adds start to used nodes list
    usedNodes = [startNode]
    
    # Successor nodes that are discovered but not yet visited
    optionNodes = util.PriorityQueue()
    successors = process.getSuccessors(startNode)
    for successor in successors:
        # Adds nodes and their paths, with the cost as the priority queue determiner
        beginPath = [successor[1]]
        successorComplete = (successor, beginPath)
        h_value = process.heuristic(successor[0])
        optionNodes.push(successorComplete, process.getCostOfActions(beginPath) + h_value)

    currentNode, path = startNode, []

    # Searches until there are not options left
    while not foundGoal and optionNodes.count > 0:
        # Gets current node to look at (node with shortest path length)
        currentNode, path = optionNodes.pop()

        # Checks whether the current node has not been used
        if not currentNode[0] in usedNodes:
            # Checks whether goal has been found
            if process.isGoalState(currentNode[0]):
                foundGoal = True

            else:
                # Updates visited nodes and option nodes
                usedNodes.append(currentNode[0])
                successors = process.getSuccessors(currentNode[0])
                for successor in successors:
                    if not successor[0] in usedNodes:
                        # Adds nodes and their paths, with the cost as the priority queue determiner
                        newPath = path + [successor[1]]
                        nextCost = process.getCostOfActions(newPath)
                        successorComplete = (successor, newPath)
                        h_value = process.heuristic(successor[0])
                        optionNodes.push(successorComplete, nextCost + h_value)

    # Checks whether goal has been found
    if not foundGoal:
        return []
    else:
        return path