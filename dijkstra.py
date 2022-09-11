"""
Authored: Aung Naing Oo

Dijkstra's algorithm using priority queue

"""

from queue import PriorityQueue
graph = {
	'A': {'B':2, 'C':4},
	'B':{'A':2, 'C':3, 'D':8},
	'C':{'A':4, 'B':3, 'D':2, 'E':5},
	'D':{'B':8, 'C':2, 'E':11,'F':22},
	'E':{'C':5, 'D':11, 'F':1},
	'F':{'D':22,'E':1}
	}



visited = []
D = {v:float('inf') for v in graph.keys()}      #initialise all nodes to infinity
predecessors = {v:[] for v in graph.keys()}     #keep track of predecessors that assigned the shorted value
pq = PriorityQueue()


def dijkstra(graph, start):
    D[start] = 0    #assign 0 cost to the start node
    pq.put((0,start))
    while not pq.empty():
            (dist, current_vertex) = pq.get()
            if current_vertex not in visited:
                visited.append(current_vertex)
            for neighbor in graph[current_vertex]:
                    distance = graph[current_vertex][neighbor]
                    if neighbor not in visited:
                            old_cost = D[neighbor]
                            new_cost = D[current_vertex] + distance
                            if new_cost < old_cost:
                                    pq.put((new_cost,neighbor))
                                    D[neighbor] = new_cost
                                    predecessors[neighbor].append(current_vertex)


#recursively traceback the shortest path from end node to start node
def printPath(end):
    print(end)
    if len(predecessors[end]) > 0:
        printPath(predecessors[end][-1])
    else:
        print("Traced complete")

def printValue(end):
    print(f"At the cost of ",D[end])



#change values
start = 'A'
end = 'F'

dijkstra(graph, start)
printPath(end)
printValue(end)

