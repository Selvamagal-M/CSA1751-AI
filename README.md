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
        
A* Algorithm

      while open_list:
    _, current = heapq.heappop(open_list)

    if current == goal:
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(start)
        return path[::-1]

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        neighbor = (current[0] + dx, current[1] + dy)

        if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current

Min-Max  

           def minimax(depth, node_index, is_max, scores, h):
    if depth == h:
        return scores[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, scores, h)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, scores, h)
            best = min(best, val)
        return best

        
Greedy Best-First Search (GBFS)


        while pq:
        
         h, node, path = heapq.heappop(pq)
    
    if node == goal:
        return path

    for neighbor in graph[node]:
        priority = heuristics[neighbor]
        heapq.heappush(pq, (priority, neighbor, path + [neighbor]))
Alpha-Beta Pruning 


     def alpha_beta(depth, index, is_max, scores, h, alpha, beta):
    if depth == h:
        return scores[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, False, scores, h, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, scores, h, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break
        return best

Decsion Tree

     # The algorithm selects the best feature using:
     Information_Gain = Entropy_Before - Entropy_After_Split


     
