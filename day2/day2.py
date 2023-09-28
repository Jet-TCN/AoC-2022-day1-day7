RPS = {'X': 1, 'Y': 2, 'Z': 3,
       'A': 1, 'B': 2, 'C': 3}

input_data = []

with open('input2.txt') as file:
    input_data = [l.strip() for l in file]


# PART 1
def part1() -> int:
    score = 0
    for battle in input_data:
        opponent = battle[0]
        you = battle[-1]

        score += RPS[you]

        if RPS[opponent] == RPS[you]:
            score += 3
            continue

        versus = RPS[opponent] - RPS[you]
        if versus % 3 == 2:
            score += 6

    return score

# PART 2
def part2() -> int:
    score = 0
    for battle in input_data:
        opponent = battle[0]
        outcome = battle[-1]
        
        if outcome == 'Y':
            score += 3 + RPS[opponent]

        elif outcome == 'X':
            score += 1 + (RPS[opponent] + 1) % 3

        elif outcome == 'Z':
            score += 7 + RPS[opponent] % 3

    return score


print(part2())
