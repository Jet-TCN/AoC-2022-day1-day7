# Declare an empty list in which to store out input data
input_data = []

# Open our input.txt file to be read
with open('input.txt') as file:
    input_data = [l.splitlines()[0] for l in file]

# Create a master list, in which more lists will be stored, populated with one empty list element initially
master_list = [[]]

# Iterate over our input data, creating a new list each time a whitespace is encountered
# We will need a counter to keep track of which list we are accessing
list_index_counter = 0

for line in input_data:
    # If the line is empty, we will insert a new list into master_list
    if line == '':
        master_list.append([])              # Append empty list element
        list_index_counter += 1             # Increment the counter
    # Otherwise, we will cast the string to an integer and append to the list at the current index
    else:
        master_list[list_index_counter].append(int(line))
        
# Now we sum each element in the master list, we can use a list comprehension here
master_list = [sum(sublist) for sublist in master_list]

# Part one
# Find the element with the highest value in the master list
print(max(master_list))

# Part two
# Sort the master list in ascending order
master_list.sort(reverse=True)

# Print out the sum of the first three elements
print(sum(master_list[0:2]))
