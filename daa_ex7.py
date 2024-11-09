#graph coloring using backtracking 
def is_safe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:  # Check if any adjacent vertex has the same color
            return False
    return True
def graph_coloring_util(graph, m, color, v):
    if v == len(graph):  # If all vertices are assigned a color
        return True
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c  # Assign color c to vertex v
            if graph_coloring_util(graph, m, color, v + 1):  # Recursively assign colors to the rest of the vertices
                return True
            color[v] = 0  # Backtrack
    return False
def graph_coloring(graph, m):
    color = [0] * len(graph)  # Initialize all vertices with color 0 (no color assigned)
    if not graph_coloring_util(graph, m, color, 0):
        return "Solution does not exist"
    return color
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]]
m = 3 
result = graph_coloring(graph, m)
print("Color assignment:", result)
