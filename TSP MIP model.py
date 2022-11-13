import os
import sys
import vrplot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np
import pandas as pd
import read_files
import moviepy.editor as mp

n_customers = 9
figsize = (8,8)
file_name = 'fa_2'

a = read_files.Coords*0.002
coords = a.tolist()
nodes = read_files.T
depot, customer_nodes = nodes[0], nodes[1:]

#Optimal solution
min_tour, cost = vrplot.opt.mip.get_solution_tsp(coords, nodes)

_ = vrplot.static.construct_route(
    min_tour,
    coords,
    nodes,
    label="Optimal solution",
    figsize=figsize
)

#Nearest neighbour
random_starting_node = np.random.randint(len(nodes))

nn_route, nn_sol_steps = vrplot.opt.heuristic.get_route_nearest_neighborhood(
    customer_nodes,
    coords,
    start=random_starting_node)

print(f"Starting from: {random_starting_node} - Route: {nn_route}")

# vrplot.animated.show_solutions(
#     nn_sol_steps,
#     coords,
#     nodes,
#     figsize=figsize,
#     file_name=file_name)
#
# clip = mp.VideoFileClip(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".gif")
# clip.write_videofile(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".mp4")

#Farthest Addition
fa_route, fa_sol_steps = vrplot.opt.heuristic.get_route_farthest_addition(
    customer_nodes,
    coords,
    start=random_starting_node)

print(f"Starting from: {random_starting_node} - Route: {fa_route}")

vrplot.animated.show_solutions(
    fa_sol_steps,
    coords,
    nodes,
    figsize=figsize,
    file_name=file_name)

# clip = mp.VideoFileClip(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".gif")
# clip.write_videofile(r"C://Users/joepl/PycharmProjects/BEP_try_2.0/Animations/"+file_name+".mp4")
