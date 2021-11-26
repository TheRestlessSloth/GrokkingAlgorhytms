from collections import deque

#1 exercise
graph = {}
costs = {}
parents = {}
processed = []

graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["d"] = 7
graph["b"]["a"] = 8

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

infinity = float("inf")
costs["a"] = 5
costs["b"] = 2
costs["fin"] = infinity
costs["c"] = infinity
costs["d"] = infinity

parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#print(graph)
print(parents)
print(costs)
#print(processed)

#2 exercise

graph = {}
costs = {}
parents = {}
processed = []

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["fin"] = 30
graph["b"]["c"] = 1

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity


parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print()
print(parents)
print(costs)

#3 exercise

graph = {}
costs = {}
parents = {}
processed = []

graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["b"] = 2

graph["b"] = {}
graph["b"]["fin"] = 2
graph["b"]["c"] = 2

graph["c"] = {}
graph["c"]["a"] = -1
graph["c"]["fin"] = 2

graph["fin"] = {}

costs["a"] = 2
costs["b"] = 2
costs["c"] = infinity
costs["fin"] = infinity


parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["fin"] = None

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print()
print(parents)
print(costs)

#algo bellman-ford
graph = {}
costs = {}
parents = {}
processed = []

graph["a"] = {}
graph["a"]["b"] = -1
graph["a"]["c"] = 4

graph["b"] = {}
graph["b"]["c"] = 3
graph["b"]["d"] = 2
graph["b"]["e"] = 2

graph["c"] = {}

graph["d"] = {}
graph["d"]["b"] = 1
graph["d"]["c"] = 5

graph["e"] = {}
graph["e"]["d"] = -3

costs["b"] = 2
costs["c"] = 2
costs["e"] = infinity
costs["d"] = infinity

parents["b"] = "b"
parents["c"] = "c"
parents["e"] = None
parents["d"] = None

class Graph: 

	def __init__(self, vertices): 
		self.V = vertices # No. of vertices 
		self.graph = [] # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 
		
	# utility function used to print the solution 
	def printArr(self, dist): 
		print("Vertex Distance from Source") 
		for i in range(self.V): 
			print("% d \t\t % d" % (i, dist[i])) 
	
	# The main function that finds shortest distances from src to 
	# all other vertices using Bellman-Ford algorithm. The function 
	# also detects negative weight cycle 
	def BellmanFord(self, src): 
		# Step 1: Initialize distances from src to all other vertices 
		# as INFINITE 
		dist = [float("Inf")] * self.V 
		dist[src] = 0

		# Step 2: Relax all edges |V| - 1 times. A simple shortest 
		# path from src to any other vertex can have at-most |V| - 1 
		# edges 
		for i in range(self.V - 1): 
			# Update dist value and parent index of the adjacent vertices of 
			# the picked vertex. Consider only those vertices which are still in 
			# queue 
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						dist[v] = dist[u] + w 

		# Step 3: check for negative-weight cycles. The above step 
		# guarantees shortest distances if graph doesn't contain 
		# negative weight cycle. If we get a shorter path, then there 
		# is a cycle. 

		for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						print("Graph contains negative weight cycle")
						return
						
		# print all distance 
		self.printArr(dist) 

g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 

# Print the solution 
g.BellmanFord(0) 

# This code is contributed by Neelam Yadav