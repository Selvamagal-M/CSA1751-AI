import math

def minimax(depth, node_index, is_maximizing, scores, h):
    if depth == h:
        return scores[node_index]

    if is_maximizing:
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

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    tree_height = 3
    result = minimax(0, 0, True, scores, tree_height)
    print("Optimal Value:", result)
