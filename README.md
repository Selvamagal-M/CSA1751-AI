Uniform Cost Search (UCS)


    while priority_queue:
    cost, node, path = heapq.heappop(priority_queue)
    
    if node == goal:
        return cost, path

    if node not in visited:
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )
Breadth-First Search (BFS)

    while queue:
    
    node = queue.popleft()
    bfs_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
            

Depth-First Search (DFS)
 

     visited.add(start)
    dfs_order.append(start)
 
    for neighbor in graph[start]:
      if neighbor not in visited:
        dfs(graph, neighbor, visited, dfs_order)
