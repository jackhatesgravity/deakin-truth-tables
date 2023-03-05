from prettytable import PrettyTable
from functools import reduce
import itertools, sys, string

### GLOBAL VARIABLES ###

# Honestly, too lazy to type it out
alphabet = list(string.ascii_lowercase)

# Generate all binary permutations for n inputs
n = int(sys.argv[1])
l = list(itertools.product([0, 1], repeat=n))

### HELPER FUNCTIONS ###

# Generates table headers
def generate_headers(table_name):
    table_headers = [alphabet[i] for i in range(n)]
    table_headers.append(table_name)
    return table_headers

# Iterate through a list and perform the given function to each output row
def truth_table(list, func):
    for i in range(len(l)):
        new_row = []
        for j in l[i]:
            new_row.append(j)

        new_row.append(reduce(func, new_row))
        list.add_row(new_row)
    return

### MAIN PROGRAM ###

# Create AND table
t_AND = PrettyTable()
t_AND.field_names = generate_headers("AND")

# Create OR table
t_OR = PrettyTable()
t_OR.field_names = generate_headers("OR")

# Calculate AND truth table
truth_table(t_AND, lambda x, y: x and y)

# Calculate OR truth table
truth_table(t_OR, lambda x, y: x or y)

# Print the results
print("\nAND Truth Table\n", t_AND, "\n")
print("OR Truth Table\n", t_OR, "\n")

# Need to refactor the printing...
# Death to copy paste