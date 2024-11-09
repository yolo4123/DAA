from collections import defaultdict

def bcc(graph):
    def dfs(u, parent):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        for v in graph[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    component = []
                    while stack[-1] != v:
                        component.append(stack.pop())
                    component.append(stack.pop())
                    component.append(u)
                    biconnected.append(component)
            elif v != parent:
                low[u] = min(low[u], disc[v])

    disc = defaultdict(lambda: -1)
    low = {}
    stack, biconnected = [], []
    time = 0
    for node in graph:
        if disc[node] == -1:
            dfs(node, None)
    return biconnected
def scc(graph):
    def dfs(u):
        nonlocal time
        disc[u] = low[u] = time  # Discovery and low-link values
        time += 1
        stack.append(u)
        on_stack[u] = True
        for v in graph[u]:
            if disc[v] == -1:  # If `v` is not visited
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:  # If `v` is on the stack, update the low-link value
                low[u] = min(low[u], disc[v])
        if low[u] == disc[u]:  # Found a strongly connected component
            component = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                component.append(v)
                if v == u:
                    break
            scc_list.append(component)
    disc = defaultdict(lambda: -1)  # Discovery times of visited nodes
    low = defaultdict(int)           # Lowest points reachable from each node
    on_stack = defaultdict(bool)      # To check if a node is in the stack
    stack, scc_list = [], []
    time = 0
    for node in graph:
        if disc[node] == -1:
            dfs(node)
    return scc_list
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
print(scc(graph))
print(bcc(graph))
