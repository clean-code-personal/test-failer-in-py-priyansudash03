
# def print_color_map():
#     major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
#     minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
#     len_major = [len(i) for i in major_colors ] 
#     len_minor = [len(i) for i in minor_colors ]
#     total_color = len(major_colors)*len(minor_colors)
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             print(f'{i * 5 + j} | {major} | {minor}')
#     return len(major_colors) * len(minor_colors)


# result = print_color_map()
# assert(result == 25)
# print("All is well (maybe!)\n")


def compute_index(i, j, num_minor_colors):
    """Computes the index based on the major and minor color combination."""
    return i * num_minor_colors + j

def format_row(i, major, minor, num_minor_colors):
    """Formats a single row as a string."""
    index = compute_index(i, 0, num_minor_colors) + j  # Compute index for this row
    return f'{index} | {major} | {minor}'

def generate_color_map():
    """Generates the full color map and returns it as a list of strings."""
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(format_row(i, major, minor, len(minor_colors)))
    return color_map

# Testing the functions
def test_compute_index():
    # Intentionally changing the expected result to make it fail (i=1, j=2, num_minor_colors=5)
    assert compute_index(1, 2, 5) == 8, "compute_index failed"  # 7 is correct, 8 will make it fail
    
def test_format_row():
    # Intentionally changing the expected result to make it fail
    result = format_row(1, "Red", "Green", 5)
    expected = "8 | Red | Green"  # We intentionally make it incorrect
    assert result == expected, f"format_row failed: expected {expected}, got {result}"

def test_generate_color_map():
    # Intentionally causing the test to fail by expecting 26 rows instead of 25
    color_map = generate_color_map()
    assert len(color_map) == 26, f"generate_color_map failed: expected 26 rows, got {len(color_map)}"  # This will fail

# Run the tests
test_compute_index()
test_format_row()
test_generate_color_map()

# Running the color map function (prints the map)
def print_color_map():
    color_map = generate_color_map()
    for row in color_map:
        print(row)
    return len(color_map)

# Final assertion check (intentionally incorrect)
result = print_color_map()
assert(result == 26), f"Test failed. Expected 26 rows, got {result}"  # This is intentional to make it fail
print("All is well (maybe!)\n")
