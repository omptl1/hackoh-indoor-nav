from gtts import gTTS
import os

def parse_directions_from_file(file_path):
    direction_mapping = {
        'n': 'north',
        's': 'south',
        'e': 'east',
        'w': 'west',
    }

    current_direction = None
    stride_count = 0
    directions = []

    with open(file_path, 'r') as file:
        abbreviated_directions = file.read().replace('\n', '')  # Remove newline characters

    for direction in abbreviated_directions:
        if direction in direction_mapping:  # Add this check to ignore invalid characters
            if current_direction != direction:
                if current_direction and stride_count > 0:
                    if stride_count == 1:
                        directions.append(f"Face {direction_mapping[current_direction]}. Go straight for {stride_count} stride.\n")
                    else:
                        directions.append(f"Face {direction_mapping[current_direction]}. Go straight for {stride_count} strides.\n")
                current_direction = direction
                stride_count = 1
            else:
                stride_count += 1

    if current_direction and stride_count > 0:
        if stride_count == 1:
            directions.append(f"Face {direction_mapping[current_direction]}. Go straight for {stride_count} stride.\n")
        else:
            directions.append(f"Face {direction_mapping[current_direction]}. Go straight for {stride_count} strides.\n")

    directions.append("You have reached your destination.")

    return ''.join(directions)

file_path = 'example_maze_output.txt'
parsed_directions = parse_directions_from_file(file_path)
print(parsed_directions)

language = 'en'
voice = 'comical'  # You need to check available voices in the gTTS library for a funny voice
myobj = gTTS(text=parsed_directions, lang=language, tld= 'com.au', slow=False)
myobj.save("dir.mp3")
