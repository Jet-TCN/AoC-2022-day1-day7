# 4 for part 1, 19 for part 2
MARKER_LENGTH = 14

with open('input') as file:
    input_data = file.read()

for pos in range(len(input_data)):
    chars = set(input_data[pos:pos+MARKER_LENGTH])
    if len(chars) == MARKER_LENGTH:
        print(pos+MARKER_LENGTH)
        break
