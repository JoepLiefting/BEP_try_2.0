import itertools
import pandas as pd
from decimal import Decimal
import math
import os
import sys
sys.path.append(os.path.join(os.getcwd(), "vrplot"))
import vrplot
import moviepy.editor as mp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np
np.random.seed(42)


# n = 4 # n. of customers
# k = 3 # n. of vehicles
# customers = ['🧍'] * n
# separations = ["┃"] * (k - 1) # 3 vehicles = 2 separations
# symbols = customers + separations
#
# # Transformation to set exclude duplicate permutations
# ways = set(itertools.permutations(symbols))
#
#
# print(f"k={4} vehicles can pick up n={n} customers in {len(ways)} different ways.\n")
# print("# Ways (vehicles are separated by '|'):")
# vrplot.opt.complexity.enumerate_ways(ways) #vrplot moet import worden

#################################
file_name = 'animation_7'
figsize = (5,5)

n_vehicles = 3
n_customers = 7

# Get a random distribution of nodes
coords = vrplot.util.get_random_nodes(n_customers)
nodes = list(range(n_customers + 1))

# Depot = first node / Customers = remaining nodes
depot, customer_nodes = nodes[0], nodes[1:]

# Plot nodes
# figsize = (5, 5)
# vrplot.static.draw_nodes(coords, nodes, figsize=figsize)

# Get all possible routes
vrp_solutions = vrplot.opt.complexity.get_solution_space(
    customer_nodes,
    depot=depot,
    n_vehicles=n_vehicles)

# Calculate route costs
# vrp_sol_costs = [vrplot.util.get_total_cost(s, coords) for s in vrp_solutions]
#
# # Plot
# plt.scatter(np.arange(len(vrp_sol_costs)), vrp_sol_costs, s=1, alpha=0.5)
# plt.title(
#     f"Costs for all {len(vrp_solutions):,} solutions for "
#     f"\n a {n_customers}-customer and {n_vehicles}-vehicle VRP"
#     " \n(considering distinguishable vehicles)")
#
# plt.ylabel("Solution cost")
# _ = plt.xlabel("Solution")

# vrp_sorted_sol = sorted(
#     vrp_solutions,
#     key=lambda s:vrplot.util.get_total_cost(s, coords),
#     reverse=True)

vrp_solutions_indistinguishable = vrplot.opt.complexity.get_solution_space(
    customer_nodes,
    depot=depot,
    n_vehicles=n_vehicles,
    distinguish_vehicles=False)

#Calculate route costs
vrp_sol_costs = [
    vrplot.util.get_total_cost(s,coords)
    for s in vrp_solutions_indistinguishable]

# #Plot
# n_sols = len(vrp_solutions_indistinguishable)
# plt.scatter(np.arange(n_sols), vrp_sol_costs, s=1, alpha=0.5)
#
# plt.title(
#     f"Costs for all {n_sols:,} solutions for "
#     f"\n a {n_customers}-customer and {n_vehicles}-vehicle VRP"
#     " \n(considering indistinguishable vehicles)")
#
# plt.ylabel("Solution cost")
# _ = plt.xlabel("Solution")

# vrp_sorted_sol = sorted(
#     vrp_solutions_indistinguishable,
#     key=lambda s:vrplot.util.get_total_cost(s, coords),
#     reverse=True)
#
# vrplot.animated.show_solutions(
#     vrp_sorted_sol[-100:],
#     coords,
#     nodes,
#     figsize=figsize,
#     file_name=file_name)
#
#
# clip = mp.VideoFileClip(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".gif")
# clip.write_videofile(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".mp4")

print(coords)