def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    color_map = []
    
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((i * 5 + j, major, minor)) #it will give error if the size of list changes
    
    return color_map

def print_color_map(color_map):
    for row in color_map:
        print(f'{row[0]} | {row[1]} | {row[2]}')


color_map = generate_color_map()


assert len(color_map) == 20, f"Expected 25 rows, but got {len(color_map)}"
assert color_map[4] == (4, "White", "Blue"), f"First row mismatch: {color_map[4]}"



print_color_map(color_map)

print("All is well (maybe!)\n")
