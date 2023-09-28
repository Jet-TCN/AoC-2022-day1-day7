input_string = "SPLIT"

with open('input.txt') as file:
    for l in file.readlines():
        input_string += l if l != '\n' else "SPLIT"
    
data = [[int(x) for x in elves.split('\n')[0:-1]] for elves in input_string.split("SPLIT")]
cals = [sum(elves) for elves in data]

# Part one
print(max(cals))

# Part two
cals.sort(reverse=True)
print(sum([cals[0], cals[1], cals[2]]))
