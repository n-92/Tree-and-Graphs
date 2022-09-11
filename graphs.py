graph = dict()
graph['A'] = ['B','G','D']
graph['B'] = ['A','E','F']
graph['C'] = ['F','H']
graph['D'] = ['F','A']
graph['E'] = ['B','G']
graph['F'] = ['B','D','C']
graph['G'] = ['A','E']
graph['H'] = ['C']

inv_graph = {tuple(v): k for k, v in graph.items()}


#Breadth First Search
queue = []
visited = []
queue.append(graph['D'])
while len(queue) > 0:
    node = queue.pop(0)
    if inv_graph[tuple(node)] not in visited:
        visited.append(inv_graph[tuple(node)])
    for neighbor in node:
        if neighbor not in visited:
            queue.append(graph[neighbor])
    
print(visited)


#Depth First Search
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'B')