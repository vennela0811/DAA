import collections
from collections import deque

graph = {
    0: [1, 5],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1, 6],
    4: [1, 5],
    5: [0, 4],
    6: [3]
}

# BFS
def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end = " ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS
def dfs(node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end = " ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


print("\nBFS: ", end=" ")
bfs(0)

print("\nDFS: ", end=" ")
dfs(0)

"""
BFS - TC: O(V + E), SC: O(V)
DFS - TC: O(V + E), SC: O(V)

"""
        