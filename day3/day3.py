# Set priorities
priority = {chr(x): x-96 for x in range(97, 123)}
priority.update({chr(x): x-38 for x in range(65, 91)})

input_data = []

with open('input.txt') as file:
    input_data = [l.strip() for l in file]

# Part one
def part1() -> int:
    rucksack = []

    for comps in input_data:
        compartment_one, compartment_two = comps[:len(comps)//2], comps[len(comps)//2:]
        rucksack.append([compartment_one, compartment_two])

    priority_sum = 0

    for compartments in rucksack:
        get_intersection = set(compartments[0]).intersection(compartments[1])
        priority_sum += sum([priority[item] for item in get_intersection])

    return priority_sum

# Part two
def part2() -> int:
    groups = [input_data[x:x+3] for x in range(0, len(input_data), 3)]
    priority_sum = 0
    
    for compartments in groups:
        get_intersection = set(compartments[0]).intersection(compartments[1], compartments[2])
        priority_sum += sum([priority[item] for item in get_intersection])

    return priority_sum
