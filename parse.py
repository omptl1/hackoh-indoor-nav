from gtts import gTTS 
import os 



def parse_directions(abbreviated_directions):
    direction_mapping = {
        'n': 'north',
        's': 'south',
        'e': 'east',
        'w': 'west',
    }

    current_direction = None
    stride_count = 0
    directions = []

    for direction in abbreviated_directions:
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

abbreviated_directions = "nnnnssssew"
parsed_directions = parse_directions(abbreviated_directions)
print(parsed_directions)


language = 'en'
myobj = gTTS(text=parsed_directions, lang=language, slow=False) 
myobj.save("dir.mp3")