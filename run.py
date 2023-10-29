import process, search, parse

# Gets the input array of coordinates and type
inputArray = process.convert_input_text('example_maze_input.txt')

inputArray = process.surround_image(inputArray)

# Returns the output string of directions
outputArray = search.aStarSearch(inputArray)

# Outputs a string of characters to a file
process.outDirections(outputArray,'example_maze_output.txt')

parse.parse_directions_from_file('example_maze_output.txt')
