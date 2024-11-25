import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["F1", "F2", "D", "A", "B"]
G.add_nodes_from(nodes)

# Add edges with capacities and costs
edges = [
    ("F1", "A", {"cost": 15, "capacity": 300}),
    ("F1", "B", {"cost": 20, "capacity": 300}),
    ("F1", "D", {"cost": 10, "capacity": 300}),
    ("F2", "A", {"cost": 35, "capacity": 500}),
    ("F2", "B", {"cost": 25, "capacity": 500}),
    ("F2", "D", {"cost": 10, "capacity": 500}),
    ("D", "A", {"cost": 8, "capacity": float('inf')}),
    ("D", "B", {"cost": 12, "capacity": float('inf')}),
]

G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # Position the nodes using the spring layout
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Add edge labels for costs and capacities
edge_labels = {(u, v): f"Cost: {d['cost']}, Cap: {d['capacity']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Flow Network for Question 2")
plt.axis("off")
plt.show()
