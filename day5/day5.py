input_data = []


with open('input') as file:
    input_data = [l.splitlines()[0] for l in file]

# There are two parts to this file, seperated by an empty line
# Thus we must distinguish between the initial conditions and the instructions

initial_conditions = input_data[:input_data.index("")]
stack_instructions = input_data[input_data.index(""):][1:]

# Since the way the crates are arranged resemble how actual stacks work
# The first step is to create stacks that replicate the initial conditions

# Get the amount of stacks to be generated
stacks_to_generate = [int(num) for num in initial_conditions[-1] if num.isdigit()]

# Create a dictionary with stack identifier as key and stack data as value
# We're just going to use a list instead of creating a class
stacks = {key:[] for key in stacks_to_generate}

# Remove unnecessary portions of data, we can discard the final line as it is already interpreted
# Necessary data occurs every 1+4n intervals which can be interpreted as [1::4] in splicing
initial_conditions = [line[1::4] for line in initial_conditions[:-1]]


# Then interpret the rest of the initial conditions to populate our stacks
for data in initial_conditions:
    for position, character in enumerate(data):
        if character.isalpha():
            stacks[position+1].append(character)

# The second step now to interpret the instructions portion of the data, since we already know the format to be:
#   move <amount> from <stack_to_move_from> to <stack_to_move_to>
# As we only require the unknowns everything else can be discarded, infact these occur every 1+2n intervals if split by whitespace
stack_instructions = [[int(x) for x in instructions.split()[1::2]] for instructions in stack_instructions]

# Now we iterate over the instructions and perform them as requested, pushing (appending) and popping from our stacks

for line in stack_instructions:
    for actions in range(line[0]):
        stacks[line[2]].insert(actions, stacks[line[1]].pop(0))

# Now we get the top element of each stack
top_row = [line[0] for line in stacks.values()]

# And output
print("".join(top_row))
