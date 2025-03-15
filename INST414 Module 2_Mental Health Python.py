# INST414 Module 2: Social Media & Mental Health
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Loading in data from the .dat File on my computers
file_path = "C:\\Users\\MegaN\\Downloads\\XXH2023_YRBS_Data.dat"  # The file path from my device

# Line that reads the .dat file (assuming it's tab- or comma-separated)
with open(file_path, "r") as file:
    lines = file.readlines()

# How the data is processed
edges = []
for line in lines:
    parts = line.strip().split()  # Adjust separator if needed (e.g., `.split(',')`)
    
    if len(parts) == 3:  # Example: source, target, weight
        source, target, weight = parts
        edges.append((source, target, float(weight)))  # Convert weight to float

# Command to create the Graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# How the graph data will be analyzed the Graph (Using: Degree Centrality)
centrality = nx.degree_centrality(G)
print("Node Centrality:", centrality)

# Visualizing the Graph
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
edge_labels = {(e[0], e[1]): e[2] for e in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graph Visualization from .dat File")
plt.show()
