import os
import sys
sys.path.append(os.path.join(os.getcwd(), "vrplot"))
import vrplot

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
sns.set_style("whitegrid")

import numpy as np
np.random.seed(42)

import itertools

n_customers = 8
figsize = (5,5)

coords = vrplot.util.get_random_nodes(n_customers)
nodes = list(range(n_customers + 1))
depot, customer_nodes = nodes[0], nodes[1:]

# Eliminate symmetrical routes
routes = set()
for p in itertools.permutations(customer_nodes):
    if p not in routes and tuple(reversed(p)) not in routes:
        routes.add(p)

#Solution format = (route, ) where route = (depot, customer nodes, depot)
tsp_solutions = [( (depot,) + route + (depot,), ) for route in routes]
tsp_sol_costs = [vrplot.util.get_total_cost(s, coords) for s in tsp_solutions]

# plt.scatter(np.arange(len(tsp_solutions)), tsp_sol_costs, s=1, alpha=0.5)
# plt.title(
#     f"Costs for all {len(tsp_solutions):,} solutions for a "
#     f"\n{n_customers}-customer ({n_customers+1}-node) symmetrical TSP")
# plt.ylabel("Solution cost")
# plt.xlabel("Solution")

tsp_sorted_cost_sol = sorted(
    zip(tsp_sol_costs, tsp_solutions),
    key=lambda s:s[0],
    reverse=True)

tsp_sorted_cost, tsp_sorted_sol = zip(*tsp_sorted_cost_sol)
tsp_best_sol_cost, tsp_best_sol = tsp_sorted_cost_sol[-1]

print(f"Best solution: {tsp_best_sol[0]}- (Cost: {tsp_best_sol_cost:6.2f})")

vrplot.animated.show_solutions(
    tsp_sorted_sol[-50:],
    coords,
    nodes,
    figsize=figsize)

