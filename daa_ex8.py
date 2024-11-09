#Hamilton cycle using backtracking
def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True
def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False
def hamiltonian_cycle(graph):
    path = [-1] * len(graph)  # Initialize path
    path[0] = 0  # Start from the first vertex
    if not hamiltonian_cycle_util(graph, path, 1):
        print("Solution does not exist")
        return False
    print("Solution Exists: Following is one Hamiltonian Cycle")
    print(" -> ".join(map(str, path)) + " -> " + str(path[0]))
    return True
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
hamiltonian_cycle(graph)
