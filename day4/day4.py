input_data = []

with open('input.txt') as file:
    input_data = [l.strip() for l in file]

def part1() -> int:
    pair_sum = 0
    for task in input_data:
        current_task = [[int(task_range) for task_range in single.split('-')] for single in task.split(",")]
        current_pairs = [[x for x in range(current_task[0][0], current_task[0][1]+1)],[y for y in range(current_task[1][0], current_task[1][1]+1)]]
        if set(current_pairs[0]).issubset(current_pairs[1]) or set(current_pairs[1]).issubset(current_pairs[0]):
            pair_sum+=1
    return pair_sum


def part2() -> int:
    overlap_pair = 0
    for task in input_data:
        current_task = [[int(task_range) for task_range in single.split('-')] for single in task.split(",")]
        current_pairs = [[x for x in range(current_task[0][0], current_task[0][1]+1)],[y for y in range(current_task[1][0], current_task[1][1]+1)]]
        if set(current_pairs[0]).intersection(current_pairs[1]):
            overlap_pair+=1
    return overlap_pair
