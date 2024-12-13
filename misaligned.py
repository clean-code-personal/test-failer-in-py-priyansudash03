color_map = []

def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

def display_color_map(color_map):
    for entry in color_map:
        print(entry)

generate_color_map()
display_color_map(color_map)

assert(color_map[-1] == '24 | Violet | Slate'), "The last entry does not match the expected value"
assert(len(color_map) == 25), "The total number of entries in the color map should be 25"
assert(all(entry.find('|', entry.find('|') + 1) - entry.find('|') - 1 == 6 for entry in color_map)), "Major color alignment is incorrect"
assert(all(len(entry.split('|')[2]) == 6 for entry in color_map)), "Minor color alignment is incorrect"

print("All is well (maybe!)\n")
