import process
import search

# Gets the input array of coordinates and type
inputArray = process.convert_input_text('example_maze_input.txt')

# Returns the output string of directions
outputString = search.aStarSearch(inputArray)


