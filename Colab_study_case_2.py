import itertools

import vrplot

n = 4 # n. of customers
k = 3 # n. of vehicles
customers = ['🧍'] * n
separations = ["┃"] * (k - 1) # 3 vehicles = 2 separations
symbols = customers + separations

# Transformation to set exclude duplicate permutations
ways = set(itertools.permutations(symbols))


print(f"k={4} vehicles can pick up n={n} customers in {len(ways)} different ways.\n")
print("# Ways (vehicles are separated by '|'):")
vrplot.opt.complexity.enumerate_ways(ways)

############################

