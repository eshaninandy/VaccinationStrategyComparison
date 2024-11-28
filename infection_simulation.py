# The code belongs to Eshani Nandy.
# No section of the code was borrowed from any sources, any similarity is purely coincidental

import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

# Parameters
population_size = 1000            # Number of nodes or individuals in a population
initial_infected = 20             # Initially infect # nodes to start the infection
D = 5                             # Infectious period
k = 6                             # Average degree of node given we start with 3 connections for every new node
R0 = 5.08                         # Basic Reproduction Number (Delta variant)
infection_prob = R0/ (D*k)        # Infection probability based on Delta R0
recovery_prob = infection_prob/R0 # Recovery probability
death_prob = 0.01                 # Death probability
time_steps = 100                  # Number of times simulation runs


# Create the network through a random graph
graph = nx.barabasi_albert_graph(population_size, 3)

global total_vaccinated, total_deceased
total_vaccinated = 0
total_deceased = 0
time_series = {
    "susceptible": [],
    "infected": [],
    "recovered": [],
    "dead": []
}

# Initialize node states
for node in graph.nodes():
    graph.nodes[node]['state'] = 0  # Reset to Susceptible

# Infect initial nodes
initial_infected_nodes = random.sample(list(graph.nodes()), initial_infected)
for node in initial_infected_nodes:
    graph.nodes[node]['state'] = 1  # Set initial infected

# Function to spread infection and update states
def spread_infection():
    new_infections = []
    new_recoveries = []
    new_deaths = []
    global total_deceased

    for node in graph.nodes():
        if graph.nodes[node]['state'] == 1:  # If node is infected
            # Try to infect susceptible neighbors
            for neighbor in graph.neighbors(node):
                if graph.nodes[neighbor]['state'] == 0 and random.random() < infection_prob:
                    new_infections.append(neighbor)
            # Recovery or death outcome
            if random.random() < recovery_prob:
                new_recoveries.append(node)
            elif random.random() < death_prob:
                new_deaths.append(node)

    # Update states for new infections, recoveries, and deaths
    for node in new_infections:
        graph.nodes[node]['state'] = 1
    for node in new_recoveries:
        graph.nodes[node]['state'] = 2
    for node in new_deaths:
        graph.nodes[node]['state'] = 3
        total_deceased+=1

# Color map for visualization
def get_color_map():
    color_map = []
    for node in graph.nodes():
        if graph.nodes[node]['state'] == 0:
            color_map.append('yellow')  # Susceptible
        elif graph.nodes[node]['state'] == 1:
            color_map.append('red')    # Infected
        elif graph.nodes[node]['state'] == 2:
            color_map.append('blue')   # Recovered
        elif graph.nodes[node]['state'] == 3:
            color_map.append('grey')  # Dead
        elif graph.nodes[node]['state'] == 4:
            color_map.append('green') # Vaccinated
    return color_map

# Set up animation
fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    ax.clear()
    spread_infection()
    color_map = get_color_map()
    nx.draw(graph, node_size=50, node_color=color_map, ax=ax, with_labels=False)
    ax.set_title(f"Time Step {frame + 1}  Infection Simulation")

    # Calculate and print metrics
    global time_series
    susceptible_count = sum(1 for n in graph.nodes if graph.nodes[n]['state'] == 0)
    infected_count = sum(1 for n in graph.nodes if graph.nodes[n]['state'] == 1)
    recovered_count = sum(1 for n in graph.nodes if graph.nodes[n]['state'] == 2)
    immune_count = recovered_count
    herd_immunity_threshold = 1 - (1 / R0)  # For R0 = 5.08
    immune_percentage = immune_count/population_size

    if immune_percentage >= herd_immunity_threshold:
        print(f"No vaccination: Herd immunity achieved at time step {frame+1}!")

    time_series["susceptible"].append(susceptible_count)
    time_series["infected"].append(infected_count)
    time_series["recovered"].append(recovered_count)
    time_series["dead"].append(total_deceased)

    # Display metrics on the graph with adjusted coordinates
    x_text_pos, y_text_start = 0.85, 0.9  # Adjusted x and starting y position
    y_text_step = 0.05                    # Space between lines
    
    ax.text(x_text_pos, y_text_start, f"Susceptible %: {susceptible_count/population_size:.2%}", transform=ax.transAxes, 
            fontsize=10, verticalalignment='top')
    ax.text(x_text_pos, y_text_start - y_text_step, f"Infected %: {infected_count/population_size:.2%}", transform=ax.transAxes, 
            fontsize=10, verticalalignment='top')
    ax.text(x_text_pos, y_text_start - 2 * y_text_step, f"Recovered %: {recovered_count/population_size:.2%}", transform=ax.transAxes, 
            fontsize=10, verticalalignment='top')
    ax.text(x_text_pos, y_text_start - 3 * y_text_step, f"Dead %: {total_deceased/population_size:.2%}", transform=ax.transAxes, 
            fontsize=10, verticalalignment='top')
    ax.text(x_text_pos, y_text_start - 4 * y_text_step, f"Population Immunity %: {immune_count / population_size:.2%}", 
            transform=ax.transAxes, fontsize=10, verticalalignment='top')
    ax.text(x_text_pos, y_text_start - 6 * y_text_step, 
            f"Herd Immunity Threshold: {herd_immunity_threshold:.2%}", transform=ax.transAxes, 
            fontsize=8, verticalalignment='top')
        
    # Set axis limits and layout
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

# Plotting after the animation
def plot_time_series():
    plt.figure(figsize=(10, 6))
    plt.plot(time_series["susceptible"], label="Susceptible", color="yellow")
    plt.plot(time_series["infected"], label="Infected", color="red")
    plt.plot(time_series["recovered"], label="Recovered", color="blue")
    plt.plot(time_series["dead"], label = "Dead", color="grey" )
    plt.title("COVID-19 Simulation Dynamics")
    plt.xlabel("Time Step")
    plt.ylabel("Number of Individuals")
    plt.legend()
    plt.grid(True)
    plt.savefig("infection_spread.png", dpi=300, format="png")

ani = animation.FuncAnimation(fig, update, frames=time_steps, repeat=False, interval=500)
ani.save('infection_spread.mp4', fps=2)
plot_time_series()
