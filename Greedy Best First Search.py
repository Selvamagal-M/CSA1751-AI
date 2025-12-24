import heapq

def gbfs(graph, start, goal, heuristics):
    pq = [(heuristics[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        
        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                priority = heuristics[neighbor]
                heapq.heappush(pq, (priority, neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }

    heuristics = {
        'A': 6, 'B': 4, 'C': 4, 'D': 5, 'E': 2, 'F': 3, 'G': 0
    }

    print(gbfs(graph, 'A', 'G', heuristics))
